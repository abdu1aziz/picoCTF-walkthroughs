## General Skills - # 4  
  

|Code Name|Points |  
|--|--|  
| Nice Netcat.. | 15p |  
  

 - First I had to connect to server via netcat.
 - The response came out in list of integers.
 - After couple of seconds of staring at them, I quickly realized they were in **ASCII** format.
 - Now I decided to show of my messy python scripting skills, and wrote a quick script called: `flagFinder.py`
 - With the help of this script I the following commands:
	 - [x] `nc mercury.picoctf.net 22342 > output.txt`
	 - [x] `python flagFinder.py -d output.txt`
- Finally I got back the Magically flag: `picoCTF{ORIGINAL_FLAG_HIDDEN}`

> I decided to hide the original flag, so you can go try to find our flag on your own.