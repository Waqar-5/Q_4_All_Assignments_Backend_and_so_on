# Linux Core Commands Cheat Sheet for Developers

**Goal:** Memorize and practice the commands that every developer **must know** to work efficiently on Linux.

---

## 1. File & Directory Management

| Command  | Purpose                  | Example                                      | Notes / Memory Tip                    |
| -------- | ------------------------ | -------------------------------------------- | ------------------------------------- |
| `ls`     | List files & directories | `ls -lah`                                    | `l`=long, `a`=all, `h`=human-readable |
| `cd`     | Change directory         | `cd /var/log`                                | Always track current dir with `pwd`   |
| `pwd`    | Print current directory  | `pwd`                                        | “Where am I?”                         |
| `mkdir`  | Create directory         | `mkdir project`                              | Create project folders                |
| `rmdir`  | Remove empty directory   | `rmdir old_folder`                           | Only works on empty dirs              |
| `rm`     | Remove files/folders     | `rm file.txt`<br>`rm -r folder/`             | `-r` = recursive                      |
| `cp`     | Copy files/folders       | `cp file1.txt file2.txt`<br>`cp -r src dest` | Core for backups & duplicates         |
| `mv`     | Move/rename files        | `mv old.txt new.txt`<br>`mv file.txt /tmp/`  | Move or rename quickly                |
| `touch`  | Create empty file        | `touch newfile.txt`                          | Quick placeholder files               |
| `find`   | Search files             | `find /home -name '*.log'`                   | Search recursively                    |
| `locate` | Fast search              | `locate file.txt`                            | Uses database, update with `updatedb` |
| `tree`   | Show directory tree      | `tree /home/user`                            | Visualize folder structure            |

---

## 2. File Viewing & Manipulation

| Command | Purpose                   | Example                      | Notes / Memory Tip                  |
| ------- | ------------------------- | ---------------------------- | ----------------------------------- |
| `cat`   | Display file content      | `cat file.txt`               | Quick view                          |
| `less`  | Page-by-page view         | `less file.txt`              | Scroll with `j/k`                   |
| `head`  | Show first lines          | `head -n 10 file.txt`        | Preview start                       |
| `tail`  | Show last lines           | `tail -n 10 file.txt`        | Preview end, use `-f` for live logs |
| `grep`  | Search text               | `grep 'error' file.log`      | Powerful search with regex          |
| `awk`   | Text processing           | `awk '{print $1}' file.txt`  | Extract columns easily              |
| `sed`   | Stream editor             | `sed 's/old/new/g' file.txt` | Find & replace efficiently          |
| `cut`   | Extract fields            | `cut -d',' -f1 file.csv`     | Works with delimiters               |
| `wc`    | Count lines, words, chars | `wc -l file.txt`             | Quick stats                         |
| `diff`  | Compare files             | `diff file1.txt file2.txt`   | Show differences                    |

---

## 3. File Permissions & Ownership

| Command | Purpose            | Example                     | Notes / Memory Tip             |
| ------- | ------------------ | --------------------------- | ------------------------------ |
| `chmod` | Change permissions | `chmod 755 file.txt`        | 7=rwx, 5=r-x, 5=r-x            |
| `chown` | Change owner       | `chown user:group file.txt` | Ownership management           |
| `chgrp` | Change group       | `chgrp developers file.txt` | Useful for team projects       |
| `ls -l` | View permissions   | `ls -l file.txt`            | Check rwx bits                 |
| `stat`  | File details       | `stat file.txt`             | Shows permissions, size, dates |

---

## 4. Process & Job Management

| Command  | Purpose                         | Example                  | Notes / Memory Tip                    |
| -------- | ------------------------------- | ------------------------ | ------------------------------------- |
| `ps`     | List processes                  | `ps aux`                 | Monitor all running processes         |
| `top`    | Interactive monitor             | `top`                    | Real-time CPU/mem usage               |
| `htop`   | Advanced monitor                | `htop`                   | Better visual, use arrows, F9 to kill |
| `kill`   | Terminate process               | `kill 1234`              | Use PID from `ps`                     |
| `pkill`  | Kill by name                    | `pkill firefox`          | Convenient if PID unknown             |
| `jobs`   | Background jobs                 | `jobs`                   | List suspended jobs                   |
| `bg`     | Resume job background           | `bg %1`                  | Resume %1 job                         |
| `fg`     | Resume job foreground           | `fg %1`                  | Bring back to terminal                |
| `nice`   | Start process with priority     | `nice -n 10 ./script.sh` | Lower value = higher priority         |
| `renice` | Change running process priority | `renice 5 -p 1234`       | Adjust on-the-fly                     |
| `uptime` | System uptime & load            | `uptime`                 | Quick load check                      |

