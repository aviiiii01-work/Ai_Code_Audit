import os
import pandas as pd

def read_or_write_file(mode: str, filename: str, content: str = "") -> str:
    """
    Handles file operations. Mode can be 'read' or 'write'.
    For 'write', provide the content string.
    """
    try:
        if mode == 'write':
            with open(filename, 'w') as f:
                f.write(content)
            return f"Saved to {filename}"
        else:
            if not os.path.exists(filename): return "File not found."
            with open(filename, 'r') as f:
                return f.read()
    except Exception as e:
        return str(e)