#!/bin/python3
import random
import sys

print(sys.argv)

# Read port list from file and print random port
port_list = "inconspicuous_ports_list.txt"
with open(port_list) as f:
    print(random.choice(f.read().splitlines()))
