from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with 1 qubit and 1 classical bit
circuit = QuantumCircuit(1, 1)

# Apply a Hadamard gate to qubit 0
circuit.h(0)

# Measure qubit 0 and store the result in classical bit 0
circuit.measure(0, 0)

# Use the high-performance classical AerSimulator backend
simulator = AerSimulator()

# Run the simulation for 1,024 shots (repetitions) to gather statistics
job = simulator.run(circuit, shots=1024)
result = job.result()

# Extract and print the frequency of each measured state
counts = result.get_counts()
print("Measurement counts (out of 1024 shots):", counts)
