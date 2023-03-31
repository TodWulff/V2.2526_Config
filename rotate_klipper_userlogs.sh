#!/usr/bin/env bash

/usr/sbin/logrotate -v -f /home/pi/printer_data/logs/klipper_userlogs.conf

#needs a service restart to allow loggers to get new file handles
#systemctl restart klipper  # nixed this in favor of tossing a reboot confirmation dialog via UI

# this was a painful implementation - might be all I did, might not.  Not too sure...
# I was like a fat bastard in a candy shop (I can say that as I taint thin... :)

# in no particular or known/recalled order:
# - used the shebang above
# - sudo ln -s /home/pi/printer_data/config/rotate_klipper_userlogs.sh /usr/bin/rotate_klipper_userlogs

# - created /etc/sudoers.d/sudo-for-brody-scripts
# - pi ALL = (root) NOPASSWD: /usr/sbin/logrotate args, /home/pi/printer_data/config/rotate_klipper_userlogs.sh

# - ended up chmod'g: 
# - sudo chmod 777 /var/lib/logrotate
# - sudo chmod 777 /var/lib/logrotate/status
