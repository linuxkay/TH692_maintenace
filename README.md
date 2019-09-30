# TH692 networkcam maintenace tools

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

# Other notes
sync date and time etc.
py file syncs date and time of isolated cam(wich does not have access to outside of LAN).


# License

MIT

# Author

Linuxkay
