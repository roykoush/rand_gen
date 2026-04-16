# rand_gen 

This repository contains the source code, raw dataset used for testing and bell curve simulation associated with the preprint: **"A Statistical Benchmarking of Keystroke Entropy Pools Versus State-of-the-Art Software Random Number Generators"**.

### Contents
- **`harvest/`**: Keystroke interval harvester and logger implementation which runs as a background daemon so you might have to give accessibility permissions to run the program, depending on your machine
- **`simulations/`**: Monte Carlo simulation script for bell curve generation.
- **`sample_data/`**: Sample dataset used for the experimental results.

### **Prerequisites**
To run these scripts, you need the following libraries (ofc, you already should have Python 3.10 or later):

1. **pynput**
2. **matplotlib**

### Full Documentation
For the complete methodology please refer to the **preprint** archived on Zenodo at [https://zenodo.org/records/18637817].

-- As part of the paper as a whole, tests were run on the data. The tests were all standard programs so not included in this repo --


