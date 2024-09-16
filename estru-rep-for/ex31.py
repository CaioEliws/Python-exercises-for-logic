numbers = [3, 5, 1, 10, -2]

primary = float('-inf') # (-inf) Inicializa com o menor valor possivel
secundary = float('-inf') # (-inf) Inicializa com o menor valor possivel

for num in numbers:
    if num > primary:
        secundary = primary
        primary = num
    elif num > secundary and num < primary:
        secundary = num
    

print(f"O maior número é: {primary}")
print(f"O segundo maior número é: {secundary}")