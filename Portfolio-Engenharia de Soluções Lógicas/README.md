# 🌾 Automação e Auditoria de Irrigação Inteligente (Python)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Curso](https://img.shields.io/badge/Curso-Gest%C3%A3o%20da%20TI-orange.svg)]()
[![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen.svg)]()

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte das atividades práticas do curso de **Gestão da Tecnologia da Informação**. O objetivo do sistema é automatizar o processo de irrigação agrícola através do monitoramento contínuo de sensores de umidade do solo e fluxo de água. 

A solução foca em conceitos fundamentais de **Governança de TI, IoT (Internet das Coisas) e Compliance Ambiental**, garantindo a otimização de recursos hídricos, mitigação de riscos operacionais (como vazamentos) e fornecendo alertas em tempo real caso haja anomalias no consumo de insumos.

## 🚀 Funcionalidades

* **Monitoramento Contínuo:** Loop contínuo de varredura (*polling*) dos sensores de umidade e fluxo hídrico.
* **Inteligência de Processos:** Cálculo dinâmico do volume de água necessário com base no deficit atual de umidade do solo.
* **Mitigação de Riscos (Fail-Safe):** Interrupção automática da irrigação e emissão de alertas estruturados caso a vazão ultrapasse os limites de segurança configurados.
* **Automação Eficiente:** Desligamento inteligente assim que o solo atinge o nível ideal de umidade, evitando desperdício de energia e recursos naturais.

## 🛠️ Tecnologias e Conceitos Aplicados

A arquitetura do algoritmo simula a lógica de sistemas embarcados e foi projetada utilizando conceitos de boas práticas de desenvolvimento:

* **Arquitetura de Sistemas de Controle:** Estruturação de loops de monitoramento em tempo real (`ENQUANTO SISTEMA ATIVO`).
* **Lógica Condicional e Parametrização:** Definição de constantes de governança (`Umidade_IDEAL = 60` e `LIMITE_FLUXO = 70`) para tomada de decisão dinâmica.
* **Tratamento de Exceções Operacionais:** Implementação de regras de negócio *Hard-Stop* para cenários de incidentes críticos (vazamento ou vazão acima do limite).

---

## 🧠 Lógica e Estrutura do Código

### Mapeamento do Fluxo de Processos (BPMN / Fluxograma)
O fluxo operacional mapeado para o sistema segue uma ordem lógica estrita de validação de dados:
1. **Início e Captura:** Inicialização e leitura dos sensores de campo.
2. **Tomada de Decisão Principal:** Avaliação se o solo necessita de água (comparativo com a umidade ideal). Se não precisar, o sistema permanece em monitoramento.
3. **Ativação e Controle:** Caso necessite, calcula-se a quantidade de água e liga-se o fluxo de irrigação.
4. **Auditoria de Vazão:** Durante a irrigação, se o fluxo d'água ultrapassar o limite seguro, o sistema emite um alerta de anomalia e força o desligamento imediato do hardware por segurança.

### O Algoritmo Estruturado (Pseudocódigo)
```pascal
Inicio
    // Definições iniciais de Governança
    definir Umidade_IDEAL = 60
    definir LIMITE_FLUXO = 70
    
    LOOP Continuo de monitoramento
    ENQUANTO SISTEMA ATIVO FAÇA
        LER Umidade-Solo
        LER FLUXO-AGUA
        
        SE UMIDADE-SOLO == Umidade_IDEAL ENTÃO
            DESLIGAR IRRIGAÇÃO()
        SENÃO
            CALCULAR QUANTIDADE_AGUA()
            LIGAR IRRIGAÇÃO()
            
            // Loop de Auditoria e Segurança Ativa
            ENQUANTO IRRIGAÇÃO-ATIVA FAÇA
                LER FLUXO-AGUA
                LER UMIDADE-SOLO
                
                SE FLUXO-AGUA > LIMITE_FLUXO ENTÃO
                    EMITIR ALERTA "POSSIVEL desperdicio ou VAZAMENTO"
                    DESLIGAR IRRIGAÇÃO()
                    PARAR
                FIMSE
            FIMENQUANTO
        FIMSE
    FIMENQUANTO
FIM
