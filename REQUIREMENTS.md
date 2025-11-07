# ANProto Python Requirements

## System Requirements

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv or venv (recommended)

## Python Package Dependencies

### Core Dependencies
- cryptography >= 40.0
  - Provides Ed25519 cryptographic primitives
  - Handles key generation, signing, and verification

### Development Dependencies
- setuptools >= 61.0
  - Required for package build and installation
- wheel
  - Required for package distribution

## Installation Requirements

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Upgrade package tools
pip install --upgrade pip setuptools wheel

# Install package in editable mode
pip install -e .
```

### System-Wide Installation (Not Recommended)
If installing system-wide, you'll need either:
- Administrator/root privileges
- `--break-system-packages` flag for pip (not recommended)

## Operating System Support

### Linux
- Fully supported
- Tested on modern distributions
- No additional requirements

### macOS
- Supported
- May need Command Line Tools installed
- No additional requirements

### Windows
- Supported
- May need Microsoft Visual C++ Build Tools for cryptography package
- Use appropriate activation script for virtual environment

## Memory Requirements
- Minimal (~50MB RAM during operation)
- No specific disk space requirements beyond Python installation

## Network Requirements
- None for operation
- Internet connection only needed for initial package installation

## Security Requirements
- Access to system entropy source for key generation
- Read/write permissions in installation directory
- Execute permissions for Python interpreter