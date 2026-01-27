# Advanced Linux Insights for Developers

This README contains lesser-known Linux tips, tricks, and points every developer should know to master Linux beyond basics. Fully editable for personal notes.

---

## 1. Hidden Files and Directories

* Linux configuration often resides in hidden files (`.` prefix) like `~/.bashrc`, `~/.vimrc`, `~/.gitconfig`.
* **Tip:** Use `ls -A` to see all except `.` and `..`—reveals developer-critical configs.

## 2. File Permissions and Special Bits

* **SUID** (`chmod 4755`): Run a program as file owner (often root).
* **SGID** (`chmod 2755`): New files inherit the directory's group.
* **Sticky Bit** (`chmod 1777`): Only file owner can delete files in shared directories (e.g., `/tmp`).
* **Tip:** Check permissions with `ls -l` and spot `s` or `t`.

## 3. Process Management Tricks

* `ps aux --sort=-%mem | head`: Top memory-consuming processes.
* `top` & `htop`: Interactive process monitoring.
* `nice` and `renice`: Adjust process priority.
* **Tip:** Combine `ps` with `grep` to filter specific processes.

## 4. File System Insights

* `inotifywait -m <directory>`: Monitor real-time file system changes.
* `df -hT`: Check filesystem type and free space.
* `du -sh *`: Summarize directory sizes.
* **Tip:** Use `lsattr` to see file attributes (immutable, append-only).

## 5. Networking Tips for Developers

* `ss -tulnp` or `netstat -tulnp`: Check listening ports.
* `ping -c 5 google.com`: Quick connectivity test.
* `traceroute <host>`: Trace path to a host.
* **Tip:** `curl -I <url>` for quick HTTP headers inspection.

## 6. Package Management Best Practices

* Ubuntu/Debian: `apt update && apt upgrade` to keep packages fresh.
* RedHat/Fedora: `yum update` or `dnf update`.
* **Tip:** Use `--simulate` option (`apt-get -s install <package>`) to preview changes.

## 7. Bash & Shell Tricks

* `history | grep <command>`: Search previous commands.
* `!!` repeats last command, `!n` repeats command number n.
* Brace expansion: `touch file{1..5}.txt` creates multiple files.
* **Tip:** Use `Ctrl + r` for reverse search in terminal.

## 8. Environment Variables and Config

* `printenv` or `env`: List environment variables.
* `export VAR=value`: Set temporary environment variable.
* Persist variables in `~/.bashrc` or `~/.zshrc`.
* **Tip:** Prepend PATH to prioritize custom binaries: `export PATH=~/bin:$PATH`.

## 9. Disk & Storage Tricks

* `lsblk -f`: Check disk partitions and filesystem types.
* `blkid`: Shows UUIDs of disks, useful for fstab.
* `mount -o loop file.iso /mnt`: Mount ISO images.
* **Tip:** Always use UUID in `/etc/fstab` to avoid mount failures on reboot.

## 10. Logs & Debugging

* `/var/log/syslog` or `/var/log/messages`: General logs.
* `journalctl -xe`: Systemd logs with error details.
* `dmesg | tail -n 20`: Kernel messages for recent events.
* **Tip:** `tail -f` for live monitoring during development/testing.

## 11. Hidden Developer Commands

* `strace <command>`: Trace system calls of a program.
* `lsof -i :<port>`: Check process using a network port.
* `watch -n 1 <command>`: Run a command repeatedly every second.
* **Tip:** Great for debugging performance and network issues.

## 12. Security Practices

* `chmod 600 ~/.ssh/id_rsa`: Protect SSH private keys.
* `fail2ban`: Prevent brute-force login attempts.
* `ufw` or `iptables`: Firewall configuration.
* **Tip:** Always run security updates automatically: `apt install unattended-upgrades`.

## 13. Scripting Tips

* Use `set -e` in bash scripts to exit on errors.
* Use functions to modularize scripts.
* `trap 'commands' EXIT`: Cleanup on script exit.
* **Tip:** Comment scripts generously; makes debugging easier.

## 14. Performance & Monitoring

* `vmstat 1`: Memory, CPU, swap usage every 1 second.
* `iostat -xz 1`: Disk performance monitoring.
* `sar -u 1 5`: CPU usage history.
* **Tip:** Combine tools to identify bottlenecks efficiently.

## 15. Hidden Filesystem Features

* `tmpfs`: Temporary filesystem in memory for faster read/write.
* `chattr +i <file>`: Make file immutable.
* `rsync -av --progress`: Efficient file sync with progress.
* **Tip:** Use tmpfs for temporary builds or cache to boost performance.

---

*Keep this README.md editable. Use these hidden tricks and commands to excel in Linux, improve productivity, debugging, and system management.*
