# rand_gen
key interval time extractor!

Uhh, I would def add the physics stuff here for dictionary purposes.
But for now, its pretty clear that you must install the time libraries and ig some permission must be given. 

Always shows this in my window, although it works okay:


<img width="563" height="308" alt="Screenshot 2025-07-14 at 8 03 40 PM" src="https://github.com/user-attachments/assets/26a8f3f7-c6ad-487e-b705-4b406ad30b6c" />

Added the log size just to keep track of the change. 




# The Reasons
This project investigates whether human cognitive entropy — specifically, timing variations between keystrokes — can serve as a valid, measurable, and reusable source of randomness for two distinct applications: (1) simulating quantum statistical behavior (via Bell-type tests) and (2) generating secure, deterministic passwords.

Instead of relying on standard randomness libraries like Python’s `random` or hardware RNGs, this project extracts entropy from the last few decimal digits of each keypress interval, which are assumed to carry the most unpredictable and personal motor/cognitive noise. These digit strings are then hashed using SHA-256 to whiten and spread the entropy evenly, making it suitable for structured uses.

**In the Bell simulation**, the entropy is used to decide whether outcomes match or mismatch, based on angle differences (which may vary between runs). The key result is that the simulated match rates consistently follow theoretical expectations from quantum mechanics, proving that human-derived entropy can statistically behave like quantum randomness. It validates the quality of the entropy without needing to prove or reproduce a fixed number like 91.4%.

**In the password generator**, the same entropy is used to create secure, strong passwords. SHA-256 hashes are converted into characters from uppercase, lowercase, digits, and symbols. The output is balanced (at least one from each class) and shuffled deterministically using the entropy itself (not external randomness). The default output is 16 characters, because 95^16 combinations provide over 10^30 possible outcomes — more than sufficient for real-world use. Users can truncate or expand as needed; the system supports variable lengths depending on application.

The password generator uses slices of 12 floats at a time. Each new run uses the next slice, making each password different — but still reproducible on the same device. On a different device or with a different user, the same logic yields completely different outputs, proving that the entropy is **user- and machine-specific**. Importantly, the entropy is finite and depletes with use. For example, the system stopped generating new passwords after 2,478 iterations when a float pool of 29,736 data points was exhausted — a behavior no PRNG exhibits. This validates its nature as harvested, not simulated, randomness.

**Why this is original:**

* It uses a unique, fully human-derived entropy source.
* It validates this entropy via simulation *and* practical application.
* It demonstrates that the entropy is finite, exhaustible, reproducible (on the same device), and unrepeatable elsewhere.
* It uses no black-box randomness — all randomness is sourced, tracked, and accounted for.
* The project links quantum statistical modeling and real-world cryptography through a common entropy pipeline.

**What the project is not claiming:**

* It does not replace the `random` library.
* It does not claim infinite or perfect randomness.
* It does not compete with quantum or hardware RNGs.

Instead, it demonstrates that human cognitive entropy is structured, scientifically testable, and functionally useful — capable of powering both simulations and secure systems, while exhibiting the same failure modes (entropy exhaustion, sensitivity to environment) that characterize real physical randomness.


