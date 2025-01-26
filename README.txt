 ##   ##  #######  ######            ##  ##
 ###  ##   ##   #  # ## #            ##  ##
 #### ##   ## #      ##               ####
 ## ####   ####      ##                ##
 ##  ###   ## #      ##               ####
 ##   ##   ##   #    ##              ##  ##
 ##   ##  #######   ####             ##  ##

___________________________________________
                   ABOUT
___________________________________________
Description: simple analogue of netcat
Program: NetX | analogue of netcat
Language: Python 3.12.7
Tested on: Linux 6.11.2
Author: ghostface-cybersecurity

___________________________________________
               PROGRAM LAUNCH
___________________________________________
              EXAMPLES OF USE
___________________________________________
             #1 COMMAND SHELL
___________________________________________
// Launch listener 
// Example: python3 netX.py -t <IP> -p <PORT> -l -c
python3 netX.py -t 192.168.1.101 -p 5555 -l -c

// Running a script in client mode
// Example: python3 netX.py -t <listener IP> -p <listener PORT>
python3 netX.py -t 192.168.1.101 -p 5555
ctrl+D
> <any your command>
> ls
> whoami
> pwd
> <etc...>

__________________________________________
    #2 EXECUTION OF A SINGLE COMMAND
__________________________________________
// Lauch server (listener)
// Example: python3 netX.py -t <IP> -p <PORT> -l -r="<your command>"
python3 netX.py -t 192.168.1.101 -p 5555 -l -r="whoami"

// Lauch client 
// Example: python3 netX.py -t <server IP> -p <server PORT>
python3 netX.py -t 192.168.1.101 -p 5555
ctrl+D
ghostface
>
________________________________________
           #3 SENDING REQUEST
________________________________________
echo -ne "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n" | python3 ./netX.py -t www.google.com -p 80

________________________________________
     FOR MORE DETAILED INSTRUCTIONS
________________________________________
python3 netX.py -h
python3 netX.py --help

________________________________________
            LEGAL STATEMENT
________________________________________
By downloading, modifying, redistributing, and/or executing NetX, the
user agrees to the contained LEGAL.txt statement found in this repository.

I, ghostface-cybersecurity, the creator, take no legal responsibility for unlawful actions
caused/stemming from this program. 

Use responsibly and ethically!
