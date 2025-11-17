# Necessary imports
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def quantum_random_number_generator(number):
    n = 1
    while 2**n <= number:
        n += 1
    
    # Simulator
    aersim = AerSimulator()

    while True:

        # Initializing quantum circuit
        qrng = QuantumCircuit(n,n)
        # Creating superposition to induce randomness
        qrng.h(range(n))
        # Measurement in z-basis 
        qrng.measure(range(n),range(n))

        # Runable circuit
        transpiled_qrng = transpile(qrng,aersim)
        # Shots = 1, since we want a single random result
        job = aersim.run(transpiled_qrng,shots=1)
        result = job.result()
        # counts gives a dict with outcome as keys and frequency as values
        counts = result.get_counts()
        # randome bits only takes the dict key
        random_bits = list(counts.keys())[0]
        # random number generated in decimal
        random_digit = int(random_bits,2)
        if random_digit <= number:
            return random_digit

