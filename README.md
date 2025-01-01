# Hyperion
Hyperion MOD for the Emperor of the Fading Suns V1.52 Game

# Description
This is a public repository for my work on the Hyperion MOD.

# Story

The year is 6000 A.D.

The Known Worlds have seen the Emperor Wars come and go, the rise of the Third Republic, and the subsequent fall back into another period of Dark Ages that have lasted for the past 750 years. Somehow, through all that, the Houses, League, Church, Ministries, and Aliens have survived it all and Mankind is now on the precipice of the reemergence from this new Dark Period. Technology is at a level of World War I and so this is where we find ourselves today, Mylord. While everyone is at peace, this will only hold true as long as the balance of power can be maintained. The Church has reemerged to assert its authority over technological research again, and it is rumored that the League is slowly rebuilding in an attempt to create the Fourth Republic. Regent elections will begin anew and little is know of the Symbiot threat, which suddenly disappeared during the Third Republic. The Vau are still as mysterious as ever and now, Mylord, it is time to advance the status of our House, to its previous, historical glory.

# Details
This repository will contain the files for the Hyperion MOD for EFS V1.52.

Hyperion specializes in developing a very satisfying game playing experience that will require the player to manage their empire with much better skill than the standard game in order to be successful, including:

1. Massive technology tree, that will require several playthroughs to see every tech.
2. Vast amount of units that start from the World War 1 era into a foreseeable Fading Suns future.
3. Formulaic unit design where each unit is designed with a point system in mind to ensure that the unit is balanced for the technology required to build it. Resource utilization, time to build, and unit cost and upkeep are all generated via formulas to ensure that these values are appropriate for the specific unit. This point system ensures that each unit is designed such that when acquired, it is useful and better than its predecessors making technology research crucial to a player's success in the game. Real world military unit asymmetry and then a gradual change to symmetry as technology advances, ensure that Houses must keep researching technology to stay ahead of the other Houses, or start to fall behind.
4. Firebird management is much more critical with players having to manage their economy properly in order to succeed.
5. A lot of time has been spent on researching Military units of World War 1, the Interim Period, World War 2, the Cold War, Modern Warfare, and potential future warfare and unit designs have taken into account the various issues of those units as they were put into service. For example, the very first Tanks were pretty bad, as well as Aviation units; however, they have a utility during the early game where their use is part of that natural progress of humanity. Additionally, there were many units that were theorized but never implemented; only prototypes built, but never put into service; or units that were used, but found to be ineffective. Hyperion explores all this to show what could have been possible.
6. Virtually every city type has unique units that it can either build or upgrade and so building units is significantly more interesting.

# Background
I created Hyperion for EFS back in the day during the late 1990's as I was inspired by the Nova MOD. I spent the next several years working on Hyperion with the last version, 1.4, released around the 2003 or so time frame and it was one of the most popular MODs at the time.

Realizing that I could never perfect the MOD with the deficiencies in the previous V1.4 EFS release, I acquired the game code from Andrew Greenberg and started working on fixing the game. Unfortunately, I did not have the requisite C++ programming experience / skill to fix many of the issues with the original code and so went through 3 different development periods between 2005 to 2008, 2015, and 2017, burning out each time due to my inability to fix the game code sufficiently to prevent random crashes while playing.

Nonetheless, all this development was saved in an Assembla repository where the changes that I made were put into "cold strorage" where they could still be accessed if needed.

In December 2021, I was once again contacted by Andrew to work on EFS V1.5. I decided to try once again, but this time we had an experienced C++ programmer on the team, Aleksandr Dorogov, and he was able to solve pretty much all the issues that I couldn't and I was allowed to focus on fixing / changing the issues that I could. I brought my changes out of cold storage that I worked on in the past (some of them were 15+ years old!) and one by one, started putting these changes into the eventual EFS V1.5. To this end, using Hyperion as my guide, the development team (which also includes Boris Okolodkov, who did a lot of the FLC art for Hyperion, Andrew, and Nikolai Skauge, who is a fellow MODder (he is currently developing Empyrean) and has been running the EFS Discord channel for many years keeping EFS's heartbeat going) was able to create EFS V1.5 that has many of the previous issues / restrictions either fixed or lifted.

With the release of EFS V1.5, I felt that my work on the game patch was still incomplete as I had issues with trying to implement Hyperion with V1.5 and there were still many, many loose ends. So we started working on EFS V1.51 immediately after the release of EFS V1.5. During the development period we added some amazing new teams members to help with the development of EFS V1.51: 1) Jonathan Campbell who has been instrumental in testing our proposed changes to a high level of quality and 2) Nicola Parolin who is the original developer of the Emperor Wars MOD and is equally adept and making changes to the game code. With these new team members, we were able to develop EFS V1.51 and release it at the end of February 2023.

With the release of EFS V1.51, I took a break from EFS for a bit to work on other personal projects, but once again returned towards the last Quarter of 2023. Once again, I found myself, programming and once again I couldn't work on Hyperion. Then in the second quarter of 2024, we added another experienced programmer to the team, Tomas Mecir, and with that we had a programmer that could take over the coding of the game and let me work on Hyperion once again. So I have spent the second half of 2024 working on Hyperion again, getting it to the state it is in today.

1. Hyperion has 450+ technologies of which I'd estimate the tech tree to be 95 to 99% complete.
2. Hyperion has almost 1000 units of which I'd estimate this will be 20 to 25% of the final unit count when I'm done.
3. I've created unit art (both BMP's / PNG's and GIF's / FLC's) of about 75% of these units, with unit variants using palette shifted artwork to help with filling in missing artwork. I've either used the original EFS game artwork, artwork created for Hyperion in the past, or I've used mostly Stable Diffusion to AI generate new artwork. I have sufficient artwork generated to create artwork for all the current units, for the most part, and just need time to filling in what is missing. What I need the most help with is generating the 32 x 32 pixel Unit Icon artwork. Since I'm colorblind, I find that when I downscale artwork from 175 x 150 to 32 x 32, sometimes the resulting image doesn't have a lot of detail. I struggle a bit with getting it to look good so a lot of the Unit Icon 32 x 32 pixel artwork needs some improvement. I'm hoping someone will be able to help me with that in the future.

# Schedule

We are now in the year 2025 and we are working on a new EFS release; however, I've been able to spend significant time on Hyperion and have just updated the Hyperion Historical Galaxy such that the MOD is in a playable state. While all the current units having been properly designed, I need to work on the Space units to better implement my vision for these units. Also, there are significant gaps in unit areas, that I will fill once I start playtesting the MOD more.

It is my hope that I'll be able to get the MOD 80 to 95% complete by the end of 2026.

Areas that need work or that I haven't started on:

1. The Manowitz Volumes - I actually have a significant automation capability here, but need to add new information for new technologies and new units.
2. Finishing up the missing artwork - note that units that don't have artwork are fully playable, it's just that their Unit Icon and / or FLC artwork is blank.
3. Filling in missing Technologies and Units. For the Tech Tree, I think this is mostly complete, but for the units there are a lot of units that need to be added (Drone-like units, automaton units, gaps in technological research areas, etc.).
4. Ensuring that unit designs are not convergent. While a lot of time has been spent designing units with the point system, it is possible that I've designed units with stats that are too similar. I need to check all this out and ensure there is enough unit statistic separation for similar unit designs.
5. Playtesting - I need to check to see how the game plays. It should be noted that Hyperion technology research with be significantly slower than the standard game; however, the number of units available to build will be significantly greater than the main game, even at the start. As the game is played, various gaps will become apparent where there are unit gaps for technological advancement. This is the area that needs a significant amount of work.