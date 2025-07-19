import math, random
import matplotlib.pyplot as plt

# Parameters
n = 5000   # pairs per run
runs = 10  # runs per angle
step = 5   # degree step

angles = list(range(0, 181, step))
theort_ = []
measured = []

req_seq = 2 * n

# Check entropy size
if len(fl) < req_seq:
    print("Entropy list too small.")
    exit()

for theta in angles:
    diff = math.radians(theta)
    exp = math.cos(diff / 2) ** 2
    theort_.append(exp * 100)

    g = 0  # accumulate match %
    
    for _ in range(runs):
        # Pick a random start index
        start = random.randint(0, len(fl) - req_seq)
        m = 0

        for j in range(n):
            x = fl[start + 2*j]
            y = fl[start + 2*j + 1]

            if x < exp:
                a = b = 0 if y < 0.5 else 1
            else:
                a, b = (0, 1) if y < 0.5 else (1, 0)

            if a == b:
                m += 1

        pct = (m / n) * 100
        g += pct

    avg = g / runs
    measured.append(avg)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(angles, theort_, label='Quantum Prediction (cos²)', color='teal', linewidth=1.5)
plt.plot(angles, measured, label='Measured from Entropy', color='coral', linestyle='--', marker='o')
plt.xlabel('Angle (degrees)')
plt.ylabel('Match Percentage')
plt.title('Match vs Angle')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
