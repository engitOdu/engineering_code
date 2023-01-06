import matplotlib.pyplot as plt

class Thermodynamics:

  def __init__(self,temp1, pressure1,pressure2,k):
    # self.v1 = v1
    # self.p1 = p1
    # self.v2 = v2
    # self.p2 = p2
    # self.v3 = v3
    # self.p3 = p3
    # self.v4 = v4
    # self.p4 = p4s
    self.temp1 = temp1
    self.pressure1 = pressure1
    self.pressure2 = pressure2
    self.k = k

  # def plot(self):
  #   # set up the P-V diagram
  #   plt.subplot(2, 1, 1)
  #   plt.plot([self.v1, self.v2], [self.p1, self.p2], 'b-', label='isothermal expansion')
  #   plt.plot([self.v3, self.v4], [self.p3, self.p4], 'r-', label='isobaric cooling')
  #   plt.xlabel('Volume (L)')
  #   plt.ylabel('Pressure (atm)')
  #   plt.legend()

  #   # set up the T-s diagram
  #   plt.subplot(2, 1, 2)
  #   plt.plot([1, 2, 3, 4], [1, 1, 1, 1], 'b-', label='isothermal expansion')
  #   plt.plot([4, 5, 6, 7], [1, 1, 2, 2], 'r-', label='isobaric cooling')
  #   plt.xlabel('Entropy (J/K)')
  #   plt.ylabel('Temperature (K)')
  #   plt.legend()

  #   plt.show()

  def temp2(self):
    temp2 = self.temp1 * ((self.pressure2 / self.pressure1) ** (self.k - 1) / self.k)
    return temp2;()

    

