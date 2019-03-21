from myTables.ConfigTables import AccessInterfaceTable, VLANTable, InterfaceTable
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
import sys


dev = Device(host="demo01", user="tf", passwd="Passw0rd").open()

l3 = InterfaceTable(dev) 

l3.name = "irb"
l3.unit_name = "42"
l3.ip_address = "10.10.42.1/24"
l3.append()
l3.load()
l3.pdiff()
l3.commit_check()
l3.commit()

vlan = VLANTable(dev)
vlan.name = "DT"
vlan.description = "For DT"
vlan.vlan_id = "42"
vlan.l3iface = "irb.42"
vlan.append()
vlan.load()
vlan.pdiff()
vlan.commit_check()
vlan.commit()

phy = AccessInterfaceTable(dev) 
phy.name = "ge-0/0/42"
phy.unit_name = 0
phy.mode = "access"
phy.vlan = ["DT"]
phy.append()
phy.load()
phy.pdiff()
phy.commit_check()
phy.commit()


dev.close()