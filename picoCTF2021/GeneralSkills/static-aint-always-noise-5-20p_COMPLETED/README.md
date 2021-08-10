## General Skills - # 5
  

|Code Name|Points |  
|--|--|  
| Static Ain't Always Noise | 20p |  
  

 - I quickly got a binary file, and shell script.
 - My First assumption after reading the prompt was that I need to find the flag in `static` binary file using shell script called `ltdis.sh`
 - Before I did all that decided to run my own basic command that I usually run on all binaries.
 - I ran `cat static | grep -a "picoCTF{"`
 - And sure enough I found the flag: `picoCTF{ORIGINAL_FLAG_HIDDEN}GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.08Tt`

> I decided to hide the original flag, so you can go try to find our flag on your own.