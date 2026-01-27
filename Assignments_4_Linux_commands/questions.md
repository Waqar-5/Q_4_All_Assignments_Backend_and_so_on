# Linux – 60 Detailed Questions with Answers and Memory Tricks

## Introduction

This README contains **60 detailed Linux questions** with answers and **memory tricks** to help you remember them for exams and interviews. Each topic is explained clearly for quick understanding.

---

## Questions and Answers

1. **Who created Linux?**

   * **Answer:** Linus Torvalds
   * **Trick:** Remember "Linux by Linus" (alliteration helps).

2. **Which license does Linux use?**

   * **Answer:** GPL (GNU General Public License)
   * **Trick:** GPL allows everyone to “G”et source and “P”lay with it.

3. **Default shell in most Linux distributions?**

   * **Answer:** Bash
   * **Trick:** Bash = Bourne Again SHell, think “Again” for default.

4. **Command to list all files including hidden files?**

   * **Answer:** `ls -a`
   * **Trick:** “a” for all, including hidden ones.

5. **Command to set read/write/execute for owner and read/execute for group/others?**

   * **Answer:** `chmod 755 file.txt`
   * **Trick:** 7 = rwx, 5 = r-x; remember octal code 755.

6. **Command to show current directory?**

   * **Answer:** `pwd`
   * **Trick:** "Print Working Directory" literally prints where you are.

7. **Commands to view running processes?**

   * **Answer:** `ps`, `top`
   * **Trick:** PS = Process Status, Top = real-time top list.

8. **Directory for user home directories?**

   * **Answer:** `/home`
   * **Trick:** Think of `/home` as “home for users”.

9. **Command to show mounted filesystems and space?**

   * **Answer:** `df`
   * **Trick:** Disk Free = df.

10. **Commands to find files?**

    * **Answer:** `find`, `locate`
    * **Trick:** Find = search manually, Locate = search fast with DB.

11. **Command to display first 10 lines of a file?**

    * **Answer:** `head`
    * **Trick:** Head = start of the file.

12. **Command to compare two files?**

    * **Answer:** `diff`, `cmp`, `comm`
    * **Trick:** Diff = differences; cmp = compare bytes.

13. **Command to display last 10 lines of a file?**

    * **Answer:** `tail`
    * **Trick:** Tail = end of the file.

14. **Command to search text in files?**

    * **Answer:** `grep`
    * **Trick:** Global Regular Expression Print.

15. **Main network configuration file?**

    * **Answer:** `/etc/network/interfaces`
    * **Trick:** Think network interface configuration.

16. **Command to show memory usage?**

    * **Answer:** `free`
    * **Trick:** Free memory available = free command.

17. **Command to execute commands as root?**

    * **Answer:** `sudo`
    * **Trick:** Super User DO.

18. **Command to change file ownership?**

    * **Answer:** `chown`
    * **Trick:** Change OWNership = chown.

19. **Non-Linux OS?**

    * **Answer:** Windows 10
    * **Trick:** Only Linux distributions = Ubuntu, Fedora, Arch.

20. **File storing user account info?**

    * **Answer:** `/etc/passwd`
    * **Trick:** PASSword info is stored here (not actual passwords).

21. **Command to display groups of a user?**

    * **Answer:** `groups`
    * **Trick:** Groups command directly shows user’s groups.

22. **Command to add new user?**

    * **Answer:** `adduser` or `useradd`
    * **Trick:** Add USER = adduser.

23. **Directory for system configuration files?**

    * **Answer:** `/etc`
    * **Trick:** ETC = Editable Text Configs.

24. **Command to list all processes with full details?**

    * **Answer:** `ps -ef`
    * **Trick:** EF = Everything Full.

25. **Command to kill process by PID?**

    * **Answer:** `kill <pid>`
    * **Trick:** Kill the process ID.

26. **Commands to download files?**

    * **Answer:** `wget`, `curl`
    * **Trick:** WGet = Web Get; Curl = transfer URL.

27. **View file content page by page?**

    * **Answer:** `less`
    * **Trick:** Less allows scrolling instead of dumping content.

28. **Command to show last reboot time?**

    * **Answer:** `last reboot`
    * **Trick:** Remember “last” command logs system events.

