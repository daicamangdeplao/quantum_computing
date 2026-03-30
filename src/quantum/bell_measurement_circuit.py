import sys
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Force UTF-8 output so Greek/special chars render on all platforms
sys.stdout.reconfigure(encoding='utf-8')


# =============================================
# Bell States (maximally entangled two-qubit states)
# =============================================
# |Phi+⟩ = (|00⟩ + |11⟩) / √2  →  measured as |00⟩
# |Phi-⟩ = (|00⟩ - |11⟩) / √2  →  measured as |10⟩
# |Psi+⟩ = (|01⟩ + |10⟩) / √2  →  measured as |01⟩
# |Psi-⟩ = (|01⟩ - |10⟩) / √2  →  measured as |11⟩

def prepare_bell_state(label: str) -> QuantumCircuit:
    """
    Returns a circuit that prepares the given Bell state.
      label: 'Phi+', 'Phi-', 'Psi+', 'Psi-'
    """
    qc = QuantumCircuit(2)
    if label in ('Psi+', 'Psi-'):
        qc.x(1)  # flip qubit 1 to get |Psi⟩ family
    qc.h(0)
    qc.cx(0, 1)
    if label in ('Phi-', 'Psi-'):
        qc.z(0)  # add phase flip for '-' variants
    return qc


def bell_measurement() -> QuantumCircuit:
    """
    Bell measurement circuit (inverse of Bell state preparation).
    Transforms the Bell basis back to the computational basis:
      CNOT(0→1), then H(0), then measure both qubits.
    """
    qc = QuantumCircuit(2, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    return qc

def draw_circuit(label: str):
    print("\n" + "=" * 58)
    print(f"Circuit diagram for |{label}⟩ preparation + Bell measurement:")
    print("=" * 58)
    ref = prepare_bell_state(label).compose(bell_measurement())
    print(ref.draw(output='text'))

# =============================================
# Demo: Bell Measurement for all four Bell states
# =============================================
simulator = AerSimulator()
# The number of times the circuit is run and measured independently
#   fewer shots -> rough estimation
#   more shots -> better estimation, but costly computation
# In theory, Bell measurement is **deterministic**, i.e. shot = 1 is actually sufficed.
# 1024 is just a good practice that might be adapted to probabilistic circuits.
SHOTS = 1024

bell_states = {
    'Phi+': '|Phi+⟩ = (|00⟩ + |11⟩) / √2',
    'Phi-': '|Phi-⟩ = (|00⟩ - |11⟩) / √2',
    'Psi+': '|Psi+⟩ = (|01⟩ + |10⟩) / √2',
    'Psi-': '|Psi-⟩ = (|01⟩ - |10⟩) / √2',
}

expected_outcome = {
    'Phi+': '00',
    'Phi-': '10',
    'Psi+': '01',
    'Psi-': '11',
}

print("=" * 58)
print("          Bell Measurement Circuit Demo")
print("=" * 58)

for label, description in bell_states.items():
    prep = prepare_bell_state(label)
    meas = bell_measurement()
    full_circuit = prep.compose(meas)

    result = simulator.run(full_circuit, shots=SHOTS).result()
    counts = result.get_counts()

    dominant = max(counts, key=counts.get)
    dominant_pct = counts[dominant] / SHOTS * 100

    print(f"\nBell state: {description}")
    print(f"Expected measurement outcome: |{expected_outcome[label]}⟩")
    print(f"Simulation ({SHOTS} shots): {counts}")
    print(f"  → collapsed to |{dominant}⟩ ({dominant_pct:.1f}%)")
    draw_circuit(label)

# # =============================================
# # Circuit diagram for |Phi+⟩ as reference
# # =============================================
# print("\n" + "=" * 58)
# print("Circuit diagram for |Phi+⟩ preparation + Bell measurement:")
# print("=" * 58)
# ref = prepare_bell_state('Phi+').compose(bell_measurement())
# print(ref.draw(output='text'))
#
# # =============================================
# # Circuit diagram for |Phi-⟩ as reference
# # =============================================
# print("\n" + "=" * 58)
# print("Circuit diagram for |Phi-⟩ preparation + Bell measurement:")
# print("=" * 58)
# ref = prepare_bell_state('Phi-').compose(bell_measurement())
# print(ref.draw(output='text'))


print("\nKey insight:")
print("  Bell measurement maps each Bell state to a unique")
print("  computational basis state, distinguishing all four")
print("  maximally entangled states with 100% certainty.")
