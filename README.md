# 🌪️ Chaos App - LGTM Stack Validator

Uma aplicação desenvolvida em Python com o propósito de atuar como um agente de *Chaos Engineering*. O objetivo primário desta ferramenta é injetar falhas, estressar recursos e gerar telemetria imprevisível para validar a eficácia de pilhas de observabilidade modernas, especificamente a stack **LGTM (Loki, Grafana, Tempo, Mimir)**.

## 🎯 Por que este projeto existe?
Em arquiteturas distribuídas e orquestradas pelo Kubernetes, não basta ter o monitoramento instalado; é preciso garantir que ele reaja quando o caos acontece. Este app simula os piores cenários de produção de forma controlada.

## ⚙️ Funcionalidades (Simulações)

*(Nota: Ajuste esta lista conforme as rotas/funções que você criou no seu código)*

* **🔥 CPU Spike:** Simula um loop pesado para testar os alertas de CPU do Node Exporter e cAdvisor.
* **💧 Memory Leak:** Aloca memória de forma contínua até o limite do container para disparar eventos de *OOM (Out of Memory)* no Kube-state-metrics.
* **🚨 Log Flood:** Gera milhares de logs de erro em milissegundos para testar a taxa de ingestão e indexação do Loki.
* **🐛 HTTP 500 Generator:** Rotas que retornam erros intermitentes para visualização de taxas de erro no Grafana.
* **🕸️ Trace Delay (Tempo):** Adiciona latência artificial (sleeps) em rotas específicas para validar a rastreabilidade (traces) e gargalos de performance.

## 🚀 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/chaos-app.git](https://github.com/SEU-USUARIO/chaos-app.git)
   cd chaos-app
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Execute a aplicação:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python app.py
   ```

🐳 Deploy no Kubernetes (K3s)
Para testar a stack LGTM de forma real, a aplicação deve rodar dentro do cluster.

1. Construa a imagem Docker:
   ```bash
   docker build -t chaos-app:v1 .
   ```
2. Aplique o manifesto de deploy (exemplo):
   ```bash
   kubectl apply -f k8s/deployment.yaml
   ```
📊 Instrumentação e Observabilidade
Esta aplicação foi projetada para expor métricas no formato /metrics para que o Grafana Alloy possa realizar o scrape. 
Os logs são emitidos em stdout/stderr para coleta automática via container logs.
