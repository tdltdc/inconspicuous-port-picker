#!/bin/python3
import random
import argparse
import pandas as pd

# Optionally allow user to request a system port or a registered port
parser = argparse.ArgumentParser(
    prog='random-port-picker',
    description='Pick a random inconspicuous port.'
)
parser.add_argument('-s', '--system', action='store_true', help='Pick an incon'
                    'spicuous system port, i.e. a port in the range of 0 to '
                    '1023.')
parser.add_argument('-r', '--registered', action='store_true', help='Pick a '
                    'registered / non-system port, i.e. a port in the range of'
                    ' 1024 to 49151.')
args = parser.parse_args()

# Read port list from file
port_list = "inconspicuous_ports_list.txt"
with open(port_list) as f:
    inconspicuous_ports = f.read().splitlines()
    inconspicuous_ports = pd.DataFrame(pd.to_numeric(inconspicuous_ports),
                                       columns=['port'])

# Parse user arguments (if any) and set pool of available inconspicuous ports
if args.system:
    port_pool = inconspicuous_ports['port'][inconspicuous_ports['port'] < 1024]
elif args.registered:
    port_pool = inconspicuous_ports['port'][inconspicuous_ports['port'] > 1023]
else:
    port_pool = inconspicuous_ports['port']

# Print port
print(random.choice(port_pool))