29. **Check open ports?**

    * **Answer:** `netstat`, `ss`, `lsof`
    * **Trick:** Network utilities = netstat or ss; lsof shows open files (ports included).

30. **Schedule tasks?**

    * **Answer:** `cron`, `at`, `batch`
    * **Trick:** Cron = recurring, at = one-time.

31. **Command to create symbolic link?**

    * **Answer:** `ln -s`
    * **Trick:** s = symbolic.

32. **Commands to show logged-in users?**

    * **Answer:** `who`, `w`, `users`
    * **Trick:** Who = current users, W = detailed.

33. **Command to show hostname?**

    * **Answer:** `hostname` or `cat /etc/hostname`
    * **Trick:** Host name = hostname.

34. **Command for disk usage of directories?**

    * **Answer:** `du`
    * **Trick:** Disk Usage = du.

35. **Encrypted password file?**

    * **Answer:** `/etc/shadow`
    * **Trick:** Shadow = hidden encrypted info.

36. **Change user password?**

    * **Answer:** `passwd`
    * **Trick:** Remember PASSWORD = passwd.

37. **Show CPU info?**

    * **Answer:** `lscpu` or `cat /proc/cpuinfo`
    * **Trick:** List CPU = lscpu.

38. **Display mounted filesystems?**

    * **Answer:** `mount` or `df`
    * **Trick:** Mount = actual mount points.

39. **Copy files?**

    * **Answer:** `cp`
    * **Trick:** CP = copy.

40. **Move/rename files?**

    * **Answer:** `mv`
    * **Trick:** Move = mv.

41. **Check kernel version?**

    * **Answer:** `uname -r`
    * **Trick:** Kernel Release = -r.

42. **Extract .tar.gz files?**

    * **Answer:** `tar -zxvf`
    * **Trick:** z = gzip, x = extract, v = verbose, f = file.

43. **Search command history?**

    * **Answer:** `history` or Ctrl + r
    * **Trick:** Ctrl + r = reverse search.

44. **Change group ownership?**

    * **Answer:** `chgrp`
    * **Trick:** Change GRouP = chgrp.

45. **Check filesystem type?**

    * **Answer:** `df -T`
    * **Trick:** T = Type.

46. **Display environment variables?**

    * **Answer:** `env`, `printenv`, `set`
    * **Trick:** All show ENV.

47. **Users currently logged in with details?**

    * **Answer:** `w`
    * **Trick:** W = Who + What they are doing.

48. **Find path of executable?**

    * **Answer:** `which`, `whereis`
    * **Trick:** Which one? = which.

49. **Monitor real-time logs?**

    * **Answer:** `tail -f /var/log/syslog`, `journalctl -f`
    * **Trick:** Tail follow = -f.

50. **Compress with gzip?**

    * **Answer:** `gzip`
    * **Trick:** GZip = G compress.

51. **Network interfaces & IP?**

    * **Answer:** `ifconfig` or `ip addr`
    * **Trick:** IP Address = ip addr.

52. **Display routing table?**

    * **Answer:** `route` or `ip route`
    * **Trick:** Routes = route.

53. **Reboot system immediately?**

    * **Answer:** `reboot`, `shutdown -r now`, `init 6`
    * **Trick:** Reboot = restart.

54. **System uptime?**

    * **Answer:** `uptime`
    * **Trick:** Uptime = how long the system is up.

55. **Check free memory?**

    * **Answer:** `free -h`, `vmstat`, `top`
    * **Trick:** Free memory = free.

56. **Install package in Ubuntu?**

    * **Answer:** `apt install <package>`
    * **Trick:** APT = Advanced Package Tool.

57. **Update package list in Ubuntu?**

    * **Answer:** `apt update`
    * **Trick:** Update = refresh package DB.

58. **Remove package in Ubuntu?**

    * **Answer:** `apt remove <package>`
    * **Trick:** Remove = delete package.

59. **Display inode info?**

    * **Answer:** `ls -i`, `stat`, `df -i`
    * **Trick:** Inode = file index.

60. **Display disk partitions?**

    * **Answer:** `fdisk -l`, `lsblk`, `blkid`
    * **Trick:** fdisk list = partitions

---

*This file is fully editable. Use the tricks to memorize commands quickly for interviews and exams.*
