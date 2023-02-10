print("ДЗ7. Урок 4.\n Вивести середину рядка")
s = input("Input yor text")
a = len(s)

if a % 2 == 1:
    print("Midle of yor text symbols -", s[a//2])
else:
    print("Midle of yor text symbols -", s[a//2-1: a//2+1])