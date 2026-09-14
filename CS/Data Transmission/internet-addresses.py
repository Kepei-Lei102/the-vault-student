"""Addresses, counted: IPv4, IPv6, MAC, private ranges and a subnet — with Python's ipaddress module.

Run:  python3 internet-addresses.py
"""
import ipaddress
print(f"IPv4: 32 bits -> {2**32:,} addresses  (4.3 billion; the world ran out in 2011–2019)")
print(f"IPv6: 128 bits -> {2**128:.2e} addresses  (about {2**128/8e9:.1e} per person alive)")
v4 = ipaddress.ip_address("192.168.1.37"); v6 = ipaddress.ip_address("2001:db8:0:0:0:0:8a2e:370")
print(f"{v4}  = {int(v4):032b}  private? {v4.is_private}")
print(f"{v6}  compressed: {v6.compressed}   full: {v6.exploded}")
for a in ["10.0.0.5", "172.16.4.9", "192.168.0.1", "8.8.8.8", "223.5.5.5"]:
    ip = ipaddress.ip_address(a); print(f"  {a:12s} {'private (never routed on the internet; NAT at the router)' if ip.is_private else 'public (globally unique)'}")
net = ipaddress.ip_network("192.168.1.0/24")
print(f"\nsubnet {net}: mask {net.netmask}, {net.num_addresses} addresses, hosts {net[1]} .. {net[-2]}, broadcast {net.broadcast_address}")
for sub in net.subnets(new_prefix=26): print(f"  split into /26: {sub}  ({sub.num_addresses} addresses each)")
mac = "3C:22:FB:9A:12:7E"
print(f"\nMAC {mac}: 48 bits = 6 bytes of hex; first three {mac[:8]} = the manufacturer (OUI, here Apple), last three the serial number burned in at the factory")
print(f"48 bits -> {2**48:.2e} possible MACs; the NIC's address never changes, the IP address is what the network hands it")
