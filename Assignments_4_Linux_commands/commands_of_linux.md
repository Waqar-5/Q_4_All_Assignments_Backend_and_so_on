# Essential Linux Commands – Complete Developer Guide

This README contains all commonly used Linux commands, grouped into categories, with **detailed explanations, examples, and usage tips**. Fully editable for your notes and reference.

---

## 1. File & Directory Management

| Command  | Description                | Example                                             |
| -------- | -------------------------- | --------------------------------------------------- |
| `ls`     | List files and directories | `ls -l /home`                                       |
| `cd`     | Change directory           | `cd /var/log`                                       |
| `pwd`    | Print current directory    | `pwd`                                               |
| `mkdir`  | Create directory           | `mkdir project`                                     |
| `rmdir`  | Remove empty directory     | `rmdir old_folder`                                  |
| `rm`     | Remove files/directories   | `rm file.txt`<br>`rm -r folder/`                    |
| `cp`     | Copy files/directories     | `cp file1.txt file2.txt`<br>`cp -r folder1 folder2` |
| `mv`     | Move or rename files       | `mv file.txt /tmp/`<br>`mv oldname.txt newname.txt` |
| `touch`  | Create empty file          | `touch newfile.txt`                                 |
| `find`   | Search files               | `find /home -name '*.log'`                          |
| `locate` | Fast search using database | `locate file.txt`                                   |
| `tree`   | Display directory tree     | `tree /home/user`                                   |

**Tip:** Use `ls -lah` for human-readable sizes and hidden files.

---

## 2. File Viewing & Manipulation

| Command | Description                       | Example                        |
| ------- | --------------------------------- | ------------------------------ |
| `cat`   | Display file content              | `cat file.txt`                 |
| `less`  | Page-by-page view                 | `less file.txt`                |
| `head`  | Show first lines                  | `head -n 20 file.txt`          |
| `tail`  | Show last lines                   | `tail -n 20 file.txt`          |
| `grep`  | Search text in files              | `grep 'error' /var/log/syslog` |
| `awk`   | Text processing                   | `awk '{print $1}' file.txt`    |
| `sed`   | Stream editor for replace         | `sed 's/old/new/g' file.txt`   |
| `cut`   | Extract columns                   | `cut -d',' -f1 file.csv`       |
| `wc`    | Count lines, words, characters    | `wc -l file.txt`               |
| `diff`  | Compare two files                 | `diff file1.txt file2.txt`     |
| `cmp`   | Compare binary files              | `cmp file1 file2`              |
| `comm`  | Compare sorted files line by line | `comm file1.txt file2.txt`     |

---

## 3. File Permissions & Ownership

| Command   | Description                 | Example                         |
| --------- | --------------------------- | ------------------------------- |
| `chmod`   | Change permissions          | `chmod 755 file.txt`            |
| `chown`   | Change file owner           | `chown user:group file.txt`     |
| `chgrp`   | Change group                | `chgrp developers file.txt`     |
| `umask`   | Set default permission mask | `umask 022`                     |
| `ls -l`   | View permissions            | `ls -l file.txt`                |
| `stat`    | Detailed file info          | `stat file.txt`                 |
| `getfacl` | View ACLs                   | `getfacl file.txt`              |
| `setfacl` | Set ACLs                    | `setfacl -m u:user:rw file.txt` |

**Tip:** Remember `SUID`, `SGID`, and `Sticky Bit` for special cases.

---

## 4. Process & Job Management

| Command  | Description                          | Example                  |
| -------- | ------------------------------------ | ------------------------ |
| `ps`     | List processes                       | `ps aux`                 |
| `top`    | Interactive process monitor          | `top`                    |
| `htop`   | Advanced interactive process monitor | `htop`                   |
| `kill`   | Terminate process by PID             | `kill 1234`              |
| `pkill`  | Kill by process name                 | `pkill firefox`          |
| `jobs`   | List background jobs                 | `jobs`                   |
| `bg`     | Resume job in background             | `bg %1`                  |
| `fg`     | Bring job to foreground              | `fg %1`                  |
| `nice`   | Start process with priority          | `nice -n 10 ./script.sh` |
| `renice` | Change priority of running process   | `renice 5 -p 1234`       |
| `uptime` | System uptime and load               | `uptime`                 |
| `vmstat` | CPU, memory, IO info                 | `vmstat 1`               |

---

## 5. Disk & Storage Management

| Command   | Description            | Example                |
| --------- | ---------------------- | ---------------------- |
| `df`      | Disk free space        | `df -h`                |
| `du`      | Disk usage             | `du -sh /var`          |
| `lsblk`   | Block devices          | `lsblk`                |
| `blkid`   | Partition UUIDs        | `blkid`                |
| `mount`   | Mount filesystems      | `mount /dev/sdb1 /mnt` |
| `umount`  | Unmount filesystem     | `umount /mnt`          |
| `fsck`    | Check filesystem       | `fsck /dev/sdb1`       |
| `tune2fs` | Adjust ext filesystems | `tune2fs -l /dev/sdb1` |
| `mkfs`    | Create filesystem      | `mkfs.ext4 /dev/sdb1`  |
| `swapon`  | Enable swap            | `swapon /swapfile`     |
| `swapoff` | Disable swap           | `swapoff /swapfile`    |

