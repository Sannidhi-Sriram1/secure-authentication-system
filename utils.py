import re

# Prevent buffer overflows with strict input validation
def is_valid_input(value, min_len=3, max_len=20):
    if not isinstance(value, str) or not (min_len <= len(value) <= max_len):
        return False
    return re.match(r"^[a-zA-Z0-9_.-]+$", value) is not None
