🐍 Fundamentos de Programação em Python
📝 Descrição do Projeto
Este projeto reúne os exercícios e práticas desenvolvidos ao longo das primeiras aulas da disciplina de Programação — Computadores (UNICID), como parte do curso de Gestão da Tecnologia da Informação. O objetivo central é construir uma base sólida em lógica de programação utilizando Python, partindo dos conceitos mais essenciais até a criação de sistemas com regras de negócio reais.
As atividades evoluem progressivamente: começando pela estrutura básica de um programa (print, condicionais, variáveis), passando por cálculos práticos como média escolar, IMC e conversão de temperatura, até chegar a um sistema de análise de vendas com detecção de anomalias — projeto mais robusto que simula uma lógica de auditoria financeira com funções, variáveis globais e tratamento de exceções.
O projeto também registra descobertas conceituais importantes, como o impacto de discrepâncias nos dados sobre médias, os riscos do uso de global em sistemas críticos e a importância da normalização de dados para sistemas mais confiáveis.
🚀 Tecnologias Utilizadas

Linguagem: Python 3.x
Ambiente: Google Colab / Jupyter Notebook
Conceitos aplicados: Variáveis, casting, condicionais, funções, escopo global, tratamento de exceções (try/except), formatação de strings com f-strings

📊 Resultados e Aprendizados
O projeto consolidou fundamentos essenciais para o desenvolvimento de sistemas reais.

Sistema de Análise de Vendas: Desenvolvi um programa que detecta automaticamente anomalias em registros financeiros, simulando a lógica de auditoria de um sistema bancário.
Lógica de Negócio na Prática: Aprendi que um limiar de alerta mal calibrado (ex: 5x a média) pode deixar passar valores suspeitos — e que ajustá-lo para 2.5x torna o sistema significativamente mais seguro.
Riscos do uso de global: Compreendi que variáveis globais em sistemas críticos representam uma vulnerabilidade real, pois permitem alterações sem rastreamento — o padrão profissional exige encapsulamento e auditoria.
Tratamento de Erros: Implementei try/except para garantir que entradas inválidas do usuário não quebrem o fluxo do programa.
Debugging por Intuição: Desenvolvi a percepção de identificar erros como UnboundLocalError antes mesmo de ler a mensagem — reconhecendo padrões visuais no editor e no comportamento do código.

🔧 Como Executar

Acesse o Google Colab ou abra o arquivo em um ambiente Jupyter.
Faça upload do arquivo .ipynb ou abra diretamente pelo link do Colab.
Execute as células sequencialmente com Shift + Enter.
Para os exercícios interativos (média, IMC, vendas), insira os valores solicitados nos campos de input().
