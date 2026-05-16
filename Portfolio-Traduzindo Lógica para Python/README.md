# 📊 Core Business Suite: Inteligência de Negócios e Governança de TI

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Curso](https://img.shields.io/badge/Curso-Gest%C3%A3o%20da%20TI-orange.svg)]()
[![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen.svg)]()

## 📖 Sobre o Projeto

Este projeto consolida uma suíte corporativa de scripts desenvolvidos como parte das atividades práticas do curso de **Gestão da Tecnologia da Informação**. O objetivo é aplicar a lógica de programação em Python para resolver problemas reais de tomada de decisão gerencial, cobrindo o planejamento tributário, auditoria de balanços, regras de governança de Recursos Humanos, automação comercial e análise estatística visual.

A coleção de ferramentas demonstra como a TI atua de forma transversal dentro de uma organização, otimizando processos financeiros, operacionais e estratégicos.

---

## 🚀 Módulos Integrados e Regras de Negócio

### 1. Planejamento Tributário Internacional
* **Funcionalidade:** Simula a incidência de alíquotas fiscais de diferentes nações (Alemanha, Brasil, EUA, Reino Unido, Japão) sobre insumos, permitindo cálculos em cascata para prever o custo de importação e precificação.

### 2. Análise de DRE (Demonstração do Resultado do Exercício)
* **Funcionalidade:** Automatiza o cálculo do **Lucro Operacional** e do **Lucro Líquido** deduzindo custos fixos, variáveis, despesas operacionais e tributos, confrontando o resultado final com a meta de lucro estipulada pela diretoria.

### 3. Matriz de Elegibilidade e Recursos Humanos
* **Funcionalidade:** Engine de regras que analisa o tempo de experiência e avaliação de desempenho para promoções, contendo uma regra *Hard-Stop* (bloqueio impeditivo imediato caso o colaborador esteja cumprindo aviso prévio).

### 4. Frente de Caixa Inteligente (PDV) com Descontos Progressivos
* **Funcionalidade:** Processa as vendas do dia e aplica gatilhos automáticos de descontos baseados em volume (5% para compras acima de R$ 200,00 e 10% para compras que ultrapassam R$ 500,00), validando entradas para impedir inconsistências físicas (valores negativos ou zerados).

### 5. Simulador de Ativos e Previdência (Juros Compostos)
* **Funcionalidade:** Executa projeções financeiras mês a mês considerando aportes variáveis e aplicação de juros capitalizados sobre o saldo acumulado, disparando alertas automáticos de conquistas quando metas parciais (ex: R$ 10.000,00) são alcançadas.

### 6. Sistema de Controle Acadêmico e Desempenho de Equipes
* **Funcionalidade:** Consolida médias ponderadas de notas, gerando saídas estruturadas com base em limites de corte para classificação automática em: Aprovado, Recuperação ou Reprovado.

### 7. Engine Analítica e Plotagem Estatística
* **Funcionalidade:** Integração com as bibliotecas `numpy` e `matplotlib` para gerar visualizações e relatórios estatísticos de amostragem aleatória com áreas de preenchimento condicional em conformidade com o ecossistema Data Science.

---

## 🧠 Arquitetura e Engenharia de Software

O código foi padronizado utilizando boas práticas de desenvolvimento:
* **Sanitização de Inputs:** Tratamento dinâmico de strings nas capturas de dados operacionais (uso do `.replace(',', '.')` e `.lower()`) garantindo resiliência contra falhas humanas na digitação.
* **Tipagem Conversora Dinâmica:** Uso rigoroso de coerção de tipos (`float()` e `int()`) antes do processamento aritmético para evitar distorções de cálculo por inferência ambígua.
* **Componentização por Funções:** Divisão do código em blocos isolados e reutilizáveis (funções independentes), permitindo escalabilidade e facilidade na manutenção dos microsserviços gerenciais.

---

## 💻 Estrutura do Repositório

O projeto está centralizado em módulos limpos de execução:

```python
# Exemplo de lógica de proteção de entrada e tomada de decisão contida no sistema
def processar_vendas():
    total_compra = 0.0
    itens_comprados = 0
    quantidade_tipos = int(input("Quantos produtos diferentes foram comprados? "))

    for i in range(1, quantidade_tipos + 1):
        nome = input(f"\nNome do produto {i}: ")
        preco = float(input("Preço unitário: "))
        qtd = int(input("Quantidade deste produto: "))

        if preco <= 0 or qtd <= 0:
            print(f"Erro: Valores inválidos para {nome}")
        else:
            total_compra += (preco * qtd)
            itens_comprados += qtd

    # Escalonamento de Desconto
    if total_compra > 500.00:
        total_final = total_compra * 0.90
    elif total_compra > 200.00:
        total_final = total_compra * 0.95
    else:
        total_final = total_compra
