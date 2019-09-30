# TH692 networkcam maintenace tools

# Description
Sync date and time of TH692 remotely.

Programs to syncs date and time of network isolated TH692 camera (wich does not have access internet).


#Update info

2019/09/30

Added `setTimeforCAM.sh`

`setTimeforCAM.sh` only requires `telnet` since TH692 only have telnet access.


# Requirement

telnet

sudo apt install telnet 

python3

sudo apt install python3

# Bechmark results

sh `setTimeforCAM.sh` VS python3 `setTimeforCAM.py`

shell version hits max 14% cpu usage in RaspberryPi1B

python version hits 100% cpu usage in RaspberryPi1B

Recommend using shell version.

It's faster and lighter.

# Credits 

<a href="Make a shell script execute commands in telnet or programs">StackExchange: Make a shell script execute commands in telnet or programs</a>


<a href="https://stackoverflow.com/questions/4651437/how-do-i-set-a-variable-to-the-output-of-a-command-in-bash">Stack Overflow :shell - How do I set a variable to the output of a command in Bash</a>

I don't use bash at all so it was huge help.

# License

MIT

# Author

Linuxkay
