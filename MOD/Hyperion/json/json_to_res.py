import csv
import json
import struct
import sys
import os

# ---------------------------------------------------------
# JSON to RES conversion utility
#
# Minimal required Python version: 3.10
# Usage example: python.exe json_to_res.py diplo.res.json
# ---------------------------------------------------------

VERSION_STRING = b"(C) H.D.I. V1.0\x1A"

def getSize(format):
    return struct.calcsize('<' + format)

HEADER_ENTRY_SIZE = getSize('12sl')

sections = {}
offsets = {}

def readCsvSection(csvreader):
    row1 = next(csvreader)
    categoryName = row1[0]
    for row in csvreader:
        if all(txt == '' for txt in row):
            return
        lists = sections.setdefault(categoryName, [])
        lists += [[] for _ in range(0, (len(row) - len(lists)))]
        for index, el in enumerate(row):
            if (el != ''):
                offsets[categoryName] = offsets.setdefault(categoryName, 0) + len(el)
                lists[index].append(el)

def parseCsvFile():
    with open("test.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        while True:
            try:
                readCsvSection(csvreader)
            except StopIteration:
                break

def getPaddedFormat(txt, size):
    return '{}s{}x'.format(len(txt), size - len(txt))

def packWrite(file, format, *data):
    file.write(struct.pack('<' + format, *data))

def packWriteStr(file, txt, pad=None):
    encodedStr = txt.encode(encoding='ansi')
    if pad is None:
        file.write(struct.pack('{}s'.format(len(encodedStr)), encodedStr))
    else:
        file.write(struct.pack(getPaddedFormat(encodedStr, pad), encodedStr))

def getStrSize(txt, pad=None):
    if not txt:
        return 0
    #txt = txt.replace("\\n", "\n").replace("\\\"", "\"")
    encodedStr = txt.encode(encoding='ansi')
    if pad is None:
        return struct.calcsize('{}s'.format(len(encodedStr)))
    else:
        return struct.calcsize(getPaddedFormat(encodedStr, pad))

def packLenStr(file, txt):
    #txt = txt.replace("\\n", "\n").replace("\\\"", "\"")
    packWrite(file, 'h', len(txt))
    if txt:
        packWriteStr(file, txt)

def getLenStrSize(txt):
    return getSize('h') + getStrSize(txt)

control_types = {
    "custom": 0,
    "button": 1,
    "static": 2,
    "menubar": 3,
    "edit": 4,
    "scroll": 5,
    "listbox": 6,
    "bitmask": 7
}

def parseControlType(typeStr):
    return control_types[typeStr]

def packWriteControl(file, control):
    type = parseControlType(control['type'].lower())
    packWrite(file, "9l", type, control['id'],
     control['x'], control['y'], control['dx'], control['dy'],
      control['style'], control['fore'], control['back'])
    packLenStr(file, control.get('name', ''))
    match type:
        case 7 | 2:
            packLenStr(file, control.get('data', ''))
        case 1 | 3:
            packLenStr(file, control.get('data1', ''))
            packLenStr(file, control.get('data2', ''))
        case 4:
            packWrite(file, "l", control['maxLength'])
        case 5:
            packWrite(file, "ll", control['range'], control['page'])

def getControlSize(control):
    size = getSize("9l") + getLenStrSize(control.get('name', ''))
    type = parseControlType(control['type'].lower())
    match type:
        case 7 | 2:
            return size + getLenStrSize(control.get('data', ''))
        case 1 | 3:
            return size + getLenStrSize(control.get('data1', '')) + getLenStrSize(control.get('data2', ''))
        case 4:
            return size + getSize("l")
        case 5:
            return size + getSize("ll")
    return size

def packWriteColumn(file, column):
    items = column.get('items', [])
    # winId = number of unit +
    # 2000 if struct
    # 3000 if unit
    packWrite(file, "LBBHHHHL", 0, column['hotkey'], column['flags'], column['textWidth'], 0,
     len(items), column['winId'], len(items))
    if 'text' in column:
        packLenStr(file, column['text'] + '\0')
    else:
        packLenStr(file, '')
    for item in items:
        packWrite(file, "LBBH", 0, item['hotkey'], item['flags'], item['winId'])
        if 'text' in item:
            packLenStr(file, item['text'] + '\0')

def getColumnSize(column):
    size = getSize("LBBHHHHL")
    tempsize1 = size
    if 'text' in column:
        size += getLenStrSize(column['text'] + '\0')
    else:
        size += getLenStrSize('')
    for item in column.get('items', []):
        tempsize = size
        size += getSize("LBBH")
        if 'text' in item:
            size += getLenStrSize(item['text'] + '\0')
        else:
            size += getLenStrSize("")
    return size

def getStringSize(string):
    return getSize("h") + getLenStrSize(string['value'])

def getSectionSize(section):
    controls = section.get('controls', [])
    if 'controls' in section:
        return getSize('6h') + sum(getControlSize(control) for control in controls)
    columns = section.get('columns', [])
    if 'columns' in section:
        return getSize('h') + sum(getColumnSize(column) for column in columns)
    strings = section.get('strings', [])
    if 'strings' in section:
        return getSize("h") + sum(getStringSize(string) for string in strings)

def calculateOffsets(base):
    offset = base
    for key, contents in sections.items():
        offsets[key] = offset
        #print(getSectionSize(contents))
        offset += getSectionSize(contents)

def parseJsonFile(filename):
    with open(filename) as jsonfile:
        contents = jsonfile.read()
        # if not contents.startswith('{'):
        #     contents = '{' + contents
        # if not (contents.endswith('}') or contents.endswith('}\n') or contents.endswith('}\r\n')):
        #     contents = contents + '}'
        contents = '{\n' + contents + '\n}'
        #with open(filename + "debug", "w") as debugfile:
        #    debugfile.write(contents)
            
        global sections
        sections = json.loads(contents)

def usage():
    print("Usage: " + sys.argv[0] + " input_file.json output_file.res")

def processJsonFile(inFilename, outFilename):
    parseJsonFile(inFilename)

    calculateOffsets(len(VERSION_STRING) + len(sections) * HEADER_ENTRY_SIZE)
    with open(outFilename, "wb") as resfile:
        # write header
        resfile.write(VERSION_STRING)
        for section in sections:
            packWriteStr(resfile, section, 12)
            packWrite(resfile, 'l', offsets[section])

        # write contents of each sections
        for name, contents in sections.items():
            if 'columns' in contents:
                columns = contents.get('columns', [])
                packWrite(resfile, "H", len(columns))
                for column in columns:
                    packWriteColumn(resfile, column)
            elif 'strings' in contents:
                strings = contents.get('strings', [])
                packWrite(resfile, "h", len(strings))
                for string in strings:
                    packWrite(resfile, "h", string["ID"])
                    packLenStr(resfile, string["value"])
            elif 'controls' in contents:
                controls = contents.get('controls', [])
                packWrite(resfile, "6h", contents['x'], contents['y'], contents['dx'], contents['dy'], contents['style'], len(controls))
                for control in controls:
                    packWriteControl(resfile, control)

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        for filename in os.listdir("."):
            if filename.endswith(".json"):
                processJsonFile(filename, filename[:-4])
        exit()
    outFilename = sys.argv[1][:-4] if len(sys.argv) == 2 else sys.argv[2]

    processJsonFile(sys.argv[1], outFilename)
