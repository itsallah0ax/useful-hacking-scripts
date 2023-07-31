#!/usr/bin/env python3

# This script parses out port numbers from nmap or rustscan port-scan results and prints them to stdout in the following format: x,x,x,x,x,x,x

import sys

# Parses out port numbers from rustscan scan results
def parse_rustscan_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

# Parses out all info before the colons
    port_num1 = [line.split(':')[-1].strip() for line in lines]
    print(",".join(port_num1))

# Parses out port numbers from nmap scan results
def parse_nmap_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

# Parses out all info after the forward slash
    port_num2 = [line.split('/')[0].strip() for line in lines]
    print(",".join(port_num2))

# Main construct block 
if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] != '--type':
        print("Usage: python script.py --type 'nmap/rustscan' input_file")
        sys.exit(1)

    input_type = sys.argv[2]
    input_file = sys.argv[3]

    if input_type == 'nmap':
        parse_nmap_input(input_file)
    elif input_type == 'rustscan':
        parse_rustscan_input(input_file)
    else:
        print("Invalid input type. Use either 'nmap' or 'rustscan'.")
        sys.exit(1)