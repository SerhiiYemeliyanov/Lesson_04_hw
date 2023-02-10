print("Home Work L4.2\n Define palindrom")
s = input("Input tuor phraise - ", )

if s[0:len(s)] == s[::-1]:
    print(s, "is palindrome")
else:
    print(s, "is NOT palindrome")