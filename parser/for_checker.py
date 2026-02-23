import re

def check_for_statements(code: str) -> bool:
    pattern = r'\bfor\s*\(?.*\)?\s*\{'
    matches = re.findall(pattern, code)
    return len(matches) > 0