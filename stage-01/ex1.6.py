# nota1 = input("Nota 1: ") # Erro 1: Essa linha armazena str onde se pretende armazena numero (falta coversao)
# nota2 = input("Nota 2: ") # Erro 2: Essa linha armazena str onde se pretende armazena numero (falta coversao)
# media = nota1 + nota2 / 2 # Erro 3: Operacao aritmetica nao suportada e falha na precedencia.
# if media >= 10            # Erro 4: Falta os dois pontos (:) para indicar o inicio do bloco if

# codigo corrigido:
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
if media >= 10:
    print("Aprovado")
else:
    print("Reprovado")
