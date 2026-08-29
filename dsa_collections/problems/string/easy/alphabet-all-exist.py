def all_exist(s: str):
    seen = [False] * 26

    for c in s.lower():
        if 'a' <= c <= 'z':
            seen[ord(c) - ord('a')] = True

    return all(seen)