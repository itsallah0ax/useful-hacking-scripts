#Fun lil thing I made, give me a follow: itsallah0ax :)
#!/usr/bin/env python3
import argparse
import re

# Create the argument parser
parser = argparse.ArgumentParser(description='Hex to human-readable converter')
parser.add_argument('-i', '--input', type=str, help='Input file containing the hex string')

# Parse the command-line arguments
args = parser.parse_args()

# Read the hex string from the input file
with open(args.input, 'r') as file:
    hex_string = file.read().strip()

# Convert hex string to bytes and remove non-printable ASCII characters
decoded_string = bytes.fromhex(hex_string).decode('latin')
decoded_string = re.sub(r'[^\x20-\x7E]', '', decoded_string)

print(decoded_string)