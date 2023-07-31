# useful-hacking-scripts

## Hex To Human Readable Text Script

The __hex-to-text.py__ file is a simple python script that takes hex input from a specified file using the '-i' arg, and then outputs the human-readable version to STDOUT on your CLI.

Usage: 
```
python3 hex-to-text.py -i <file_you_want_to_convert>
```

## Nmap result parsing for easy copy/paste

The __port-parser.py__ file is a simple python script that takes text input from a specified input file and returns the port numbers from the input file in the following format: x,x,x,x,x . Simply copy the scan results from either a rustscan or nmap port-scan to a text file, specify the port scanner you used, specify the input file, and then run the script.

Usage:

```
python3 port-parser.py --type 'nmap/rustscan' <file_to_parse>
```

Full Example:

```
Copying scan results:

h0ax@h0ax:~$ sudo nmap --top-ports=20 domaincontroller.dc
[sudo] password for campbell: 
Starting Nmap 7.80 ( https://nmap.org ) at 2023-07-31 18:52 EDT
Nmap scan report for timelapse.htb (10.10.11.152)
Host is up (0.034s latency).

PORT     STATE    SERVICE
21/tcp   filtered ftp
22/tcp   filtered ssh
23/tcp   filtered telnet
25/tcp   filtered smtp
53/tcp   open     domain
80/tcp   filtered http
110/tcp  filtered pop3
111/tcp  filtered rpcbind
135/tcp  open     msrpc
139/tcp  open     netbios-ssn
143/tcp  filtered imap
443/tcp  filtered https
445/tcp  open     microsoft-ds
993/tcp  filtered imaps
995/tcp  filtered pop3s
1723/tcp filtered pptp
3306/tcp filtered mysql
3389/tcp filtered ms-wbt-server
5900/tcp filtered vnc
8080/tcp filtered http-proxy

Nmap done: 1 IP address (1 host up) scanned in 1.66 seconds

*** Copy everything from 21 to http-proxy to a text file (What you copy will be different for you) ***


Run the following since it is an nmap scan:

h0ax@h0ax:~$ python3 port-parser.py --type nmap nmap-output-to-parse.txt
21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080


** What it looks like for rustscan: **

h0ax@h0ax:~$ rustscan -a 10.10.11.152 -b 500 -t 500
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: http://discord.skerritt.blog           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
0day was here ♥

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 924'.
Open 10.10.11.152:53
Open 10.10.11.152:88
Open 10.10.11.152:135
Open 10.10.11.152:139
Open 10.10.11.152:389
Open 10.10.11.152:445
Open 10.10.11.152:464
Open 10.10.11.152:593
Open 10.10.11.152:636
Open 10.10.11.152:5986
Open 10.10.11.152:9389
Open 10.10.11.152:49673
Open 10.10.11.152:49667
Open 10.10.11.152:49674
Open 10.10.11.152:49696
Open 10.10.11.152:61782

** Copy everything from the first 'Open' to the last port number (in this case 61782) **

Rustscan command:

h0ax@h0ax:~$ python3 port-parser.py --type rustscan rustscan-to-parse.txt 
53,88,135,139,389,445,464,593,636,5986,9389,49667,49673,49674,49696,61782

```

Now you can easily copy the ports from the scan results to be used in other tools!