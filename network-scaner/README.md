# Network Scaner 

A minimal Python-based tool for scanning devices in your local network on Linux using ARP.
⚠️ Important
Before using this tool, make sure you know the IP range of your local network.
`rourte -n` or `ip route`

## How to run
`sudo venv/bin/python network-scaner/network-scaner.py -t <IP_RANGE>`

for emaple:
`sudo venv/bin/python network-scaner/network-scaner.py -t "192.168.192.1/24"`