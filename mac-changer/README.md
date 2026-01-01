# The Changer Mac address

A minimal set of scripts for changing the MAC address of a network interface on Linux.
⚠️ Important
Before using the tool, check the names of your network interfaces. You can list them with:
`
ifconfig`
or
`ip link`
## run script
`sudo venv/bin/python mac-changer/mac-changer.py -i $S1[your interface] -m $S2[your MAC address]`
where 
 S1 - name your interfase
 S2 - new MAC address for example 02:11:22:33:44:55

for emaple:
`sudo venv/bin/python mac-changer/mac-changer.py -i ens33 -m 02:11:22:33:44:55`
