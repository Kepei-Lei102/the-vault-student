"""The Sand Reckoner: naming a number bigger than the universe.

Greek numerals stopped at a myriad myriads, 10^8.  Archimedes built a system
of "orders" and "periods" that reaches 10^(8 x 10^16), then used it to count
the grains of sand that would fill the cosmos -- taking Aristarchus's
sun-centred universe, the biggest anyone had proposed.  This script follows
his own chain of deliberate overestimates, every one rounded up.

Run:  python3 archimedes-sand.py
"""
import math
grains_per_poppy_seed = 10_000          # a poppy seed holds no more than 10^4 grains
seeds_across_finger = 40                # 40 poppy seeds side by side make a finger-breadth (about 19 mm)
# a sphere one finger-breadth across holds fewer than 40^3 = 64 000 seeds, so fewer than 6.4 x 10^8 grains: he rounds to 10^9
grains_per_finger_sphere = 10 ** 9
stadion_in_fingers = 10 ** 4            # a stadion (about 185 m) is fewer than 10^4 finger-breadths
earth_diameter_stadia = 10 ** 6         # ten times the largest estimate then current, to be safe
universe_diameter_stadia = 10 ** 14     # his upper bound for Aristarchus's sphere of the fixed stars
def grains(diameter_stadia):
    d_fingers = diameter_stadia * stadion_in_fingers
    return grains_per_finger_sphere * d_fingers ** 3      # spheres scale as the cube of the diameter
print(f"grains in a finger-breadth sphere : 10^{math.log10(grains_per_finger_sphere):.0f}   (64 000 seeds x 10^4 grains = 6.4 x 10^8, rounded up)")
print(f"grains to fill the Earth          : 10^{math.log10(grains(earth_diameter_stadia)):.0f}   (diameter 10^6 stadia = 10^10 finger-breadths)")
print(f"grains to fill the universe       : 10^{math.log10(grains(universe_diameter_stadia)):.0f}   (diameter 10^14 stadia = 10^18 finger-breadths)")
print("Archimedes' answer: fewer than 10^63 grains -- 'a thousand myriad units of the eighth order'\n")
print("his names: a myriad = 10^4; a myriad myriads = 10^8 ends the first order;")
print("the 10^8-th order ends the first period at 10^(8 x 10^8);")
print("the 10^8-th period ends at 10^(8 x 10^16) -- a 1 followed by 80 000 000 000 000 000 zeros.")
print("The sand needs only the eighth order of the first period. He built the tower to show it could be built.")
