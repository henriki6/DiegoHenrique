# 🛒 Sistema de Automação Comercial e Otimização de Troco (PDV)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Curso](https://img.shields.io/badge/Curso-Gest%C3%A3o%20da%20TI-orange.svg)]()
[![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen.svg)]()

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte das atividades práticas do curso de **Gestão da Tecnologia da Informação**. [cite_start]O objetivo é simular as operações críticas de um **Ponto de Venda (PDV) corporativo**, dividindo a solução em três camadas modulares: registro de itens [cite: 121][cite_start], validação financeira de recebimento  [cite_start]e a lógica inteligente de otimização de fluxo de caixa para a dispensa de troco em cédulas.

[cite_start]A nível de gestão, o sistema implementa regras estritas de compliance financeiro (bloqueio de transações insuficientes)  [cite_start]e otimização de inventário físico de tesouraria (redução do número de notas emitidas por transação)[cite: 108, 150].

## 🚀 Funcionalidades Modulares

* [cite_start]**Módulo de Check-out (Registrar Compra):** Loop dinâmico que acumula valores de itens sucessivos até o fechamento da compra pelo operador[cite: 121, 134, 140].
* [cite_start]**Módulo de Auditoria de Recebimento:** Interface de validação que impede a finalização da venda se o valor pago em dinheiro for menor que o total devido, solicitando fundos adicionais[cite: 64, 65, 66, 92, 93].
* [cite_start]**Módulo Otimizador de Troco:** Algoritmo de divisão bancária que calcula e exibe a menor quantidade possível de notas (R$ 100, 50, 20, 10, 5, 2) necessárias para compor o troco do cliente[cite: 106, 108, 149, 150].

## 🛠️ Tecnologias e Conceitos Aplicados

* [cite_start]**Modularização de Processos (Microsserviços):** Separação da lógica de negócios em sub-rotinas interdependentes (Registro ➡️ Validação ➡️ Distribuição)[cite: 54, 104, 121].
* [cite_start]**Algoritmo Guloso (Greedy Algorithm):** Utilizado no motor de troco para priorizar sempre a maior cédula disponível, minimizando o volume físico de notas movimentadas[cite: 108, 150, 203].
* [cite_start]**Estrutura de Dados e Operadores Matemáticos:** Uso eficiente de arrays/listas para matrizes de moedas [cite: 106, 149] [cite_start]associados a operadores de divisão inteira e resto da divisão (`%`) para calcular a decomposição de valores[cite: 110, 113, 154].

---

## 🧠 Lógica e Estrutura do Código

O sistema foi mapeado a partir de matrizes de processos e estruturado nos seguintes pseudocódigos integrados:

### 1. Registro e Consolidação da Compra
[cite_start]Responsável por capturar a entrada de mercadorias por preço unitário até receber o comando de parada (`"N"`)[cite: 130, 131, 140].

```pascal
Algoritmo Registrar_Compra
Variáveis: Total_Compra, Preço_Item: Real; [cite_start]Continuar: Texto [cite: 122, 123, 124, 125]
Inicio
    [cite_start]Total_Compra = 0 [cite: 129]
    Repetir
        [cite_start]Escreva "Digite o preço do item:" [cite: 130]
        Leia Preço_Item [cite: 131]
        Total_Compra = Total_Compra + Preço_Item [cite: 134]
        Escreva "Deseja passar mais um item? (S/N)" [cite: 136, 137]
        Leia Continuar [cite: 138, 139]
    Até que Continuar == "N" [cite: 140]
    Retornar Total_Compra [cite: 141]
Fim [cite: 142]
