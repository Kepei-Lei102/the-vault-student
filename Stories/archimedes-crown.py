"""The crown: why the bath story is not how he did it.

Vitruvius says Archimedes compared the water overflowing from a full vessel
when the crown, then an equal mass of gold, then of silver were lowered in.
Galileo, aged 22, pointed out the problem: the differences are tiny, and a
balance is far more sensitive than a basin.  Both are computed here for a
crown of one Roman pound (327 g) with a tenth of its gold swapped for silver.

Run:  python3 archimedes-crown.py
"""
import math
m = 0.327                           # kg, a Roman pound
rho_au, rho_ag, rho_w = 19300.0, 10500.0, 1000.0
f_ag = 0.10                         # tenth of the mass replaced by silver
V_gold = m / rho_au
V_crown = m * (1 - f_ag) / rho_au + m * f_ag / rho_ag
dV = V_crown - V_gold
print(f"pure gold, {m*1e3:.0f} g:      volume {V_gold*1e6:6.2f} cm3")
print(f"crown, 10 % silver:      volume {V_crown*1e6:6.2f} cm3   -> {dV*1e6:.2f} cm3 more\n")
for d_cm in (10, 20, 30):
    A = math.pi * (d_cm / 2 / 100) ** 2
    print(f"basin {d_cm:2d} cm across: the extra overflow is a rise of {dV / A * 1e3:.2f} mm of water")
print("   -- a tenth of a millimetre in a bowl, with the meniscus and the splash: not measurable in 250 BC\n")
# the hydrostatic balance: weigh the crown against an equal mass of gold, then immerse both
loss_gold = rho_w * V_gold * 9.81; loss_crown = rho_w * V_crown * 9.81
print("hydrostatic balance (On Floating Bodies): hang crown and gold on a beam, balanced in air; lower both into water")
print(f"   upthrust on the gold  {loss_gold*1e3:.1f} mN;  on the crown {loss_crown*1e3:.1f} mN;  the beam tips by {(loss_crown-loss_gold)*1e3:.1f} mN")
print(f"   that is {(loss_crown-loss_gold)/ (m*9.81) * 100:.2f} % of the crown's weight -- {((loss_crown-loss_gold)/9.81)*1e3:.1f} g on a scale, easily seen")
print("\nthe density that gives the game away, from the two weighings alone:")
print(f"   rho = W_air / (W_air - W_water) x rho_water = {m*9.81/(loss_crown)*rho_w:.0f} kg/m3  (pure gold would read 19300)")
