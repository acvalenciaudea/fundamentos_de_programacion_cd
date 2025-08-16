# 2. Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. s: clean message
#  2. k: number of letters to rotate
def matchingStrings(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate = k % len(alphabet)
    alphabet_rotated = alphabet[rotate:] + alphabet[:rotate]
    result = ""
	
    for char in s:
        lower_char = char.lower()
        if lower_char in alphabet:
            index = alphabet.index(lower_char)
            code = alphabet_rotated[index]
            result += code if char.islower() else code.upper()
        else:
            result += char
            
    return result


print(matchingStrings("middle-Outz", 2))
print(matchingStrings("D3q4", 0))
print(matchingStrings("1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M", 27))
print(matchingStrings("www.abc.xy", 87))

