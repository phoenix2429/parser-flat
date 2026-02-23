import re

def check_if_statements(code: str) -> bool:
    pattern = r'\bif\s*\(?.*\)?\s*\{'
    matches = re.findall(pattern, code)
    return len(matches) > 0