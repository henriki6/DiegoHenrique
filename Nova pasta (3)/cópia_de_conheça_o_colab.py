
TAXA_IMPOSTO_EU = 0.08
TAXA_IMPOSTO_REINO_UNIDO = 0.20
TAXA_IMPOSTO_ALEMANHA = 0.19
TAXA_IMPOSTO_JAPÃO = 0.10
TAXA_IMPOSTO_BRASIL = 0.30



def calcular_preco_total(preco_produto, taxa_imposto):
  return preco_produto * (1 + taxa_imposto)

peco_gasolina = 4.50

preco_g_alemanha = calcular_preco_total(peco_gasolina, TAXA_IMPOSTO_ALEMANHA)
preco_g_brasil = calcular_preco_total(preco_g_alemanha, TAXA_IMPOSTO_BRASIL)
preco_g_eua = calcular_preco_total(peco_gasolina, TAXA_IMPOSTO_EU)
print(f"preço da gasolina na alemanha: $ {preco_g_alemanha:.2f}")
print(f"preço da gasolina no brasil: $ {preco_g_brasil:.2f}")
print(f"preço da gasolina nos EUA: $ {preco_g_eua:.2f}")

# Calcular o lucro total de uma empresa e ver se ela atingiu o valor total do
receita_total = float(input("Digitar a receita total: "))
custos_fixos = float(input("Digitar os custos fixos: "))
impostos = float(input("Digitar os impostos: "))
despesas_operacionais = float(input("Digitar as desepesas operacionais: "))
meta_lucro = float(input("Digitar a meta de lucro: "))

# Calculos
def calcular_lucro_total(receita_total, custos_fixos):
  return receita_total - custos_fixos

# lucro operacional e igual a lucro bruto menos desespesas operacionais
lucro_operacional = calcular_lucro_total(receita_total, custos_fixos) - despesas_operacionais
# lucro liquido e igual ao lucro operacional menos os impostos
lucro_liquido = lucro_operacional - impostos

print(f"Lucro Operacional: $ {lucro_operacional:.2f}")
print(f"Lucro Líquido: $ {lucro_liquido:.2f}")

if lucro_liquido >= meta_lucro:
    print("A empresa atingiu a meta de lucro!")
else:
    print("A empresa não atingiu a meta de lucro.")

# vamos criar um codigo para verificar se um funcionario pode ser promovido com base em na experiencia, desempenho e estatos de aviso previo.

def verificar_alegibilidade(anos_exp, nota, aviso_prev):
    EXP_MINIMA = 3
    NOTA_MINIMA = 8.0

    # 1 Regra impeditiva
    if aviso_prev:
        return "Você esta em aviso previo. Nao e elegivel para a promoçao."
    # 2 Elegibilidade Total
    if anos_exp >= EXP_MINIMA and nota >= NOTA_MINIMA:
        return "Você e elegivel para a promoçao."
    # 3 feedbeck para quem deixou de atingir um dos creditos
    if anos_exp >= EXP_MINIMA:
        return "Seu desempenho nao atingiu o nivem minimo para aprovaçao"
    if nota >= NOTA_MINIMA:
        return "Voce precisa de mais experiencia para conseguir a aprovaçao"

    return "Voce nao e elegivel para a promoçao"

# FAzer os input
anos = int(input("Digite a quantidade de anos de experiencia: "))
nota = float(input("Digite a nota do desempenho: "))
aviso_prev = input("Esta de aviso previo (s ou n): ")
if aviso_prev.lower() == 's':
    aviso = True
else:
    aviso = False

def processar_venda():
    total_compra = 0.0
    itens_comprados = 0

    quantidade_tipos = int(input("Quantos produtos diferentes foram comprados: "))
    for i in range(quantidade_tipos):
        nome = input("nome do produto: ")
        preço = float(input("Preço unitario: "))
        qtd = int(input("Quantidade do produto: "))
        if preço <= 0.0 or qtd <= 0:
            print(f"Erro: Valores invalidos para o produto {nome}")
        else:
            subtotal = preço * qtd
            total_compra += subtotal
            itens_comprados += qtd

    if total_compra > 500.00:
        total_final = total_compra * 0.90
        print("Desconto de 10% aplicado")
    elif total_compra >= 200.00:
        total_final = total_compra * 0.95
        print("Desconto de 5% aplicado")
    else:
        total_final = total_compra
    print(f"Resumo: {itens_comprados} itens. Total a pagar:R$ {total_final:.2f}")

processar_venda()

def simulador_poupanca():



    print("Valor inicial do investimento:")



    saldo = float(input())



    print("Taxa de juros mensal (em %):")



    taxa = float(input())



    print("Número de meses da simulação:")



    meses = int(input())



    for m in range(1, meses + 1):



        print("Quanto deseja depositar no mês ", m, "? (0 para nenhum)")



        aporte = float(input())



        saldo = saldo + aporte



        juros = saldo * (taxa / 100)



        saldo = saldo + juros



        print("Mês ", m, ": Saldo atualizado = R$", saldo)



        if saldo > 10000.0:



            print("Parabéns! Você atingiu a meta de 10k no mês ", m)



    print("Resultado final após ", meses, " meses: R$", saldo)

def sistema_notas_turma():
    print("Quantos alunos existem na turma?")
    total_alunos = int(input())

    for j in range(1, total_alunos + 1):
        print("\nNome do aluno:")
        aluno_nome = input()

        print("Nota 1:")
        n1 = float(input())

        print("Nota 2:")
        n2 = float(input())

        media_aluno = (n1 + n2) / 2

        if media_aluno >= 7.0:
            print(f"{aluno_nome}: Aprovado com média {media_aluno:.2f}")
        elif media_aluno >= 5.0:
            print(f"{aluno_nome}: Recuperação (Média: {media_aluno:.2f})")
        else:
            print(f"{aluno_nome}: Reprovado")


# Executar função
sistema_notas_turma()



def processar_vendas():
    total_compra = 0.0
    itens_comprados = 0

    # Convertendo para int para garantir que o range funcione
    quantidade_tipos = int(input("Quantos produtos diferentes foram comprados? "))

    # range(1, x + 1) para contar de 1 até o número exato digitado
    for i in range(1, quantidade_tipos + 1):
        nome = input(f"\nNome do produto {i}: ")

        # Usando float() para preços e int() para quantidades
        preco = float(input("Preço unitário: "))
        qtd = int(input("Quantidade deste produto: "))

        if preco <= 0 or qtd <= 0:
            print(f"Erro: Valores inválidos para {nome}")
        else:
            subtotal = preco * qtd
            total_compra += subtotal
            itens_comprados += qtd

    # Lógica de descontos
    if total_compra > 500.00:
        total_final = total_compra * 0.90  # 10% de desconto
        print("Desconto de 10% aplicado!")
    elif total_compra > 200.00:
        total_final = total_compra * 0.95  # 5% de desconto
        print("Desconto de 5% aplicado!")
    else:
        total_final = total_compra

    print(f"\nResumo: {itens_comprados} itens. Total a pagar: R${total_final:.2f}")

# Chama a função para executar
processar_vendas()





import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)
