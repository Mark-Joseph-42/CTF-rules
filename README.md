# Antigravity CTF

This repository contains the workspace, solve scripts, and documentation for CTF challenges solved by the **Antigravity** AI Agent.

## Repository Structure

```
.
├── message.txt              # (Challenge artifact - deleted)
├── server.log               # (Challenge artifact - deleted)
├── confidential.pdf         # (Challenge artifact - deleted)
├── solve_crack_power.py     # Python solution
├── system_prompt.md         # The System Prompt
└── secure_email/            # Source code
```

## Solved Challenges

### 1. Riddle Registry (Forensics)
*   **Goal:** Find flag hidden in PDF metadata.
*   **Methodology:**
    *   **Agentic Strategy:** "Scenario-Based Search" (Checking `gemini.google.com` for "how to extract PDF metadata").
    *   **Tools:** `exiftool`, base64 decoding.
*   **Flag:** `picoCTF{puzzl3d_m3tadata_f0und!_3578739a}`

### 2. Log Hunt (General Skills)
*   **Goal:** Reconstruct a flag scattered across a large server log file.
*   **Methodology:**
    *   **Analysis:** Used `grep "FLAGPART"` to isolate relevant lines.
    *   **Reconstruction:** Sorted by timestamp to assemble the pieces.
*   **Flag:** `picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}`

### 3. Crack the Power (Cryptography)
*   **Goal:** Decrypt an RSA message with a large modulus `N` but small public exponent `e=20`.
*   **Methodology:**
    *   **Vulnerability:** **Low Exponent Attack**. Since $m^e < N$ (or $m^e$ is only slightly larger), the message can be recovered by taking the integer $e$-th root of the ciphertext.
    *   **Script:** `solve_crack_power.py` uses a binary search algorithm to find the integer 20th root of $c + k \cdot n$.
*   **Flag:** `picoCTF{t1ny_e_4da5fb4d}`

### 4. Secure Email Service (Web Exploitation) [In Progress]
*   **Goal:** Exploit an S/MIME web implementation.
*   **Current Status:** Source code downloaded and under analysis.
*   **Potential Vector:** Header Injection or Signature Verification Bypass.

## Antigravity System Prompt
The file `system_prompt.md` contains the refined instructions used by the agent, emphasizing:
*   **Methodology First:** Asking "how" before doing.
*   **Browser Offloading:** Using web AI for reasoning to save local tokens.
*   **Velocity:** "Shoot first, debug later" operational mode.
