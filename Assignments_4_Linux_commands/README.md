# Linux – Complete Guide

## Table of Contents

1. Introduction to Linux
2. History of Linux
3. Linux Features
4. Linux Architecture
5. Linux Distributions
6. Linux Kernel
7. Linux Shells
8. Linux File System
9. Linux File Permissions
10. Linux Commands
11. Package Management
12. Process Management
13. Networking in Linux
14. Scripting in Linux
15. System Administration
16. Security in Linux
17. Linux Tips & Tricks
18. References

---

## Introduction to Linux

* Linux is an **open-source, Unix-like operating system**.
* It is widely used for **servers, desktops, embedded systems, and supercomputers**.
* Linux follows the **POSIX standard** for compatibility.
* Key strengths: **Stability, Security, Flexibility, Multi-user support**.

## History of Linux

* **1991**: Linus Torvalds started Linux as a hobby project.
* **Unix-like**, inspired by MINIX.
* First release: Linux **0.01**.
* Linux kernel is **GPL licensed**.

## Linux Features

* **Open Source**
* **Multiuser**
* **Multitasking**
* **Portability**
* **Security**
* **Networking Support**
* **Shell and scripting support**
* **Hardware independence**

## Linux Architecture

1. **Kernel**: Core part, manages resources.
2. **System Libraries**: Shared code for system calls.
3. **System Utilities**: User commands, daemons.
4. **Shell**: Interface between user and kernel.

## Linux Distributions

* **Debian**: Stability-focused.
* **Ubuntu**: User-friendly.
* **Red Hat / CentOS / Fedora**: Enterprise.
* **Arch Linux**: Rolling release, DIY.
* **SUSE**: Enterprise-focused.

## Linux Kernel

* Monolithic kernel.
* Manages **processes, memory, devices, file systems**.
* Versions updated regularly.
* Kernel modules: Loadable and unloadable dynamically.

## Linux Shells

* **Bash**: Most common.
* **Zsh**: Advanced scripting, auto-completion.
* **Ksh**: Korn shell.
* **Fish**: Friendly interactive shell.

## Linux File System

* **Hierarchy**: `/`, `/home`, `/bin`, `/usr`, `/var`, `/tmp`
* **File types**: Regular, Directory, Symbolic Link, Device files.
* **Commands**: `ls`, `cd`, `pwd`, `mkdir`, `rmdir`, `touch`, `cp`, `mv`, `rm`

## Linux File Permissions

* **Read (r), Write (w), Execute (x)**
* **Users**: Owner, Group, Others
* **Commands**: `chmod`, `chown`, `chgrp`
* Example: `chmod 755 file.txt`

## Linux Commands

* **Navigation**: `ls`, `cd`, `pwd`
* **File Operations**: `cp`, `mv`, `rm`, `touch`
* **Text Processing**: `cat`, `grep`, `awk`, `sed`
* **System Info**: `top`, `ps`, `df`, `du`, `free`
* **Networking**: `ping`, `ifconfig`, `netstat`, `ss`

## Package Management

* **Debian/Ubuntu**: `apt`, `dpkg`
* **RedHat/Fedora**: `yum`, `dnf`, `rpm`
* **Arch Linux**: `pacman`
* Examples: `sudo apt update`, `sudo yum install httpd`

## Process Management

* **Commands**: `ps`, `top`, `htop`, `kill`, `jobs`, `fg`, `bg`
* **Signals**: `SIGKILL`, `SIGTERM`, `SIGHUP`
* **Process States**: Running, Sleeping, Stopped, Zombie

## Networking in Linux

* **Configuration**: `/etc/network/interfaces`, `ifconfig`, `ip`
* **Testing**: `ping`, `traceroute`, `netstat`, `ss`
* **Firewall**: `iptables`, `ufw`

## Scripting in Linux

* Shell scripting: `.sh` files
* Variables, loops, conditions
* Example:

```bash
#!/bin/bash
for i in {1..5}; do
  echo "Iteration $i"
done
```

* Cron jobs for scheduling: `crontab -e`

## System Administration

* **User Management**: `adduser`, `usermod`, `passwd`
* **Disk Management**: `df`, `du`, `mount`, `umount`
* **Logs**: `/var/log/syslog`, `/var/log/messages`
* **Backup**: `tar`, `rsync`

## Security in Linux

* **File Permissions and Ownership**
* **SELinux / AppArmor**
* **SSH Key Authentication**
* **Firewall Configuration**
* **Package Updates**: Regular security updates

## Linux Tips & Tricks

* Tab completion in terminal.
* History navigation: `history`, `!!`, `!n`
* Aliases: `alias ll='ls -la'`
* Combining commands: `&&`, `||`, `;`

## References

* [Linux Kernel Archives](https://www.kernel.org/)
* [The Linux Documentation Project](https://www.tldp.org/)
* [Ubuntu Official Docs](https://help.ubuntu.com/)
* [RedHat Docs](https://access.redhat.com/documentation/en-us/)

---

*This README is fully editable and can be expanded to include more commands, scripts, and advanced topics like containers, virtualization, systemd, SELinux, and networking tools.*
