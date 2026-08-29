# ASCII
# 'a' = 'A' + 32
# 'a' = 'a' - 32
# 0b100000 = 32

def toggle_char(s):
    ans = ""
    for ch in s:
        ans += chr(ord(ch) ^ 32)
    return ans
