from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Step 1: Create a Quantum Circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 2: Apply a Hadamard gate (H) to qubit 0
# This puts qubit 0 into a superposition (50% chance of 0, 50% chance of 1)
qc.h(0)

# Step 3: Apply a Controlled-NOT gate (CX)
# Qubit 0 is the control, Qubit 1 is the target. This entangles the two qubits.
qc.cx(0, 1)

# Step 4: Measure both qubits and save the results into the classical bits
qc.measure([0, 1], [0, 1])

# Optional: Draw the text-based circuit layout in your console
print("Circuit Diagram:")
print(qc.draw(output="text"))

# Step 5: Initialize the local simulator
simulator = AerSimulator()

# Step 6: Run the circuit on the simulator
# 'shots' is the number of times the experiment is repeated
job = simulator.run(qc, shots=1000)
result = job.result()

# Step 7: Get the measurement counts
counts = result.get_counts()
print("\nMeasurement Results (Bitstring: Counts):")
print(counts)
