# Quantum Random Number Generator  
*A quantum-powered true random number generator (QRNG) implemented in Python using Qiskit*  

## Project Overview

This repository provides a quantum-based random number generator (QRNG) implemented in **Qiskit**, allowing for the generation of (pseudo) true-random numbers by measuring quantum superposition. The tool can generate uniformly distributed random integers in a given range using proper rejection sampling to avoid modulo bias.

**Key features:**

- Uses **quantum circuits** (Hadamard + measurement) to create randomness  
- Calculates minimum number of qubits required for a given upper bound  
- Implements **rejection sampling**: only accepts bitstrings that fall within the valid range  
- Easily configurable for different ranges  
- Designed to be extendable for use with real quantum hardware  

---
