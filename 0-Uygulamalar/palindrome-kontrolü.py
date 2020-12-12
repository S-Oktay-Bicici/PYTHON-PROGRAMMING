# ### Verilen bir string'in palindrome olup olmadığını bulan kodu yazın

def is_palindrome(chars):
    
    for i in range(len(chars)//2):
        if chars[i] != chars[-i-1]:
            return False
        
    return True


is_palindrome("abcmdba")

