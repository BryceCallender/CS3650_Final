from qiskit import *

IBMQ.load_accounts()

print("Welcome to the random number guessing program")

numOfQubits = int(input("How many qubits do you want to use? (1 for numbers 0 and 1, 2 for 0-3, etc...): "))

q = QuantumRegister(numOfQubits)
c = ClassicalRegister(numOfQubits)

circuit = QuantumCircuit(q,c)

for i in range(0, numOfQubits):
    circuit.h(q[i])

circuit.measure(q, c)

# Use Aer's qasm_simulator
backend_sim = BasicAer.get_backend('qasm_simulator')

job = execute(circuit, backend_sim, shots=1024)

results = job.result()

counts = results.get_counts(circuit)

mostCommon = 0
highestBinary = ''

for binary, value in counts.items():
    if value > mostCommon:
        mostCommon = value
        highestBinary = binary

print("The Quantum computer has chosen a number. Try to guess it")

guessed_num = int(highestBinary, 2)

found = False

while not found:
    num = int(input("Guess a number: "))
    if num == guessed_num:
        found = True
        print("You guessed it the number was " + str(guessed_num))
    elif num > guessed_num:
        print("Too high")
    else:
        print("Too low")
