# 🤖 Chatbot Orquestrador de Atendimento ao Cliente com Rasa

-----

## 📄 Visão Geral

Este projeto apresenta um **chatbot orquestrador** desenvolvido com **Rasa Open Source** em **Python**. Ele foi projetado para atuar como um ponto de entrada inteligente para o atendimento ao cliente, sendo capaz de interpretar a intenção do usuário e **direcionar a conversa para diferentes subsistemas** (ou "setores") conforme a necessidade, como Vendas, Suporte Técnico ou Informações Gerais.

O objetivo principal é demonstrar a arquitetura de orquestração de chatbots, onde um agente principal coordena e encaminha as requisições para módulos especializados, otimizando a experiência do usuário e a eficiência do atendimento.

-----

## ✨ Funcionalidades

  * **Reconhecimento de Intenção:** Utiliza o NLU do Rasa para entender o que o usuário deseja.
  * **Orquestração Inteligente:** Direciona a conversa para fluxos específicos (simulados) baseados na intenção detectada.
  * **Módulos de Atendimento:** Simula o encaminhamento para:
      * **Vendas:** Para dúvidas sobre produtos ou compras.
      * **Suporte Técnico:** Para problemas com produtos ou serviços.
      * **Informações Gerais:** Para perguntas sobre a empresa, horários, etc.
  * **Fallback Configurado:** Oferece uma resposta amigável quando a intenção do usuário não é compreendida, melhorando a robustez.

-----

## 🚀 Como Iniciar

Siga estes passos para configurar e executar o chatbot localmente.

### Pré-requisitos

Certifique-se de ter instalado:

  * **Python 3.10.x** (Recomendado para compatibilidade com o Rasa 3.x)
  * **Git**

### Instalação e Configuração

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO # Substitua pelo nome da pasta do seu projeto, e.g., chatbot_orquestrador
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

    ```bash
    # Crie o ambiente virtual usando Python 3.10
    python3.10 -m venv .venv

    # Ative o ambiente virtual (Windows)
    .\.venv\Scripts\activate

    # Ative o ambiente virtual (Linux/macOS)
    source ./.venv/bin/activate
    ```

3.  **Instale as Dependências:**
    Com o ambiente virtual ativo, instale o Rasa e o SDK de ações customizadas.

    ```bash
    pip install rasa rasa-sdk
    ```

4.  **Treine o Modelo do Rasa:**
    Este comando irá treinar o modelo de NLU e de diálogo do seu chatbot com base nos arquivos de dados (`data/`).

    ```bash
    rasa train
    ```

5.  **Inicie o Servidor de Ações Customizadas:**
    Em uma nova janela/aba do terminal (mantendo o ambiente virtual ativo), inicie o servidor para as ações customizadas definidas em `actions.py`.

    ```bash
    rasa run actions
    ```

6.  **Converse com o Chatbot:**
    Em outra janela/aba do terminal (com o ambiente virtual ativo), inicie o shell do Rasa para interagir com o chatbot.

    ```bash
    rasa shell
    ```

    Agora você pode digitar suas mensagens e testar o direcionamento.

-----

## 🧪 Testes

Para garantir que o chatbot se comporta como esperado, você pode executar os testes definidos em `tests/test_stories.yml`.

```bash
rasa test
```

Os resultados dos testes, incluindo relatórios de NLU e visualizações de diálogo, serão gerados na pasta `results/`.

-----

## 📁 Estrutura do Projeto

```
.
├── actions/                  # Código Python para ações customizadas do bot
│   └── actions.py
├── data/                     # Dados de treinamento do Rasa (NLU, Stories, Rules)
│   ├── nlu.yml               # Exemplos de intenções e entidades do usuário
│   ├── stories.yml           # Fluxos de conversa (diálogos) para treinamento
│   └── rules.yml             # Regras fixas de conversação
├── tests/                    # Histórias de teste para validação do bot
│   └── test_stories.yml
├── config.yml                # Configurações do pipeline de NLU e políticas de diálogo do Rasa
├── domain.yml                # Definição do "mundo" do bot (intenções, respostas, ações)
├── endpoints.yml             # Configuração para conectar o Rasa ao servidor de ações
└── .gitignore                # Arquivos e pastas a serem ignorados pelo Git
```

-----

## 🤝 Contribuição

Contribuições são bem-vindas\! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.

-----

## 📄 Licença

Este projeto está sob a licença [MIT License](https://opensource.org/licenses/MIT). (Você pode mudar isso se usar outra licença.)

-----

### Dicas para personalizar:

  * Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` no link de clone.
  * Adicione uma seção de `Requisitos` mais detalhada se houver outras dependências específicas do seu sistema.
  * Se você tiver planos futuros para o projeto, pode adicionar uma seção `Próximos Passos`.
  * Se você adicionar mais funcionalidades, atualize a seção `✨ Funcionalidades`.
