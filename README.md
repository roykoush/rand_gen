# rand_gen
key interval time extractor!

Uhh, I would def add the physics stuff here for dictionary purposes.
But for now, its pretty clear that you must install the time libraries and ig some permission must be given. 

Always shows this in my window, although it works okay:


<img width="563" height="308" alt="Screenshot 2025-07-14 at 8 03 40 PM" src="https://github.com/user-attachments/assets/26a8f3f7-c6ad-487e-b705-4b406ad30b6c" />

Added the log size just to keep track of the change. 




# The Reasons
This project investigates whether human cognitive entropy can serve as a valid, measurable, and reusable source of randomness for two distinct applications: 

(1) simulating quantum statistical behavior (via Bell-type tests) and 

(2) generating secure, deterministic passwords.

### Data Source 1: Using time-variations between keystrokes

Instead of relying on standard randomness libraries like Python’s `random` or hardware RNGs, this project extracts entropy from the last few decimal digits of each keypress interval, which are assumed to carry the most unpredictable and personal motor/cognitive noise. 

### Data Source 2: Web-cam Static a.k.a Visual Entropy

### Experiments: Overview
**In the Bell simulation**, the entropy is used to decide whether outcomes match or mismatch, based on angle differences (which may vary between runs). The key result is that the simulated match rates consistently follow theoretical expectations from quantum mechanics, proving that human-derived entropy can statistically behave like quantum randomness. It validates the quality of the entropy.

**In the password generator**, the same entropy is used to create secure, strong passwords. SHA-256 hashes are converted into characters from uppercase, lowercase, digits, and symbols. These digit strings are then hashed using SHA-256 to whiten and spread the entropy evenly, making it suitable for structured uses. The output is balanced (at least one from each class) and shuffled deterministically using the entropy itself (not external randomness). The default output is 16 characters, because 95^16 combinations provide over 10^30 possible outcomes — more than sufficient for real-world use. Users can truncate or expand as needed; the system supports variable lengths depending on application.

The password generator uses slices of 12 floats at a time. Each new run uses the next slice, making each password different — but still reproducible on the same device. 

On a different device or with a different user, the same logic yields completely different outputs, proving that the entropy is **user- and machine-specific**. Importantly, the entropy is finite and depletes with use. For example, the system stopped generating new passwords after 2,474 iterations when a float pool of 29,736 data points was exhausted — a behavior no PRNG exhibits. Additionaly, Bell's inequality has been run on the predicted outcomes, thus proving the pseudo nature of this randomness: a inherently classical system at the core.


These validate its nature as harvested, not simulated, randomness.

### Quantum Experiment as Randomness Validation

The Bell-type simulation in this project is not intended to violate Bell's inequality or test the foundations of quantum mechanics. Rather, it serves a different purpose: to **statistically validate the non-deterministic and pseudo-random nature** of the human-derived entropy extracted from keystroke intervals.

In quantum theory, when two entangled qubits are measured at different angles θₐ and θ_b, the probability that both measurements yield the same result is given as:

$$
P_{\text{match}} = \cos^2\left(\frac{\theta_a - \theta_b}{2}\right)
$$

This sinusoidal match probability is a fundamental signature of quantum statistical behavior.

In our simulation, this expected value is used to **bias a pair of binary outcomes** (`a`, `b`) such that the probability of agreement equals the theoretical `P_match`. Specifically:
- A float `x` from the entropy pool is compared to `P_match`.
- If `x < P_match`, the simulation enforces a match between `a` and `b`.
- Otherwise, a mismatch is assigned.

This Monte Carlo method requires that `x` be **uniformly and unpredictably sampled** from the interval [0, 1] in order for the outcome statistics to converge to theory over many trials. **If the entropy were biased, deterministic, or insufficient**, the simulated match rates would visibly diverge from the theoretical curve.

