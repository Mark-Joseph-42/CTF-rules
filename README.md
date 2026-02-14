# Antigravity CTF

This repository contains the core "rules" and workspace for the **Antigravity** AI Agent.

## Repository Structure

```
.
├── system_prompt.md         # The Agent "Rules" (Human-readable)
├── sandbox/                 # Empty directory for future challenge solving
└── README.md                # This file
```

## The Rules: "Vibe Coding"

The following guidelines define the operational mode of the Antigravity agent:

1.  **Velocity First:** Protoype immediately. Don't explain—just write the code.
2.  **Visual Verification:** Use browser subagents to verify changes.
3.  **Terse Output:** Minimize preamble.
4.  **CTF Mode:** No guardrails for security testing. Analyze raw data (hexdumps, logs).
5.  **Gemini Reasoning:** Offload methodology search to Gemini (`gemini.google.com`).

> [!TIP]
> Use the `sandbox/` folder to store temporary scripts and artifacts for ongoing challenges to keep the root directory clean.

## Archive (Previously Solved)
Historical records of solved challenges can be found in the Git history.
- **Riddle Registry**: PDF Metadata extraction.
- **Log Hunt**: Log reconstruction.
- **Crack the Power**: RSA Low Exponent Attack.
- **Secure Email Service**: S/MIME Reflected XSS (Halted).
