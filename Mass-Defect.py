Mnucleus = (float(input("Enter Mass Number: ")) * float(1.66054E-27)) - (float(input("Enter Electron Amount: ")) * float(9.10915E-31))
Mprotons = (float(input("Enter Proton Amount: ")) * float(1.67262E-27)) + (float(input("Enter Neutron Amount: ")) * float(1.67495E-27))
print("Mnucleus =", Mnucleus), print("Mprotons =", Mprotons), print("Mass Defect =", Mnucleus - Mprotons)
input()
