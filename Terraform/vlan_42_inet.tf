resource "junos-qfx_inet-iface" "vlan42" {
        resource_name = "customerXYvlaninetiface42"
        iface_name = "vlan"
        iface_inet_address = "10.10.42.1/24"
        iface_unit = "${junos-qfx_vlan.vlan42xyz.vlan_num}"
        iface_desc = "L3 iface for vlan ${junos-qfx_vlan.vlan42xyz.vlan_num}" 
}
