import hashlib, string, random, math
import matplotlib.pyplot as plt
from collections import Counter

with open("keystroke_floats.txt") as f:
    fl = [float(line.strip()) for line in f if line.strip()]

n = 12              # Floats per password
group_size = 50     # Number of passwords per group
trial_len = group_size * n
max_trials = len(fl) // trial_len


all_entropies = [[] for _ in range(group_size)]

def password_from_chunk(chunk):
    digits = ''.join(str(f).split('.')[-1][-4:] for f in chunk)
    digest = hashlib.sha256(digits.encode()).digest()
    U, L, D, S = string.ascii_uppercase, string.ascii_lowercase, string.digits, "!@#$%&*?"
    ALL = U + L + D + S
    chars = [
        U[digest[0] % len(U)],
        L[digest[1] % len(L)],
        D[digest[2] % len(D)],
        S[digest[3] % len(S)],
    ]
    for i in range(4, 16):
        chars.append(ALL[digest[i] % len(ALL)])
    random.seed(int.from_bytes(digest, 'big'))
    random.shuffle(chars)
    return ''.join(chars)

def shannon_entropy(pw):
    freqs = Counter(pw)
    total = len(pw)
    return -sum((c/total) * math.log2(c/total) for c in freqs.values())


for t in range(max_trials):
    offset = t * trial_len
    for r in range(group_size):
        start = offset + r * n
        chunk = fl[start:start + n]
        if len(chunk) < n:
            break
        pw = password_from_chunk(chunk)
        H = shannon_entropy(pw)
        all_entropies[r].append(H)

# Average per position
avg_entropies = [sum(x)/len(x) for x in all_entropies]

# === Plot
plt.plot(range(1, group_size+1), avg_entropies, marker='o', color='blue', label='Average Entropy')
plt.axhline(y=3.75, color='red', linestyle='--', label='Min recommended entropy (3.75)')
plt.title("Avg Shannon Entropy Per Password Position (Averaged Over All Trials)")
plt.xlabel("Password Position in Group (1–50)")
plt.ylabel("Avg Entropy (bits per char)")
plt.ylim(3.5, 4.2)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
