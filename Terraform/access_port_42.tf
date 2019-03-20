resource "junos-qfx_vlan-access-port" "ge42" {
        resource_name = "customerXYdev1port42"
        port_name = "ge-0/0/42"
        port_desc = "Customer mapped to VLAN ${junos-qfx_vlan.vlan42xyz.vlan_num}"
   	port_vlan = "${junos-qfx_vlan.vlan42xyz.vlan_name}"
}
