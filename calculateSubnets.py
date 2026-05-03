import ipaddress

def allocate_54_from_48(prefix_48):
    """Show /54 allocations within a /48."""
    network = ipaddress.IPv6Network(prefix_48)
    subnets_54 = list(network.subnets(new_prefix=54))
    print(f"Total /54 allocations from {prefix_48}: {len(subnets_54)}")
    for i, s in enumerate(subnets_54[:64]):
        print(f"  Branch {i}: {s}")

allocate_54_from_48("2001:db8:acad::/48")
#from https://oneuptime.com/blog/post/2026-03-20-ipv6-subnets-from-48/view
#Total /54 allocations from 2001:db8:acad::/48: 64
#  Branch 0: 2001:db8:acad::/54
#  Branch 1: 2001:db8:acad:400::/54
#  Branch 2: 2001:db8:acad:800::/54
#  Branch 3: 2001:db8:acad:c00::/54
#  Branch 4: 2001:db8:acad:1000::/54
# ...
#
#  Branch 60: 2001:db8:acad:f000::/54
#  Branch 61: 2001:db8:acad:f400::/54
#  Branch 62: 2001:db8:acad:f800::/54
#  Branch 63: 2001:db8:acad:fc00::/54