**Tip:** Use UUID in `/etc/fstab` for reliable mounts.

---

## 6. Networking Commands

| Command      | Description              | Example                             |
| ------------ | ------------------------ | ----------------------------------- |
| `ping`       | Test connectivity        | `ping google.com`                   |
| `traceroute` | Trace path to host       | `traceroute google.com`             |
| `ifconfig`   | View network interfaces  | `ifconfig`                          |
| `ip addr`    | Show IP addresses        | `ip addr`                           |
| `netstat`    | Show network connections | `netstat -tulnp`                    |
| `ss`         | Socket statistics        | `ss -tulnp`                         |
| `curl`       | Fetch URLs               | `curl -I https://example.com`       |
| `wget`       | Download files           | `wget https://example.com/file.txt` |
| `dig`        | DNS lookup               | `dig example.com`                   |
| `nslookup`   | DNS query                | `nslookup example.com`              |
| `iptables`   | Firewall config          | `iptables -L`                       |
| `ufw`        | Simple firewall          | `ufw status`                        |

---

## 7. Package Management

| Command       | Description           | Example                    |
| ------------- | --------------------- | -------------------------- |
| `apt update`  | Update package list   | `sudo apt update`          |
| `apt upgrade` | Upgrade packages      | `sudo apt upgrade`         |
| `apt install` | Install package       | `sudo apt install git`     |
| `apt remove`  | Remove package        | `sudo apt remove git`      |
| `yum install` | RedHat/Fedora install | `sudo yum install vim`     |
| `dnf install` | Fedora install        | `sudo dnf install vim`     |
| `rpm -i`      | Install RPM package   | `sudo rpm -i package.rpm`  |
| `dpkg -i`     | Install deb package   | `sudo dpkg -i package.deb` |

---

## 8. Bash & Shell Tricks

| Command         | Description              | Example                           |           |
| --------------- | ------------------------ | --------------------------------- | --------- |
| `history`       | Command history          | `history                          | grep git` |
| `!!`            | Repeat last command      | `!!`                              |           |
| `!n`            | Repeat command number n  | `!42`                             |           |
| `Ctrl + r`      | Reverse search           | Press `Ctrl + r` and type command |           |
| `alias`         | Create shortcut          | `alias ll='ls -la'`               |           |
| `export`        | Set environment variable | `export PATH=~/bin:$PATH`         |           |
| `source`        | Reload shell config      | `source ~/.bashrc`                |           |
| Brace expansion | Create multiple files    | `touch file{1..5}.txt`            |           |

---

## 9. System Logs & Monitoring

| Command      | Description            | Example                   |             |
| ------------ | ---------------------- | ------------------------- | ----------- |
| `dmesg`      | Kernel messages        | `dmesg                    | tail -n 20` |
| `tail -f`    | Follow logs            | `tail -f /var/log/syslog` |             |
| `journalctl` | Systemd logs           | `journalctl -xe`          |             |
| `uptime`     | System uptime/load     | `uptime`                  |             |
| `free -h`    | Memory usage           | `free -h`                 |             |
| `vmstat`     | CPU/memory stats       | `vmstat 1`                |             |
| `iostat`     | Disk IO stats          | `iostat -xz 1`            |             |
| `sar`        | System activity report | `sar -u 1 5`              |             |

---

## 10. Security & Permissions

| Command    | Description                 | Example                           |
| ---------- | --------------------------- | --------------------------------- |
| `chmod`    | Change file permissions     | `chmod 600 ~/.ssh/id_rsa`         |
| `chown`    | Change owner                | `chown user:user file.txt`        |
| `ufw`      | Firewall                    | `ufw enable`                      |
| `iptables` | Advanced firewall           | `iptables -L`                     |
| `fail2ban` | Prevent brute-force attacks | `sudo fail2ban-client status`     |
| `sudo`     | Execute command as root     | `sudo apt update`                 |
| `ssh`      | Connect to remote server    | `ssh user@host`                   |
| `scp`      | Copy files over SSH         | `scp file.txt user@host:/tmp/`    |
| `rsync`    | Sync files                  | `rsync -av --progress src/ dest/` |

---

## 11. Miscellaneous Useful Commands

| Command    | Description       | Example                     |
| ---------- | ----------------- | --------------------------- |
| `date`     | Current date/time | `date '+%Y-%m-%d %H:%M:%S'` |
| `cal`      | Calendar          | `cal 2026`                  |
| `uptime`   | System uptime     | `uptime`                    |
| `whoami`   | Current user      | `whoami`                    |
| `uname -a` | System info       | `uname -a`                  |
| `hostname` | System hostname   | `hostname`                  |
| `man`      | Command manual    | `man ls`                    |
| `apropos`  | Search man pages  | `apropos network`           |
| `echo`     | Print text        | `echo $PATH`                |
| `date`     | Show or set date  | `date`                      |

---

*This file is fully editable. Use it as a complete reference guide for all commonly used Linux commands for developers, sysadmins, and power users.*
