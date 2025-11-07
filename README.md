# ANProto Python Implementation

A minimal Python implementation of ANProto, providing Ed25519-based message signing and verification with timestamps. This implementation is compatible with the Go and JS versions of ANProto.

## Features

- Ed25519 key pair generation
- Message hashing (SHA-256)
- Message signing with timestamps
- Signature verification and message extraction
- Command-line interface
- Cross-implementation compatibility

## Quick Start

### Installation (Using Virtual Environment - Recommended)

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install package
pip install -e .
```

### Basic Usage

```bash
# Generate a new key pair
python an_cli.py gen > key.txt

# Hash and sign a message
HASH=$(python -c "import anproto; print(anproto.Hash('hello'))")
python an_cli.py sign "$HASH" "$(cat key.txt)" > signed.txt

# Verify a signed message
python an_cli.py open "$(cat signed.txt)"
```

### Python API Example

```python
from anproto import Gen, Hash, Sign, Open

# Generate a new key pair
key = Gen()  # Returns base64(pub) + base64(priv)

# Hash a message
msg_hash = Hash("Hello World")  # Returns base64(sha256(msg))

# Sign a message
signed = Sign(msg_hash, key)  # Returns pubB64 + base64(sig || timestamp || msg)

# Verify and extract message
message = Open(signed)  # Returns timestamp + payload as string
```

## API Reference

### Gen() → str
Generates a new Ed25519 key pair and returns them as concatenated base64 strings:
- First 44 characters: base64(public key)
- Remaining 88 characters: base64(private key seed || public key)

### Hash(d: str) → str
Computes SHA-256 hash of the input string and returns it as base64.

### Sign(h: str, k: str) → str
Signs a message hash using the provided key:
- `h`: Message hash (from Hash())
- `k`: Key string from Gen()
Returns: pubB64 + base64(signature || timestamp || hash)

### Open(m: str) → str
Verifies and extracts the message from a signed payload:
- `m`: Signed message from Sign()
Returns: timestamp + payload as string
Raises: ValueError for invalid format, InvalidSignature for verification failure

## Development

### Running Tests

```bash
# Using the test script
bash run_tests.sh

# Or directly with unittest
python -m unittest discover -s tests -p "test*.py" -v
```

### Making CLI Executable (Optional)

```bash
chmod +x an_cli.py
```

## Requirements

- Python 3.8 or higher
- cryptography >= 40.0
- See requirements.txt for full dependencies

## License

This is a minimal implementation for demonstration purposes. See the original protocol specification for licensing details.

