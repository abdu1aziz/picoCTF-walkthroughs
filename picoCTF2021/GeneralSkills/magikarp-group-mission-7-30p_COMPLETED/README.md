## General Skills - # 7 
  

|Code Name|Points |  
|--|--|  
| Tab, Tab, Attack | 30p |  
  
 - First I had to connect to server via ssh.
 - I was provided with login information, as the CTF contains a docker instance that launches upon performing CTF.
 - Now I went ahead and used the provided credtienials to login.
 - Upon logging in I was presented with Ubuntu instance shell session.
 - I navigated to the directory called `drop-in`, and started collecting pieces of my flag.
 - The following commands were used:
	 - [x] `I quickly realized the structure of the directories and decieded to create a simple command oneliner to drop the flag`
	 - [x] `cat 1of3.flag.txt && cat ../../../2of3.flag.txt && cat ../3of3.flag.txt`
- Finally I got back the Magically flag: `picoCTF{ORIGINAL_FLAG_HIDDEN}`

> I decided to hide the original flag, so you can go try to find our flag on your own.


![enter image description here](https://imgur.com/HgGt7EDl.png)