year = int(input("Digite um ano: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"o ano {year} ele e bissexto")
else:
    print(f"O ano {year} ele nao e bissexto")