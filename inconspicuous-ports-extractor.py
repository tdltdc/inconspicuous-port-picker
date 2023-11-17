#!/usr/bin/python3
import pandas as pd
import numpy


def explode_range(port_range):
    begin, end = port_range.split('-')
    return list(range(int(begin), int(end)+1))


# Define IANA Service Name and Transport Protocol Numbery Registry URL
url = ('https://www.iana.org/assignments/service-names-port-numbers/'
       'service-names-port-numbers.csv')

# Grab the current copy of the port registry
portreg = pd.read_csv(url)

# Select only unassigned ports / port ranges
portreg = portreg[portreg['Description'] == 'Unassigned']

# Filter out ports with known unauthorized use
portreg = portreg[portreg['Unauthorized Use Reported'].isna()]

# Grab single port numbers
single_ports_filter = portreg['Port Number'].str.match(r'^\d+$')
single_ports = pd.to_numeric(portreg['Port Number'][single_ports_filter])

# Grab and explode port ranges
range_filter = portreg['Port Number'].str.match(r'^\d+-\d+$')
temporary_df = portreg['Port Number'][range_filter].apply(explode_range)
ports_from_ranges = numpy.concatenate(temporary_df.to_numpy())

# Concatenate all ports into single array
merged_ports = list(single_ports.to_numpy()) + list(ports_from_ranges)

# Deduplicate ports
ports = list(set(merged_ports))

# Write list of ports to file
with open('inconspicuous_ports_list.txt', 'w') as fp:
    fp.write('\n'.join(str(port) for port in ports))
