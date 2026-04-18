word = input("Enter word:")
key = int(input("Enter key:"))
result = ""
for ch in word:
    if ch.isalpha():
        if ch.islower():
            new = chr(ord(ch) + key)
            result += new
        else:
            new = chr(ord(ch) + key)
            result += new
print(result)