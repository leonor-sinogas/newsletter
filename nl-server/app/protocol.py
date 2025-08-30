from typing import Dict, Tuple

""" Veery simple line protoco (one command per line):

PING
ECHO text = hellow orld
CREATE NEWSLETTER title=Friends desc="Monthly check in"
LIST_NEWSLETERS
POST_REPLY nid=1 issue=2025-08 body="I started classes"
QUIT

Rules:
- First token is the COMMAND (uppercase recommended).
- Following tokens are key=value pairs. Values may contain spaces; quotes are allowed.

"""

def parse_line(line: str) -> Tuple[str, Dict[str,str]]:
    parts = tokenize(line)
    if not parts:
        raise ValueError("empty command")
    cmd = parts[0].upper()
    args = {}
    for tok in parts[1:]:
        if "=" not in tok:
            raise ValueError(f"bad token: {tok} (expected key=value)")
        k, v = tok.split("=", 1)
        args[k] = strip_quotes(v)
    return cmd, args

def tokenize(s: str):
    out = []
    cur = []
    in_quotes = False
    quote_char = ""
    i = 0
    while i < len(s):
        c = s[i]
        if in_quotes:
            if c == quote_char:
                in_quotes = False
                i += 1
                continue
            cur.append(c)
            i += 1
            continue
        else:
            if c in ("'", '"'):
                in_quotes = True
                quote_char = c
                i += 1
                continue
            if c.isspace():
                if cur:
                    out.append("".join(cur))
                    cur = []
                i += 1
                continue
            cur.append(c)
            i += 1
    if cur:
        out.append("".join(cur))
    return out

def strip_quotes(v: str) -> str:
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    return v

def encode_ok(payload: str) -> str:
    return f"OK {payload}"

def encode_err(msg: str) -> str:
    return f"ERR {msg}"