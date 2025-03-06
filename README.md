# 🤖 Chatbot com IA e WhatsApp

Este projeto é um chatbot que utiliza **Python, JavaScript e a API da OpenAI** para interagir com mensagens do WhatsApp. Ele recebe mensagens via **Venom-Bot** e processa respostas com **GPT**, armazenando os dados em um banco **MySQL** usando **SQLAlchemy**.

##  Tecnologias Utilizadas

### Backend (Python):
- SQLAlchemy 
- OpenAI API

### Integração com WhatsApp (JavaScript):

- Venom-Bot (para capturar e enviar mensagens)
### Banco de Dados:

- MySQL

### Comunicação entre Python e JavaScript:

- Arquivos JSON para troca de informações entre as linguagens

---

## 📂 Estrutura do Projeto

```
📦 projeto-chatbot
├── 📂 app
│   ├── 📂 database
│   │   ├── config.py          # Configuração do banco de dados
│   │   ├── database_info.py   # Manipulação de dados
│   ├── 📂 functions
│   │   ├── bot.js             # Lógica de interação com WhatsApp
│   │   ├── info.json          # JSON para comunicação entre serviços
│   │   ├── message.json       # JSON para troca de mensagens
│   ├── 📂 models
│   │   ├── ai_model.py        # Lógica de resposta usando IA
├── main.py                    # Arquivo principal do projeto
├── .env                        # Variáveis de ambiente
├── README.md                   # Documentação
```

---

##  Como Rodar o Projeto

###  Configuração do Banco de Dados

Certifique-se de ter um banco MySQL rodando e ajuste as credenciais em `config.py`.

###  Instalar Dependências (Python e JavaScript)

```bash
pip install -r requirements.txt  # Instalar dependências do Python
npm install venom-bot            # Instalar dependências do Node.js
```

###  Rodar o Servidor Python

```bash
python main.py
```

> O `main.py` inicia automaticamente o `bot.js` de forma assíncrona, então não é necessário rodar manualmente o script do bot.

---

## ⚙️ Funcionalidades

- Captura mensagens do WhatsApp
- Envia as mensagens para a API da OpenAI
- Processa respostas usando IA
- Retorna a resposta ao usuário via WhatsApp
- Armazena conversas no MySQL

---

## 📫 Contato

📎 [LinkedIn](https://www.linkedin.com/in/erick-il/)\
📂 [GitHub](https://github.com/Erick-IL)


