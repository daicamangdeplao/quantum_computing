#==============================================================================
# COMPLEX NUMBER
# - Addition
# - Subtraction
# - Multiplication
# - Division
# - Conjugate
# - Modulus
#==============================================================================
import numpy as np

z1 = 3 + 4j
z2 = 1 - 2j

add_z = z1 + z2
sub_z = z1 - z2
mul_z = z1 * z2
div_z = z1 / z2
conj_z1 = np.conjugate(z1)
conj_z2 = np.conjugate(z2)
mod_z1 = np.abs(z1)
mod_z2 = np.abs(z2)

print(f"""
z1 = {z1}, z2 = {z2}

Addition: {add_z}
Subtraction: {sub_z}
Multiplication: {mul_z}
Division: {div_z}
Conjugate of z1: {conj_z1}
Conjugate of z2: {conj_z2}
Magnitude of z1: {mod_z1}
Magnitude of z2: {mod_z2}
""")
