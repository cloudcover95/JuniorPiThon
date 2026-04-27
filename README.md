# JuniorPiThon

**Python IDE + Pi Network App Ecosystem** for JuniorCloud LLC (cloudcover95)

A lightweight, sovereign Python development and runtime environment built for Raspberry Pi and edge nodes. Designed to work seamlessly with the broader JuniorCloud stack (JuniorStock, JuniorHome, JuniorMemSys, etc.).

## Features
- Local-first Python IDE/runtime optimized for Raspberry Pi
- Network app orchestration for edge device fleets
- Low-power, zero-cloud design
- Easy integration with JuniorStock trading SDK and other JuniorCloud components
- Supports Apple Silicon edge nodes alongside Pi hardware

## Project Structure
JuniorPiThon/
├── src/juniorpithon/     # Main package
├── pyproject.toml        # Modern Python project config
├── .gitignore
└── README.md
text## Quick Start

```bash
# Clone the repo
git clone https://github.com/cloudcover95/JuniorPiThon.git
cd JuniorPiThon

# Install dependencies (if using pyproject.toml)
pip install -e .

# Run the main application (adjust based on your entry point)
python -m juniorpithon
Part of JuniorCloud Ecosystem

JuniorStock — Edge-native 45 W quantitative trading SDK
JuniorHome — Sovereign edge computing home hub
JuniorMemSys-Suite — Topological memory & JuniorAGI components

Built with the same edge-native, ternary-optimized, sovereign philosophy as the rest of the JuniorCloud family.
Zero cloud. Maximum sovereignty.

Made with ❤️ by cloudcover95 @ JuniorCloud LLC
