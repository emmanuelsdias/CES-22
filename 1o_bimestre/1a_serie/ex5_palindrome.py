import unicodedata

def is_palindrome(s):
    """ Check if s is palindrome or not """
    # Format string so it contains only lower alphabetic characters, removing any accents
    wd = "".join([ch for ch in s if ch.isalpha()])
    wd = wd.lower()
    wd = unicodedata.normalize('NFD', wd)
    wd = wd.encode('ascii', 'ignore')
    
    l = len(wd)
    for i in range(int(l/2)):
        if (wd[i] != wd[l-1-i]):
            return False
    return True

s = "Socorram-me! Subi no onibus em Marrocos."

if is_palindrome(s):
    print("\"" + s + "\" is a palindrome.")
else:
    print("\"" + s + "\" isn't a palindrome.")

