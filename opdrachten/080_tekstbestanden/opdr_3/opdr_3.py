# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt(text):
    Result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            Result += chr((ord(char) - start +5) %26 + start)
        else:
            Result += char
    return Result

def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start -5)% 26 + start)
        else:
            result += char
    return result

original_text = "dit is een stukje text dat is beveiligt"
encrypt_text = encrypt(original_text)
decrypt_text = decrypt(encrypt_text)

print("origigneel", original_text)
print("versleuteld:", encrypt_text)
print("ontsleuteld", decrypt_text)