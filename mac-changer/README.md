# The Changer Mac address

A minimal set of scripts for changing the MAC address of a network interface on Linux.
⚠️ Important
Before using the tool, check the names of your network interfaces. You can list them with:
`
ifconfig`
or
`ip link`
## run script
`sudo python3 mac-changer.py -i $S1 -m $S2`
where 
 S1 - name your interfase
 S2 - new MAC address for example 02:11:22:33:44:55

for emaple:
`sudo python3 mac-changer.py -i ens33 -m 02:11:22:33:44:55`
