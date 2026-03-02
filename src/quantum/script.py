from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit

ket_0 = Statevector.from_label('0')
ket_1 = Statevector.from_label('1')

computational_basis = [ket_0, ket_1]

print(f'The computational basis: {computational_basis}')
