def check_braces(code: str) -> bool:
    stack = []

    for ch in code:
        if ch == '{':
            stack.append(ch)
        elif ch == '}':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0