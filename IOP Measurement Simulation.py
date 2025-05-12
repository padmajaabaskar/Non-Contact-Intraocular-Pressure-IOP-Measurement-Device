!pip install pyvista vtk fenics open3d
import pyvista as pv

mesh = pv.read("/content/drive/MyDrive/Cornea 3D.stl")

simplified_mesh = mesh.decimate(0.5)
simplified_mesh.save("Cornea_3D_Simplified.stl")

!pip install numpy-stl
!pip install meshio[all]

import meshio
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mesh = meshio.read("Cornea_3D_Simplified.stl")
points = np.array(mesh.points)
cells = np.array(mesh.cells_dict["triangle"])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_trisurf(points[:, 0], points[:, 1], points[:, 2], triangles=cells, cmap="coolwarm")

plt.show()

density = 1050
poisson_ratio = 0.49
mu_1 = 0.3e6
alpha_1 = 1.5

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.add_collection3d(Poly3DCollection(points[cells], alpha=0.3, edgecolor="k"))
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Cornea STL Model")

plt.show()

import sympy as sp

t = sp.symbols("t")
# New peak = 40 mmHg = 5332.88 Pa
P_air = 5332.88 * sp.exp(-(t - 0.015)**2 / (2 * (0.005)**2))

sp.plot(
    P_air,
    (t, 0, 0.05),
    xlabel="Time (s)",
    ylabel="Pressure (Pa)",
    title="Air-Puff Pressure Profile",
    ylim=(0, 6000)
)

P_input_mmHg = 40

A_applanation_mm2 = 2.5
A_applanation_m2 = A_applanation_mm2 * 1e-6

A_input_mm2 = 3.06
A_input_m2 = A_input_mm2 * 1e-6

P_eye_mmHg = P_input_mmHg * (A_input_m2 / A_applanation_m2) - 38.00

print(f"Calculated IOP of the eye: {P_eye_mmHg:.2f} mmHg")
