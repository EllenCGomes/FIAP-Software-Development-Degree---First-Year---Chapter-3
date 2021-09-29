# recebe quantas transacoes financeiras foram realizadas no dia
transacoes_realizadas = int(input("Por favor, digite quantas transacoes financeiras foram realizadas hoje: "))
# soma inicial
soma_transacoes = 0

# recebe valor de cada transacao financeira
for i in range(1, (transacoes_realizadas+1)):
    cada_transacao = float(input("Qual o valor da transacao financeira {} ? ".format(i)))
    # calcula total de transacoes financeiras
    soma_transacoes = soma_transacoes + cada_transacao
# calcula a media do valor de cada transacao
media_transacoes = soma_transacoes/transacoes_realizadas
print("O valor total gasto no dia foi de R$ {:.2f} e a media do valor de cada transacao foi de R$ {:.2f}".format(
    soma_transacoes, media_transacoes))
