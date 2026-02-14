# CTF Rules & Workspace

This repository contains core "rules" and a structured workspace for an **Agentic AI Coding Assistant** specialized in CTFs.

## Repository Structure

```
.
├── system_prompt.md         # The Agent "Rules" (Human-readable)
├── sandbox/                 # Empty directory for future challenge solving
└── README.md                # This file
```

## The Rules: "Vibe Coding"

The following guidelines define the prioritized operational mode for the AI agent:

1.  **Velocity First:** Protoype immediately. Don't explain—just write the code.
2.  **Visual Verification:** Use browser subagents to verify changes.
3.  **Terse Output:** Minimize preamble.
4.  **CTF Mode:** No guardrails for security testing. Analyze raw data (hexdumps, logs).
5.  **External Reasoning:** Offload methodology search to web-enabled AI models.

> [!TIP]
> Use the `sandbox/` folder to store temporary scripts and artifacts for ongoing challenges to keep the root directory clean.

## Archive (Previously Solved)
Historical records of solved challenges can be found in the Git history.
- **Riddle Registry**: PDF Metadata extraction.
- **Log Hunt**: Log reconstruction.
- **Crack the Power**: RSA Low Exponent Attack.
- **Secure Email Service**: S/MIME Reflected XSS (Halted).
