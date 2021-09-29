# recebe valor do usuario
valor = int(input("Digite um valor numerico inteiro: "))
# um dos dois numeros anteriores a ser somado
ultimo = 1
# um dos dois numeros anteriores a ser somado
penultimo = 0
# soma inicial
soma = 0
# valor ainda nao foi encontrado
nao_encontrado = True

# calcula a sequencia de Fibonnaci
while soma <= valor:
    soma = ultimo + penultimo
    ultimo = penultimo
    penultimo = soma
    # verifica se o valor foi encontrado
    if soma == valor:
        nao_encontrado = False
if not nao_encontrado:
    print("Acao bem sucedida!")
else:
    print("A acao falhou...")
