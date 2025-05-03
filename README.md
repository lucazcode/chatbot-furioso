# FURIOSO Chatbot 😼

Um chatbot focado no time de CS da FURIA, capaz de classificar entradas de usuário, realizar scraping de informações da HLTV.org e responder perguntas diversas sobre o time de forma interativa e divertida.

---

## 📋 Sumário

* [Visão Geral](#visão-geral) ✨
* [Deploy](#deploy) 🚀
* [Scraping de dados](#scraping-de-dados) 📝
* [Fallback](#fallback) 🤖
* [Arquitetura](#arquitetura) 🏗️
* [Logging Estruturado](#logging-estruturado)🐞
* [Limitações](#limitações) 🚧
* [Pré-requisitos](#pré-requisitos) 📦
* [Instalação](#instalação) 💻
* [Uso](#uso) ▶️
* [Deploy](#deploy) ☁️
* [Contribuição](#contribuição) 🤝
* [Autor](#autor) 🧠

---

## Visão Geral ✨

O **FURIOSO Chatbot** é uma aplicação Python que:

* 🎯 Classifica entradas de usuário em diferentes intents (`question` ou `commentary` e categorias como `factual_request`, `opinion_request`, `commentary_request`).
* 😁 Responde de forma interativa as mensagens do usuário, com diversas possibilidades disponíveis.
* 📝 Realiza scraping de dados na HLTV.org caso necessário.
* 🤖 Possui um sistema de fallback para mensagens fora do escopo ou sem dados disponíveis.
* 📊 Registra logs estruturados para facilitar debug.
* 🌐 Pode ser executado localmente via Streamlit.

---

## Deploy 🚀

O projeto está disponível online via Streamlit:

👉 [Acesse o Chatbot FURIOSO](https://chatbot-furioso.streamlit.app/)

---

## Scraping de dados 📝

Quando a mensagem do usuário é categorizada como uma pergunta e indentificada com intent `factual_request`, o método de extração de informações por scraping é ativado.

* **Scraping Detalhado**: coleta via HLTV.org as informações:

  * 📅 Data, horário e adversário da próxima partida (`extract_next_match_date_time`, `extract_next_match_opponent`).
  * 🏃‍♂️ Jogadores e links dos perfis (`extract_players`, `extract_players_links`).
  * 🎓 Treinador e link do perfil (`extract_coach`, `extract_coach_link`).
  * 🏟️ Campeonatos em andamento (`extract_championships`).
  * 🔄 Formato e fase da próxima partida (`extract_next_match_format_and_stage`).
  * 🥇 Últimos resultados (`extract_last_matches_score`).

Caso o scraping falhe em extrair os dados, o sistema de fallback é executado.

---

## Fallback 🤖

Quando o chatbot não encontra os dados solicitados na HLTV.org, ele utiliza respostas de fallback para manter a interação leve e informativa. Há três tipos de fallback:

1. **Respostas para perguntas sobre a FURIA ou CS onde o scraping não obteve dados**:
   O  chatbot retorna respostas contextualizadas que buscam fornecer direcionamento para informação oficial.

2. **Respostas para comentários sobre a FURIA ou CS**:
   O chatbot retorna respostas contextualizadas que buscam fornecer um diálogo divertido e interativo para o usuário.

3. **Respostas para comentários fora do contexto da FURIA ou CS**:
   O chatbot retorna respostas explicativas sobre o fato de não abordar assuntos fora do escopo.

---

## Arquitetura 🏗️
 
O fluxo pode variar de acordo com a entrada do usuário, mas a estrutura base principal do programa é a seguinte:

```text
Entrada do usuário → app → flux_control → ai_classification → ai_scraping_filter (situacional) → Resposta do chatbot
```

* **`app.py`**: interface Streamlit (campo de input e botão enviar).
* **`flux_control.py`**: recebe a mensagem e orquestra o fluxo de conversação e fallback.
* **`ai_classification.py`**: classifica input em `question` / `commentary`.
* **`ai_scraping_filter.py`**: mapeia texto para intents específicas.

> ℹ️ O módulo de scraping só é chamado quando a entrada do usuário for uma `question` com a intent `factual_request`.

---

## Logging Estruturado 🐞  
O sistema de logging foi criado para oferecer opcionalmente uma visão clara do que está acontecendo nos bastidores da aplicação diretamente no console.

## ✨ Como usar  
O log é opcional e fica desligado por padrão. Para habilitá-lo manualmente, basta chamar a função `enable_debug()` no seu código, como por exemplo no `manual_test.py`:

```python
# Habilita ou desabilita os logs no terminal (opcional)
enable_debug()
```

## 🔍 O que o log registra?  
- Fluxo das chamadas internas do chatbot (classificação de *intents*, scraping, etc.).  
- Erros e exceções com mensagens completas.  

## 📁 Onde configurar?  
Toda a lógica de logging está concentrada no arquivo `logger.py`, permitindo que seja facilmente ajustada ou integrada com ferramentas externas de monitoramento.

---

## Limitações 🚧

1. **Dependência da Estrutura da HLTV.org**:  
   O processo de scraping depende da estrutura atual do site HLTV.org. Se houver mudanças no layout ou na forma como as informações são organizadas, o chatbot pode deixar de funcionar corretamente. É recomendado acompanhar a [estrutura da HLTV](https://www.hltv.org/) ou realizar verificações periódicas para garantir que o sistema esteja funcionando corretamente.

2. **Limitações de Dados Disponíveis**:  
   Algumas informações podem não estar disponíveis no HLTV.org em tempo real, como a data e hora exata dos próximos jogos, ou detalhes sobre partidas futuras não anunciadas. O chatbot tenta fornecer as informações mais precisas possíveis, mas pode haver casos onde os dados não estão acessíveis.

3. **Foco Restrito ao CS e FURIA**:  
   O chatbot está focado exclusivamente em informações sobre o time da FURIA e o cenário de CS. Ele não pode fornecer respostas sobre outros jogos, equipes ou tópicos fora desse contexto. Se uma pergunta for feita fora desse escopo, o chatbot fornecerá uma resposta informando que não pode ajudar com o assunto.

4. **Possíveis Falhas no Scraping**:  
   Caso haja algum erro no processo de scraping (ex: falha na conexão, dados indisponíveis ou mudanças no site da HLTV), o chatbot irá tentar retornar uma resposta de fallback. No entanto, em casos mais críticos, pode ser necessário revisar os logs de erro ou atualizar os métodos de scraping. O sistema de logging estruturado ajuda a identificar e corrigir rapidamente esses problemas.

---

## Pré-requisitos 📦

* Python 3.11+
* `pip install -r requirements.txt`

---

## Instalação 💻

1. Clone o repositório:

   ```bash
   git clone https://github.com/lucazcode/furioso-chatbot.git
   cd furioso-chatbot
   ```
2. Crie e ative um virtualenv:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instale dependências:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Uso ▶️

Para rodar localmente com Streamlit:

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` no navegador e interaja com o chatbot.

---

## Deploy ☁️

Para publicar via Streamlit Community Cloud:

1. Crie um repositório público no GitHub e envie o código.
2. Acesse [https://share.streamlit.io](https://share.streamlit.io), faça login e clique em **"New app"**.
3. Selecione seu repositório, branch (`main`) e arquivo de inicialização (`app.py`).
4. Clique em **"Deploy"** e aguarde a publicação.

---

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

1. Fork este repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/xyz`).
3. Abra um Pull Request.

---

## Autor 🧠

Projeto desenvolvido por @lucazcode.
