def is_aboba(s: str) -> bool:
    for i in range(len(s)):
        if s.count(str(i)) != int(s[i]):
            return False
    return True


print(is_aboba("amongus"))