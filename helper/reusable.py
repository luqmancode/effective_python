"""Helper functions on general usecases"""


def to_str(bytes_or_str) -> str:
    """convert b'hello' to 'hello' and 'hi' to 'hi'"""
    if isinstance(bytes_or_str, bytes):
        return bytes.decode('utf-8')
    return bytes_or_str


def to_bytes(bytes_or_str) -> bytes:
    """Convert 'Hello' to b'Hello' and 'à propos' to b'a\u0300 propos'"""
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode()
    return bytes_or_str
