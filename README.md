# Why?
When exposing a service to the public internet, it can be useful to expose it
on a non-default port (for example, to reduce log spam from malicious SSH login
attempts).

The non-default port should preferably be inconspicuous to avoid falsely
signalling that something interesting may running on your server.

Naively picking a random valid port number therefore is not a good idea, as you
might (unknowingly) pick a port number that invites malicious traffic (for
example,
[port 445 may suggest a Samba server](https://www.shodan.io/search?query=samba)
is running on your machine).

To pick an inconspicous port, we want to exclude any port to is known to be
used. The IANA maintains the [Service Name and Transport Protocol Port Number
Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt),
which is a list of ports officially assigned by them to specific services[^1].
Of course, assignment of a port by the IANA only approximates how
"inconspicuous" a port is in the real world, but for most ports, the
approximation is close enough to give the list as a whole a good degree of
utility. Furthermore, it's a well-maintained, machine-readable source that
can be expected to stay around for the foreseeable future.

# What?
[This script](inconspicuous-ports-extractor.py) can be used to download the
IANA port registry, filter out "conspicuous" ports and dump the resulting list
of inconspicuous ports to disk.

The list of inconspicuous ports (i.e. the script's output) can be found in
[inconspicuous_ports_list.txt](inconspicuous_ports_list.txt).

A trivial script that picks a random port from the inconspicuous ports list is
included as a bonus.

# Prerequisites
[`pandas`](https://pandas.pydata.org/) and [`numpy`](https://numpy.org/).

[^1]: The registry also has an "Unauthorized Use Reported" column which the
script uses to filter out ports that are not unassigned but are known to be in
use.
