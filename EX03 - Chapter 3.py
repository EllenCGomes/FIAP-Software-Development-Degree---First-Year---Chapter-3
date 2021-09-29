# recebe quantos alimentos foram consumidos no dia
alimentos_consumidos = int(input("Por favor, digite quantos alimentos foram consumidos hoje: "))
# total inicial
total_calorias = 0

# recebe quantas calorias possui cada alimento do total consumido
for i in range(1, (alimentos_consumidos+1)):
    calorias_alimento = int(input("Quantas calorias possui o alimento {} ? ".format(i)))
    # calcula total de calorias
    total_calorias = total_calorias + calorias_alimento
print("O total de calorias consumidas no dia foi de {} kcal".format(total_calorias))
