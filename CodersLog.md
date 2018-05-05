# Bitcoin-Explained
This repository will be the beginning of my project to execute the SHA-256 Program inside simple programming languages. the end product of this will be to create a simple game, possible an app that allows a person to manually solve SHA-256 Problems to mine bitcoin. This is not meant to be a profitble project, but instead an educational one.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Log Day 1. 11:40pm/April 30th/2018
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

I'll admit, I have no idea what I'm doing.

 so I'm just winging this and gonna keep my notes and thoughts in this log.

I saw a video about how the SHA-256 Protocol was a set of simple calculations that even a person could do, that the main problem comes with from the random geuss and check nature of bitcoin and the difficulty it is set at in order to create a set of zeros to succesffully "solve" the hash. This has inspired me to create an educational game that will give me a better understanding of bitcoin but also serve as a fun educational took for others. 

Oh yeah, also it will be my first ever coding project I do alone..

So, ok, Think Donnum. What do we need. What do you want to do in this project?

I wanna create a website, that when people go to are brought to a browser game that leads them through the SHA-256 Protocol in a game like mannerer. I want this to flow kinda like http://ncase.me/trust/ (which honestly is an amazing explanation for the game theory that Richard Dawkins discussed in his book "The Selfish Gene") in the sense that it allows for user input but creates a linear path for explanation of the process.

SO far so Good. Now, what do I need for the website? For now I'll list the things I vaguely heard about that a website needs. I an ignornant of many of them but hey we all start somewhere.

1. Frontend (This is the HTML5 browser interface I think.)
2. Backend (I'm not sure but I think this is the program that does the actually computational problems.)
3. Website-Host (I think hostGator could work, I already have an account with them.)
4. Storage-Host/Cloud-Computing (I think this terminology is that I can pay a company to do the computations on their network, hostgator?)
5. Visual/Sprites (I can create these using my drawing pad, I wonder if I'll have to learn about vector files for this.)
6. Ad-Space/Monetization (Use Google Ads or partner with a store maybe? What? Don't judge me, hosting isn't free and a guys gotta eat.)
7. SHA-256 Steps and History (Shouldn't this be placed as my first step?.)

Ok, so those are the 7 main things I can think of that I need to do. Let's start with Step 7, then Step 2. I need to decide what language I can use, I know rudemnetary Python up to functions, and Matlab up to functions and graphs, would either of those work for the backend. I'm going blind into this with minimal coding experience, $419 CAD saved up for expenses, and a shit load of time. I love it.

By the time I come back, I'll have researched all this stuff more, and worked on a Beta (Is that the right word?) for the SHA-256 in it's basic form. also next time I'll make sure to make my Log short and simple, Untill them.

This is Donnum, signing off.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Log 2. 6:17pm/May 4th/2018
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

Oh boy what I have got into to.

So far I've learned the basics of Python, I/O and all of that, so I think I can can google enough info to get this beta working. The whole idea of this beta is to just create a proof that I can run the SHA-256 protocol in the most basic, generic way possible. From there I can work out how I can grow from it. I'll add my next log when I finish the beta. 

Oh yeah, this is the basic moves of SHA-256 used from 8 blocks with difficulty of 17 zeros

1. Convert all hashes to binary 
2. Hashes 1,2,3 have a position comparison, where if #1's < #0's MA-Hash = 1 in new position, otherwise MA-Hash = 0.
3. Hash 1 is rotated 3 times, shifted right 2,13 and 22 bits respectively. if #1 is odd, Sum-0 Hash is 1 in that position
4. Hash CH is created by mixing hashes 6 & 7 choosing from hash 5, where if hash 5 = 1 it takes the bit from hash 6 otherwise takes bit from has 7
5. Hash 5 is then rotated like 1, only 6,11,25 bits right. summed up simillarly. creates Sum-1
6. w_t and k_t undero 32-bit addition produce P_t
7.  P_t and CH undergo 32-bit addition o creat CHP_t
8. Sum-1 and CHP_t undergo 32-bit addition to create CHP-1 
9. CHP-1 and hash 4 undergo 32-bit to create the new Hash 5
10. MA-Hash, and CHP-1 undergo 32-bit to create MA-cHP-1 
11. MA-CHP-1 and Sum-0 undergo 32bit to creat MCP-10 which becomes the new A block. this is the block that must have 17 zeros to produce a succesfful mine/answer to the question.

these are the general steps I have, need to define 32-bit addition and what K_t(constants) and how to produce W_t(input) but after that I believe I will have all I need to solve SHA-256.



This is Donnum, signing off.
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 


