"""
Huawei Interview first question
Had exact same code but failed to pass...dunno why
"""

def delete3 (s):
    first = ""
    second = ""
    i = 0
    while i < len(s):

        if first != s[i]:
            first = s[i]
            i += 1

        elif first == s[i] and second != s[i]:
            second = s[i]
            i += 1
    
        elif first == s[i] and second == s[i]:
            s = s[:i-2] + s[i+1:]
            first = ""
            second = ""
            i = 0
            
    return s


print( delete3( "cddfffdc" ) )