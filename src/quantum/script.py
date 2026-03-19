import numpy as np
from qiskit.quantum_info import Statevector

# =============================================
# Define computational basis
# =============================================
ket_0 = Statevector.from_label('0')
ket_1 = Statevector.from_label('1')

computational_basis = [ket_0, ket_1]

print(f'The computational basis: {computational_basis}')

# =============================================
# Collapse Measurement
# =============================================
# step 1: define the system state
psi = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
# step 2: measure the state given the probability
probabilities = np.abs(psi) ** 2
result = np.random.choice(np.arange(len(psi)), p=probabilities)
# the state have to collapse to a classical binary system: 0 or 1
# ket{0} = [1, 0], ket{1} = [0, 1]
collapsed = np.zeros_like(psi)
collapsed[result] = 1

print(f'Measured: {result}')
print(f'Collapsed state: {collapsed}')