---

## 5. Networking Essentials

| Command      | Purpose            | Example                             | Notes / Memory Tip              |
| ------------ | ------------------ | ----------------------------------- | ------------------------------- |
| `ping`       | Test connectivity  | `ping google.com`                   | Stop with Ctrl+C                |
| `traceroute` | Trace path         | `traceroute google.com`             | Shows hops                      |
| `ifconfig`   | Network interfaces | `ifconfig`                          | Older, but still used           |
| `ip addr`    | Show IP addresses  | `ip addr`                           | Modern replacement for ifconfig |
| `netstat`    | Network stats      | `netstat -tulnp`                    | Show listening ports            |
| `ss`         | Socket stats       | `ss -tulnp`                         | Modern alternative to netstat   |
| `curl`       | Fetch URLs         | `curl -I https://example.com`       | Test endpoints                  |
| `wget`       | Download files     | `wget https://example.com/file.txt` | Quick file download             |
| `ssh`        | Remote login       | `ssh user@host`                     | Secure remote access            |
| `scp`        | Copy over SSH      | `scp file.txt user@host:/tmp/`      | Secure file transfer            |
| `rsync`      | Sync files         | `rsync -av --progress src/ dest/`   | Efficient backups               |

---

## 6. Package Management (Ubuntu/Debian)

| Command       | Purpose             | Example                    | Notes / Memory Tip        |
| ------------- | ------------------- | -------------------------- | ------------------------- |
| `apt update`  | Update package list | `sudo apt update`          | Always run before install |
| `apt upgrade` | Upgrade packages    | `sudo apt upgrade`         | Keep system updated       |
| `apt install` | Install package     | `sudo apt install git`     | Must-know dev packages    |
| `apt remove`  | Remove package      | `sudo apt remove git`      | Cleanup unused software   |
| `dpkg -i`     | Install .deb        | `sudo dpkg -i package.deb` | Manual install            |

---

## 7. Bash & Shell Productivity

| Command         | Purpose             | Example                    | Notes / Memory Tip            |                    |
| --------------- | ------------------- | -------------------------- | ----------------------------- | ------------------ |
| `history`       | Command history     | `history                   | grep git`                     | Find past commands |
| `!!`            | Repeat last command | `!!`                       | Quick rerun                   |                    |
| `!n`            | Repeat command n    | `!42`                      | Recall any command            |                    |
| `Ctrl+r`        | Reverse search      | Press Ctrl+r, type command | Fast recall                   |                    |
| `alias`         | Command shortcut    | `alias ll='ls -la'`        | Save typing                   |                    |
| `export`        | Set env variable    | `export PATH=~/bin:$PATH`  | Temporary PATH changes        |                    |
| `source`        | Reload config       | `source ~/.bashrc`         | Apply changes without restart |                    |
| Brace expansion | Multiple files      | `touch file{1..5}.txt`     | Quick file creation           |                    |

---

## 8. System Logs & Monitoring

| Command      | Purpose         | Example                   | Notes / Memory Tip          |                                |
| ------------ | --------------- | ------------------------- | --------------------------- | ------------------------------ |
| `dmesg`      | Kernel messages | `dmesg                    | tail -n 20`                 | Troubleshoot hardware/software |
| `tail -f`    | Live log view   | `tail -f /var/log/syslog` | Monitor logs in real-time   |                                |
| `journalctl` | Systemd logs    | `journalctl -xe`          | Debug system services       |                                |
| `free -h`    | Memory usage    | `free -h`                 | Human-readable format       |                                |
| `vmstat`     | CPU/mem stats   | `vmstat 1`                | Refresh every second        |                                |
| `iostat`     | Disk IO stats   | `iostat -xz 1`            | Monitor storage performance |                                |

---

*This cheat sheet is **fully editable**, meant to help you **practice and memorize core Linux commands** efficiently. Focus on **daily usage command
