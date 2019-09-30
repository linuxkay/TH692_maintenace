HOST='192.168.0.100'
USER='root'
PASSWD='passwordofth692'
CMD=''
#Show current time in specific time formart
NOWTIME="$(date +"%Y-%m-%d %H:%M:%S"
)" 
# This is for debug to dislpay current time in local machine
#echo "${NOWTIME}"
(
echo open "$HOST"
sleep 0.2
echo "$USER"
sleep 0.2
echo "$PASSWD"
sleep 0.2
# Manual way to set time in specific time format
#echo "date -s '2000-12-12 11:14:00'"
echo "date -s '${NOWTIME}'"
# Need sleep 0.6 to wait for date -s command to be executed
sleep 0.6 
echo "exit"
) | telnet
