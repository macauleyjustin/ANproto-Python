"""Minimal ANProto implementation in Python.

Functions:
 - Gen() -> str : returns base64(pub) + base64(priv64)
 - Hash(d: str) -> str : base64(sha256(d))
 - Sign(h: str, k: str) -> str : given payload h and key k (pubB64+privB64) returns pubB64 + base64(sig || timestamp||h)
 - Open(m: str) -> str : verifies and returns the message (timestamp+payload) string
"""
from __future__ import annotations

import base64
import hashlib
import time

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives import serialization


def Gen() -> str:
    """Generate a new key pair and return base64(pub) + base64(priv64).

    priv64 is seed(32) || pub(32) which mirrors Go's crypto/ed25519.GenerateKey output.
    """
    seed = Ed25519PrivateKey.generate().private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )
    priv = Ed25519PrivateKey.from_private_bytes(seed)
    pub = priv.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )
    priv64 = seed + pub
    pub_b64 = base64.b64encode(pub).decode("ascii")
    priv_b64 = base64.b64encode(priv64).decode("ascii")
    return pub_b64 + priv_b64


def Hash(d: str) -> str:
    h = hashlib.sha256(d.encode("utf-8")).digest()
    return base64.b64encode(h).decode("ascii")


def Sign(h: str, k: str) -> str:
    """Sign payload h using key string k (pubB64+privB64).

    Returns pubB64 + base64(signature || timestamp||h)
    """
    if len(k) < 44 + 88:
        raise ValueError("invalid key length")
    pub_b64 = k[:44]
    priv_b64 = k[44:]
    priv_bytes = base64.b64decode(priv_b64)
    seed = priv_bytes[:32]
    priv = Ed25519PrivateKey.from_private_bytes(seed)

    ts_ms = str(time.time_ns() // 1_000_000)
    msg = (ts_ms + h).encode("utf-8")
    sig = priv.sign(msg)
    signed = sig + msg
    signed_b64 = base64.b64encode(signed).decode("ascii")
    return pub_b64 + signed_b64


def Open(m: str) -> str:
    """Open and verify message m. Returns the message bytes (timestamp+payload) as string.

    Expects message format: pubB64 + base64(sig || msg)
    """
    if len(m) < 44:
        raise ValueError("invalid message")
    pub_b64 = m[:44]
    signed_b64 = m[44:]
    signed = base64.b64decode(signed_b64)
    if len(signed) < 64:
        raise ValueError("signed message too short")
    sig = signed[:64]
    msg = signed[64:]
    pub = base64.b64decode(pub_b64)
    pubobj = Ed25519PublicKey.from_public_bytes(pub)
    pubobj.verify(sig, msg)
    return msg.decode("utf-8")
