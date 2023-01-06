# import the Thermodynamics class
from thermodynamics import Thermodynamics

print("Enter temp1, p1, p2, k")
temp1 = float(input("Enter initial temp: "))
p1 = float(input("Enter initial pressure: "))
p2 = float(input("Enter second pressure: "))
k = float(input("Enter K: "))

# # create a Thermodynamics object and plot the P-V and T-s diagrams
thermo = Thermodynamics(temp1,p1,p2,k)
temp2 = thermo.temp2()
print(temp2) 
