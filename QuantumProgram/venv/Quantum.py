from qiskit import *

IBMQ.load_accounts()

print("Welcome to the random number guessing program")

numOfQubits = int(input("How many qubits do you want to use? (1 for numbers 0 and 1, 2 for 0-3, etc...): "))

# Make the quantum registers for generating the numbers and the
# classical registers to grab the measured values
q = QuantumRegister(numOfQubits)
c = ClassicalRegister(numOfQubits)

# Create the quantum circuit
circuit = QuantumCircuit(q, c)

# Add numofQuibits amount of H gates to create superpositions
for i in range(0, numOfQubits):
    circuit.h(q[i])

# Measure every quantum register line
circuit.measure(q, c)

# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')

job = execute(circuit, backend_sim, shots=1024)

results = job.result()

counts = results.get_counts(circuit)

mostCommon = 0
highestBinary = ''

# Find the highest probability for each state of bits
for binary, value in counts.items():
    if value > mostCommon:
        mostCommon = value
        highestBinary = binary

print("The Quantum computer has chosen a number. Try to guess it")

guessed_num = int(highestBinary, 2)

found = False

# Try to guess the number
while not found:
    num = int(input("Guess a number: "))
    if num == guessed_num:
        found = True
        print("You guessed it the number was " + str(guessed_num))
    elif num > guessed_num:
        print("Too high")
    else:
        print("Too low")
