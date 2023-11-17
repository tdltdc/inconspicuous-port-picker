#!/bin/python3
import random

# Read port list from file and print random port
port_list = "iana_unassigned_ports_list.txt"
with open(port_list) as f:
    print(random.choice(f.read().splitlines()))
