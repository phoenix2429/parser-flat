import re

def check_while_statements(code: str) -> bool:
    pattern = r'\bwhile\s*\(?.*\)?\s*\{'
    matches = re.findall(pattern, code)
    return len(matches) > 0