In repeated runs using keystroke-derived float values as the sampling base, the match frequencies consistently followed the cosine-squared law. This outcome does not demonstrate quantum entanglement, but it **empirically supports the claim that the human entropy behaves like a high-quality pseudo-random number generator** — sufficient for statistical modeling.

Furthermore, the simulation is sensitive to entropy exhaustion: once the keystroke float pool is depleted, the experiment ceases to operate, just as a physical random process (like radioactive decay) cannot continue without underlying physical events.

Thus, the quantum experiment serves as a **statistical validator** of the entropy’s non-determinism. While it remains classical and Bell-inequality-compliant by design, the experiment affirms that the randomness observed is not simulated or injected, but **harvested from a finite, external, user-specific source**.

### Password Generation Process Using Human-Derived Entropy

The password generator leverages the same finite pool of entropy extracted from keystroke timing intervals to produce secure, reproducible passwords tailored to each user-device environment. This process comprises several key stages designed to maximize entropy utilization while ensuring practical usability and cryptographic robustness:

1. **Entropy Sampling**  
   A contiguous slice of 12 floating-point values, each normalized to the interval [0, 1], is extracted sequentially from the keystroke-derived entropy pool. These floats serve as the fundamental randomness source for one password generation iteration. The pool is finite and depleted progressively with each new password.

2. **Hash-Based Whitening**  
   To mitigate biases and correlations inherent in raw timing data, the slice is processed through the SHA-256 cryptographic hash function. This step distributes entropy uniformly across the output bits, enhancing unpredictability and eliminating detectable structure within the input.

3. **Character Class Mapping**  
   The 256-bit hash output is segmented and mapped deterministically to characters drawn from four distinct classes: uppercase letters, lowercase letters, digits, and symbols. The generator enforces the inclusion of at least one character from each class to comply with common password complexity requirements.

4. **Deterministic Shuffling**  
   The final character sequence undergoes a deterministic shuffle process driven by additional entropy floats from the same pool. This rearrangement further obfuscates any residual ordering patterns while preserving reproducibility on the original device.

5. **Length Flexibility and Security**  
   The default output length is 16 characters, selected to yield a search space exceeding \(95^{16} \approx 10^{31}\) combinations, which is considered cryptographically strong against brute-force attacks. Users can specify different lengths, with the generator adjusting entropy slice usage accordingly.

6. **Reproducibility and Device-Specificity**  
   Due to the dependence on the exact sequence of entropy floats from a finite, device- and user-specific pool, the same password can be regenerated reliably on the original device given the same keystroke history. Conversely, different devices or users yield distinct password outputs, reinforcing personalized security.

7. **Entropy Exhaustion and Limitations**  
   The generator’s entropy pool is exhaustible; empirical observation shows cessation of password production after approximately 2,474 iterations with a 29,736-point float pool. This finite nature differentiates the system from standard software PRNGs with effectively infinite periods, imposing operational limits and necessitating entropy replenishment for sustained use.

   
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

### Applications of This Project

1. **Statistical Validation of Human-Derived Entropy Quality**  
   The project’s Bell-type simulation serves as a practical testbed to verify that keystroke timing entropy approximates high-quality pseudo-randomness sufficient for modeling quantum statistical distributions.

2. **Secure Password Generation with User- and Device-Specific Determinism**  
   The entropy-driven password generator enables reproducible password creation tied to a specific user and device, useful for scenarios where password recovery without storage is needed and limited external entropy sources exist.

3. **Entropy Source for Low-Resource or Entropy-Constrained Systems**  
   Provides a method to harvest entropy in environments without hardware RNGs or strong system entropy pools, leveraging human motor/cognitive noise as an alternative source.

4. **Empirical Study of Finite Entropy Exhaustion**  
   The project demonstrates that harvested entropy is finite and exhaustible, allowing for exploration of entropy depletion impacts on system performance and security in real-world applications.

5. **Baseline for Further Research on Human Cognitive Noise as Randomness**  
   Acts as a foundational model to encourage further investigation into using measurable human behavior signals for pseudo-random number generation in computational or cryptographic contexts.
