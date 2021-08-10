import sys


usage_msg = "Usage: "+ sys.argv[0] +" (-d [ for decoding]) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To find Flag run the netcat command and > output to a file. " +\
        "'$ python "+ sys.argv[0] +" -d output.txt'\n"



if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(usage_msg)
    sys.exit(1)


if sys.argv[1] == "-d":
	if len(sys.argv) > 2:
		filename   = open(sys.argv[2], 'r')
		ascii_list = filename.read().splitlines()
		print(''.join(chr(int(i)) for i in ascii_list))