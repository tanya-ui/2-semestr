s = input("Введите слово на английском: ")
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)


