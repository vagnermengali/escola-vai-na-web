def contar_letras(nome):
    return len(nome)

nome = input("Digite um nome: ")
print(f"O nome {nome} tem {contar_letras(nome)} letras.")
