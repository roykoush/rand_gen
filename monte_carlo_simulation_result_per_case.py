import math, random

# Parameters
theta_a = 0
theta_b = 56#float(input("Enter the angle:"))
n = 5000#int(input("Enter number of runs per trial:")) 
runs = 10 #per major-run
diff = math.radians(theta_a - theta_b)
exp = math.cos(diff / 2) ** 2
print(f"Expected match: {exp * 100:.2f}%")

# mustn't choose in last seg
seq = 2 * n  # = 4000 values per run
if len(fl) < seq:
    print("Entropy list too small.")
    exit() #nice new word, would have saved A LOT of trouble in the parking program last yr

g = 0
#marco polo model
for i in range(runs):
    # Random start index that gives enough space for 4000 values
    start = random.randint(0, len(fl) - seq)
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

    pr = (m / n) * 100
    print(f"Run {i+1}: {pr:.2f}% match")
    g += pr

print(f"Avg: {g / runs:.2f}%")
