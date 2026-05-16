# 📊 Sistema de Auditoria de Dados e Compliance Financeiro (Python)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Curso](https://img.shields.io/badge/Curso-Gest%C3%A3o%20da%20TI-orange.svg)]()
[![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen.svg)]()

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte das atividades práticas do curso de **Gestão da Tecnologia da Informação**. [cite_start]O objetivo do sistema é analisar fluxos de vendas diárias para identificar discrepâncias operacionais (*outliers*) e aplicar protocolos de segurança (como o estado de "Quarentena") quando anomalias são detectadas[cite: 207, 248, 249].

[cite_start]O projeto vai além da simples codificação, integrando conceitos essenciais de **Auditoria Financeira, Materialidade e Engenharia de Software Seguro**, avaliando os riscos do uso de variáveis globais no gerenciamento de regras de negócios críticas[cite: 216, 219, 262, 263].

## 🚀 Funcionalidades e Conceitos de Auditoria

* [cite_start]**Identificação de Outliers:** Análise de valores que se destacam drasticamente da média, evitando a distorção da realidade financeira por falhas técnicas ou eventos atípicos[cite: 207, 208, 213].
* [cite_start]**Gatilhos de Compliance (Quarentena):** Monitoramento automatizado focado em colocar o sistema em alerta caso a média de transações ultrapasse o `LIMITE_SEGURANCA` estabelecido[cite: 224, 248, 249].
* [cite_start]**Análise de Materialidade e Margem de Tolerância:** Foco nos três pilares da auditoria moderna: Custo-Benefício da Investigação, Materialidade e mitigação do Risco de Amostragem[cite: 216, 217, 218, 219, 221].

---

## 🛠️ O Perigo da Variável Global (Análise de Segurança)

[cite_start]Um dos pontos centrais de estudo deste projeto foi a segurança do código[cite: 262]. [cite_start]No script inicial, a palavra-chave `global LIMITE_SEGURANCA` foi utilizada para permitir ajustes no teto de checagem[cite: 241, 250]. 

### A Vulnerabilidade
[cite_start]No contexto de **Engenharia de Software Bancário**, o uso de variáveis globais expõe o sistema a sérios riscos[cite: 263]:
1. [cite_start]**Exposição de Memória:** Variáveis globais residem na memória compartilhada[cite: 264]. [cite_start]Qualquer função mal escrita ou um script malicioso injetado pode alterar esse limite para um valor infinito, permitindo transações fraudulentas sem disparar alertas[cite: 264].
2. [cite_start]**Falhas de Escopo:** Esquecer a declaração `global` faz com que o Python tente criar uma variável local, gerando erros de execução e comportamentos inesperados (travamentos)[cite: 266, 267].

### Boas Práticas de TI Aplicadas
[cite_start]Em sistemas corporativos reais, esses parâmetros devem ser **Encapsulados** dentro de classes privadas ou consultados dinamicamente através de um serviço externo de configuração com autenticação rígida[cite: 265]. [cite_start]Quem processa a transação **nunca** deve ter o poder de alterar as regras de validação sem deixar trilhas de auditoria (*logs*)[cite: 265].

---

## 🧠 Lógica e Estrutura do Algoritmo

### O Script de Auditoria
[cite_start]Abaixo está a implementação lógica estruturada para a captura de dados e verificação de estresse das vendas diárias[cite: 222, 229]:

```python
# Configuração de Governança
LIMITE_SEGURANCA = 10000.00
print(f"Limite de Segurança inicial: R$ {LIMITE_SEGURANCA:,.2f}")

vendas = []

# Input Seguro de Dados com Tratamento de Erros
for i in range(1, 4):
    while True:
        try:
            valor_venda = input(f"Digite o valor da venda {i} do dia (ex: 1234.56): ").replace(',', '.')
            vendas.append(float(valor_venda))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

venda1, venda2, venda3 = vendas[0], vendas[1], vendas[2]

def analisar_vendas(v1, v2, v3):
    global LIMITE_SEGURANCA  # Permite a alteração da variável (Atenção: Risco de Segurança!)
    
    print("\n--- Análise de Vendas ---")
    media = (v1 + v2 + v3) / 3
    print(f"Média das vendas: R$ {media:,.2f}")
    
    # Lógica de Investigação e Compliance
    if media > LIMITE_SEGURANCA:
        print("ALERTA: SISTEMA EM QUARENTENA!")
    
    # Sugestão de ajuste com base na volatilidade (Gatilho de 50% acima do limite)
    if any(v > LIMITE_SEGURANCA * 1.5 for v in [v1, v2, v3]):
        print("Sugestão: Vendas individuais muito altas. Considere ajustar o LIMITE_SEGURANCA se forem legítimas.")

# Execução do Teste
analisar_vendas(venda1, venda2, venda3)
