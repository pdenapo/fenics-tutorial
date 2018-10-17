# A trivial plot example showing a square mesh
from dolfin import * 
import matplotlib.pyplot as plt
mesh = UnitSquareMesh(4,4)
plot(mesh)
plt.show()

