# rand_gen 

This repository contains the source code, raw dataset used for testing and bell curve simulation associated with the preprint: **"A Statistical Benchmarking of Keystroke Entropy Pools Versus State-of-the-Art Software Random Number Generators"**.

### Contents
- **`harvest/`**: Keystroke interval harvester and logger implementation which runs as a background daemon so you might have to give accessibility permissions to run the program, depending on your machine
- **`simulations/`**: Monte Carlo simulation script for curve generation and compare with the real graph.
  - The code has been divided into two parts:
       - (i) Monte carlo simulation result per case (unimpressive plain text probabilities)

       - (ii) curve generation

<img width="774" height="431" alt="Screenshot 2026-04-17 at 9 20 04 AM" src="https://github.com/user-attachments/assets/c0ef6bb9-0626-48fb-8f44-8bc537c68404" />

Above: Sample curve generated

    
- **`sample_data/`**: Sample dataset used for the experimental results.
  

### **Prerequisites**
To run these scripts, you need the following libraries (ofc, you already should have Python 3.10 or later):

1. **pynput**
2. **matplotlib**

### To make use of the keystroke data log file

In the intervals obtained, the least significant digits are the most unreliable hence, random. The interval values extend till 6 decimal places. But I took the last 4 (Why 4? Why not 3? That is something I decided on based on the sweet spot between 'too deterministic' and 'too few options'). 


So I had 9999 maximum possible INT options. But in the project, I was comparing with standard python pseudo random number generators like random library. So I had to convert the integers into floats in [0,1). Otherwise the comparison would not have been fair.   


```python
with open("key_timings-1.log", "r") as f:
    tmng = []
    for _ in f:
        if _.strip():             
            tmng.append(float(_.strip())) 


#extracting last digs
last_digits = []
for t in tmng:
    fr_str = str(t).split(".")[1]  
    dig = fr_str[-4:]  

    last_digits.append(int(dig))


fl = [round(d / 9999, 4) for d in last_digits]


with open("keystroke_floats.txt", "w") as f:
    for val in fl:
        f.write(f"{val}\n")
```
So, the .txt file becomes the one being used in the simulation.


### Entanglement inspired correlation Monte Carlo simulation of the Alice and Bob detector experiment

The working of the simulation:

<img width="466" height="565" alt="Screenshot 2026-04-16 at 11 14 23 PM" src="https://github.com/user-attachments/assets/84836a86-ec0a-4b2e-86c0-d394bc6a2b2f" />


In my program, I have used run indices that might look random to your eyes but as a whole they can be taken as artifacts related to my dataset (the one attached in `sample_data/`) and can freely be changed (is encouraged, if you want to see how much is 'too little' and how much is 'just right' and if you make it too big, the thing becomes redundant as in they reuse points too aggressively so that is not good either)


### Full Documentation
For the complete methodology please refer to the **preprint** archived on Zenodo at [https://zenodo.org/records/18637817].

-- As part of the paper as a whole, tests were run on the data. The tests were all standard programs so not included in this repo --


