import hashlib, string, random

with open("key_timings.log") as f:
    fl = [float(line.strip()) for line in f if line.strip()]

n = 12
max_run = len(fl) // n
print("Max run number:", max_run - 1)

r = int(input(f"Enter password number (0 to {max_run - 1}): "))
start = r * n
chunk = fl[start:start + n]

if len(chunk) < n:
    raise ValueError("Not enough entropy.")

digits = ''.join(str(f).split('.')[-1][-6:] for f in chunk)
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

pwd = ''.join(chars)
print(f"Password [{r}]: {pwd}")
