<h1 align="center">NetX</h1>
<h4 align="center">simple analogue of netcat</h4>

## examples of use

### command shell

tab-1

launch listener
```
python3 netX.py -t <target IP> -p <target port> -l -c
python3 netX.py -t 192.168.1.101 -p 5555 -l -c    
```

tab-2

running a script in client mode
```
python3 netX.py -t 192.168.1.101 -p 5555
ctrl+D
> <your command>
> ls
> whoami
> pwd
```


### execution of a single command

tab-1
```
python3 netX.py -t 192.168.1.101 -p 5555 -l -r="whoami"
```

tab-2
```
python3 netX.py -t 192.168.1.101 -p 5555
ctrl+D
hellcard
>
```

### sending request

tab-1
```
 echo -ne "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n" | python3 ./netX.py -t www.google.com -p 80 
```


<h4 align="center">for more detailed instructions run this script in terminal with [-h] || [--help] flags</h4>

```
python3 netX.py -h
python3 netX.py --help
```
