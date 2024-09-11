def verificar_letra_a(string):
    string = string.lower()
    count_a = string.count('a')
    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes."
    else:
        return "A letra 'a' não foi encontrada."

texto = input("Informe uma string: ")
print(verificar_letra_a(texto))
