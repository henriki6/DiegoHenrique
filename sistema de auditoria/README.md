Aqui está o README atualizado para o novo projeto:

🔍 Sistema de Auditoria de Recursos
📝 Descrição do Projeto
Este projeto consiste em um sistema de auditoria de orçamento corporativo desenvolvido em Python, como parte do curso de Gestão da Tecnologia da Informação (UNICID). O objetivo é simular o controle financeiro de uma empresa com múltiplos departamentos, aplicando conceitos avançados de programação como decorators, recursividade e funções com argumentos dinâmicos.
O sistema percorre automaticamente a estrutura hierárquica de uma empresa (Matriz → Departamentos → Subáreas), calcula o orçamento total, permite ignorar departamentos específicos durante a auditoria e realiza a conversão de moeda em tempo real com base em uma taxa de câmbio informada. Toda execução é registrada pelo decorator @auditor, que funciona como um log automático — exibindo o nome da função chamada, os parâmetros utilizados e o tempo total de processamento.
🚀 Tecnologias Utilizadas

Linguagem: Python 3.x
Ambiente: Google Colab / Jupyter Notebook
Bibliotecas: time (nativa do Python)
Conceitos aplicados: Decorators (*args, **kwargs), funções recursivas, dicionários aninhados, controle de fluxo, formatação de saída, conversão de tipos

📊 Resultados e Aprendizados
O projeto demonstrou na prática como padrões profissionais de programação são aplicados em sistemas corporativos reais.

Decorator como sistema de log: Implementei um @auditor que intercepta qualquer função automaticamente, registrando parâmetros e tempo de execução — padrão utilizado em sistemas de compliance e rastreabilidade financeira.
Recursividade aplicada: A função navegar() percorre dicionários aninhados de qualquer profundidade, somando valores e respeitando filtros — tornando o sistema escalável para estruturas empresariais complexas.
Flexibilidade com *args e **kwargs: Aprendi a criar funções que aceitam parâmetros variáveis, permitindo ignorar departamentos dinamicamente e passar configurações como taxa de câmbio e moeda destino sem alterar a assinatura da função.
Simulação de regra de negócio real: O sistema executa uma auditoria completa ignorando o departamento de RH e converte o orçamento total de BRL para USD — simulando um fluxo real de relatório financeiro internacional.

🔧 Como Executar

Acesse o Google Colab ou abra o arquivo em um ambiente Jupyter.
Faça upload do arquivo .ipynb ou abra diretamente pelo link do Colab.
Execute todas as células sequencialmente com Shift + Enter.
Para personalizar, altere os departamentos a ignorar ou a taxa de câmbio na chamada final:

pythoncalcular_orcamento("RH", moeda_destino="USD", taxa_cambio=0.19)
