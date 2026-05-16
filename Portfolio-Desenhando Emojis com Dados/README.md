📊 Manipulador de Matrizes Complexas e Dados Estruturados

## 📝 Descrição do Projeto
Este projeto consiste em um motor de processamento lógico de estruturas de dados aninhadas e matrizes multidimensionais. O objetivo principal é consolidar conceitos avançados de iteração múltipla, manipulação de coleções imutáveis e álgebra linear computacional pura. 

Desenvolvido como parte das disciplinas do curso de **Análise e Desenvolvimento de Sistemas (2026.1)**, o sistema processa coleções aninhadas de forma performática sem o uso de dependências externas. Ele resolve dois problemas práticos específicos:
1. **Processamento Digital de Imagens (Filtro de Brilho):** Varre grades bidimensionais que representam mapas de pixels RGB, aplicando operações aritméticas diretas em tuplas de cores para gerar efeitos de sombreamento.
2. **Transposição de Matrizes de Áudio (Frequências Musicais):** Aplica conceitos de álgebra linear para realizar o espelhamento diagonal (transposição) de frequências sonoras estruturadas em dicionários, invertendo linhas e colunas puramente através de loops lógicos indexed-based.

---

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Paradigmas:** Programação Estruturada e Manipulação de Dados Puros
* **Recursos Core:** Loops aninhados (`for`), dicionários dinâmicos, ordenação indexada e mapeamento de tuplas imutáveis.

---

## 📊 Resultados e Aprendizados
O projeto obteve sucesso integral na validação de dados em ambiente de desenvolvimento local, trazendo insights fundamentais sobre o custo computacional de loops em profundidade:

* **Manipulação Limpa:** Sucesso no algoritmo de transposição sem utilizar métodos utilitários embutidos como `zip()` ou bibliotecas pesadas como o `NumPy`.
* **Gerenciamento de Imutabilidade:** Implementação de soluções contornando a natureza imutável das estruturas nativas do Python (como a recriação dinâmica de tuplas RGB modificadas).
* **Estruturação de Dados Complexos:** Domínio prático em navegação por 3 níveis de profundidade de objetos estruturados (`Dicionário -> Lista -> Dicionário -> Tupla/Matriz`).
