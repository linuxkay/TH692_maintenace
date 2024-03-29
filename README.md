# TH692 networkcam maintenace tools

## Category

Network Camera management

## Description
Sync date and time TH692 network cam remotely.

Programs to sync date and time of network isolated TH692 camera (wich does not have internet access: only LAN).


## Memo

For security reasons, I putted RaspberryPi1B in LAN which does not have internet access. Only ssh access to other machines(connected to internet)

I needed telent commnad in Pi. It does not come with it by default. So I had to download `telnet.deb` package by the command `sudo apt download telnet` in the machine(connected to internet) and scp to raspberrypi1B

Finally I could install telnet by `dkpg` command in RaspberryPi1B

## Requirements

telnet

`sudo apt install telnet`

python3

`sudo apt install python3`

## Bechmark results

sh `setTimeforCAM.sh` VS python3 `setTimeforCAM.py`

shell version hits max 14% cpu usage in RaspberryPi1B

python version hits 100% cpu usage in RaspberryPi1B

Recommend using shell version.

It's faster and lighter.

## Credits 

<a href="https://unix.stackexchange.com/questions/247336/make-a-shell-script-execute-commands-in-telnet-or-programs">StackExchange: Make a shell script execute commands in telnet or programs</a>


<a href="https://stackoverflow.com/questions/4651437/how-do-i-set-a-variable-to-the-output-of-a-command-in-bash">Stack Overflow :shell - How do I set a variable to the output of a command in Bash</a>


## Updates

2019/09/30

Added `setTimeforCAM.sh`

`setTimeforCAM.sh` only requires `telnet` since TH692 only have telnet access.

Previous network settings.
![previous_network_settings](https://user-images.githubusercontent.com/9047935/125162936-ae0fa580-e1c5-11eb-82a6-075879ea6f03.png)



## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
