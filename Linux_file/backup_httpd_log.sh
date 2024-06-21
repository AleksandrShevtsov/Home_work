#!/bin/bash
#
LOG_DIR="/var/log/httpd"
BACUK_DIR="/home/ec2-user/backup_log"

mkdir -p "$BACUK_DIR"

DATE=`date +%Y%m%d-%H%M`

ARHIVE="backup_log-$DATE.tar.gz"

sudo tar -czf "$BACUK_DIR/$ARHIVE" "$LOG_DIR"

sudo find "$BACUK_DIR" -type f -name "backup_log-*.tar.gz" -mtime +3 -exec rm {} \;

sudo rm "$LOG_DIR/access_log"

sudo service httpd restart  

