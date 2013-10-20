#!/bin/sh
# An empty init.d file, with start|stop|restart functionality, that starts a screen daemon
# Trevor Stanhope

# system user to run as
user="user"

# the full path to the filename where you store your configuration
config="`su -c 'echo $HOME' $user`/.rtorrent.rc"

# default directory for screen, needs to be an absolute path
base="`su -c 'echo $HOME' $user`"

# set command
command=""

# set options
options=""

# name of screen session
srnname=""

PATH=/usr/bin:/usr/local/bin:/usr/local/sbin:/sbin:/bin:/usr/sbin
DESC=""
NAME=
DAEMON=$NAME
SCRIPTNAME=/etc/init.d/$NAME

# file to log to
logfile="/var/log/$NAME.log"

checkcnfg() {
    exists=0
    for i in `echo "$PATH" | tr ':' '\n'` ; do
        if [ -f $i/$NAME ] ; then
            exists=1
            break
        fi
    done
    if [ $exists -eq 0 ] ; then
        echo "cannot find binary in PATH $PATH" | tee -a "$logfile" >&2
        exit 3
    fi
    if ! [ -r "${config}" ] ; then 
        echo "cannot find readable config ${config}. check that it is there and permissions are appropriate" | tee -a "$logfile" >&2
        exit 3 
    fi 
}

d_start() {
  [ -d "${base}" ] && cd "${base}"
  stty stop undef && stty start undef
  su -c "screen -ls | grep -sq "\.${srnname}[[:space:]]" " ${user} || su -c "screen -dm -S ${srnname} 2>&1 1>/dev/null" ${user} | tee -a "$logfile" >&2
  su -c "screen -S "${srnname}" -X screen ${command} ${options} 2>&1 1>/dev/null" ${user} | tee -a "$logfile" >&2
}

d_stop() {
    
}

checkcnfg

case "$1" in
  start)
    echo -n "Starting $DESC: $NAME"
    d_start
    echo "."
    ;;
  stop)
    echo -n "Stopping $DESC: $NAME"
    d_stop
    echo "."
    ;;
  restart)
    echo -n "Restarting $DESC: $NAME"
    d_stop
    sleep 1
    d_start
    echo "."
    ;;
  *)
    echo "Usage: $SCRIPTNAME {start|stop|restart}" >&2
    exit 1
    ;;
esac

exit 0
