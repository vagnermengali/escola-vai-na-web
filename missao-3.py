nota = float(input("Digite a nota do aluno: "))

if 90 <= nota <= 100:
    print("Parabéns, você tirou A!")
elif 80 <= nota < 90:
    print("Muito bem, você tirou B.")
elif 70 <= nota < 80:
    print("Bom trabalho, você tirou C.")
elif 60 <= nota < 70:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")
