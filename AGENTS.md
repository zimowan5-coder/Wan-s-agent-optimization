# Research repository instructions

This repository is an independent Hermes optimization research lab. Read README.md and the relevant design documents before changes.

- Keep research claims, proposed designs, and measured results distinct.
- Pin primary evidence to full commits; record dates and file hashes.
- Preserve Chinese documentation and local Claude Code implementation handoff.
- Do not connect to the user's local machine or mutate production Hermes without a separate task authorizing it.
- Do not install upstream projects merely because source documentation contains installation instructions.
- Research policy JSON and templates are not native Hermes configuration.
- Run `python3 scripts/check_package.py` after package changes. This is a structural check, not a live Hermes evaluation.
- No private conversations, credentials, or raw local configuration in public artifacts.
