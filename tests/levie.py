import hashlib, string, random
import matplotlib.pyplot as plt
from Levenshtein import distance as levenshtein


with open("keystroke_floats.txt") as f:
    fl = [float(line.strip()) for line in f if line.strip()]

CHUNK_SIZE = 12
max_run = len(fl) // CHUNK_SIZE

def get_password(run):
    start = run * CHUNK_SIZE
    chunk = fl[start : start + CHUNK_SIZE]

    raw_digits = ''.join(str(f).split('.')[-1][-4:] for f in chunk)
    digest = hashlib.sha256(raw_digits.encode()).digest()

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%&*?"
    all_chars = upper + lower + digits + symbols

    pw = [
        upper[digest[0] % len(upper)],
        lower[digest[1] % len(lower)],
        digits[digest[2] % len(digits)],
        symbols[digest[3] % len(symbols)],
    ]

    for i in range(4, 16):
        pw.append(all_chars[digest[i] % len(all_chars)])

    random.seed(int.from_bytes(digest, 'big'))
    random.shuffle(pw)

    return ''.join(pw)


passwords = [get_password(i) for i in range(max_run)]

distances = [
    levenshtein(passwords[i], passwords[i+1])
    for i in range(len(passwords) - 1)
]


plt.figure(figsize=(12, 7))
plt.plot(distances, marker='o', linewidth=0.5, alpha=0.6, color='teal')
plt.title("Levenshtein Distance Between Consecutive Passwords")
plt.xlabel("Run number")
plt.ylabel("Distance")
plt.grid(True)
plt.tight_layout()
plt.show()
