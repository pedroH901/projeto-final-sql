# Radar Pet 🐾

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

**Plataforma web para centralização de anúncios de animais perdidos e achados.**

[Acesse a Aplicação Online](https://link-para-seu-deploy.com) &nbsp;&nbsp;•&nbsp;&nbsp; [Reportar um Bug](https://github.com/gabriel-wav/RadarPet/issues)

Uma plataforma completa desenvolvida para ajudar a comunidade a reencontrar seus pets. O projeto conecta pessoas de forma rápida e eficiente, centralizando informações e promovendo o reencontro de animais com suas famílias.

![Demonstração do RadarPet](caminho/para/seu/gif_ou_screenshot.png)

## ✨ Funcionalidades Principais

* **Autenticação de Usuários:** Sistema completo de cadastro e login para gerenciamento seguro dos anúncios.
* **Gestão de Anúncios:** Formulário detalhado para anunciar pets, permitindo incluir espécie, raça, localização e fotos.
* **Galeria de Pets:** Painel principal com todos os anúncios em formato de cartões para visualização rápida e eficiente.
* **Página de Detalhes:** Visualização completa de cada anúncio, com todas as informações e a foto do pet em destaque.
* **Notificações Dinâmicas:** Feedback visual instantâneo para ações do usuário (sucesso, erro), melhorando a experiência de uso.
* **Design Responsivo:** Interface adaptável para uma experiência consistente em desktops e dispositivos móveis.

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

* **Backend:**
    * Python 3
    * Flask
* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript
* **Banco de Dados:**
    * Microsoft SQL Server
    * `pyodbc` (Driver de Conexão)
* **Infraestrutura e DevOps:**
    * `python-dotenv` (Gerenciamento de Variáveis de Ambiente)
    * Git & GitHub

---

## 🚀 Rodando o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em seu ambiente de desenvolvimento.

### Pré-requisitos

* Python 3.8+
* Git
* Microsoft SQL Server (qualquer edição)
* [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server)

### Guia de Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/gabriel-wav/RadarPet.git](https://github.com/gabriel-wav/RadarPet.git)
    cd RadarPet
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    ```bash
    # Criar venv
    python -m venv venv
    # Ativar no Windows
    .\venv\Scripts\activate
    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto e preencha com suas credenciais do banco de dados, usando um dos exemplos abaixo como base.

    *Exemplo para Autenticação do Windows:*
    ```ini
    DB_SERVER=NOME-PC\SQLEXPRESS
    DB_DATABASE=radar_pet
    DB_USERNAME=
    DB_PASSWORD=
    USE_WINDOWS_AUTH=true
    ```

5.  **Inicialize o Banco de Dados:**
    Este comando criará o banco `radar_pet` e suas tabelas.
    ```bash
    python database.py
    ```

6.  **Execute a Aplicação:**
    ```bash
    flask run
    ```

7.  **Acesse no Navegador:**
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Estrutura do Projeto

A estrutura de pastas foi organizada da seguinte forma para manter o código limpo e escalável:

```
radar-pet/
├── static/
│   ├── ... (outros css de página)
│   ├── main.js
│   ├── imagens/(imagens do site)
│   └── uploads/ (imagens enviadas pelos usuarios)
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── ... (outros html)
├── app.py
├── models.py
├── database.py
├── config.py
├── .env
└── requirements.txt
```
SOCORRO
