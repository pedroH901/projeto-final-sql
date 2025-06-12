# Radar Pet 🐾

Radar Pet é uma plataforma web completa desenvolvida em Python com Flask e SQL Server, criada para ajudar a comunidade a encontrar animais de estimação perdidos e anunciar os que foram encontrados. O projeto conecta pessoas de forma rápida e eficiente, promovendo o reencontro de pets com suas famílias.

##  funcionalidades

* **Autenticação de Usuários:** Sistema completo de cadastro e login para garantir que apenas usuários registrados possam anunciar pets.
* **Anúncio de Pets:** Formulário detalhado para anunciar pets perdidos ou achados, incluindo informações como espécie, raça, sexo, localização e descrição.
* **Upload de Fotos:** Funcionalidade para anexar uma foto do pet ao anúncio, essencial para a identificação.
* **Galeria de Pets:** Uma página principal onde todos os anúncios são exibidos em formato de cartões, permitindo uma visualização rápida de todos os pets.
* **Visualização de Detalhes:** Cada anúncio possui uma página própria com todas as informações detalhadas e a foto do pet em destaque.
* **Notificações Dinâmicas:** Mensagens de feedback para o usuário (sucesso, erro, etc.) que aparecem na tela e somem suavemente após alguns segundos.
* **Design Responsivo e Organizado:** A estrutura do projeto utiliza um template base, garantindo consistência visual e facilitando a manutenção.

## Tecnologias Utilizadas

* **Backend:** Python 3, Flask
* **Banco de Dados:** Microsoft SQL Server
* **Conexão com Banco:** `pyodbc`
* **Frontend:** HTML5, CSS3, JavaScript
* **Gerenciamento de Configuração:** `python-dotenv` para variáveis de ambiente

---

## 🚀 Como Usar e Executar o Projeto

Siga estes passos para configurar e rodar o projeto na sua máquina local.

### Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:
1.  **Python 3.8** ou superior.
2.  **Git**.
3.  Uma instância do **Microsoft SQL Server** (pode ser a versão Express, Developer, etc.).
4.  O **[Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server)**. Este é um passo **crucial** para a conexão com o banco de dados.

### Instalação

1.  **Clone o Repositório**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DA_PASTA_DO_PROJETO>
    ```

2.  **(Recomendado) Crie e Ative um Ambiente Virtual**
    ```bash
    # Criar
    python -m venv venv
    # Ativar (Windows)
    .\venv\Scripts\activate
    # Ativar (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Instale as Dependências**
    O arquivo `requirements.txt` contém todas as bibliotecas Python necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Ambiente (`.env`)**
    Crie um arquivo chamado `.env` na pasta raiz do projeto. Ele guardará suas credenciais do banco de dados de forma segura. Copie o conteúdo abaixo e preencha com seus dados.

    **Exemplo de `.env` para Autenticação do Windows:**
    ```ini
    # Endereço do seu servidor SQL (ex: NOME-PC\SQLEXPRESS)
    DB_SERVER=SEU_SERVIDOR
    # Nome do banco de dados que será criado
    DB_DATABASE=radar_pet
    # Para autenticação do Windows, deixe usuário e senha vazios
    DB_USERNAME=
    DB_PASSWORD=
    USE_WINDOWS_AUTH=true
    ```

    **Exemplo de `.env` para Autenticação do SQL Server:**
    ```ini
    DB_SERVER=SEU_SERVIDOR
    DB_DATABASE=radar_pet
    DB_USERNAME=seu_usuario_sql
    DB_PASSWORD=sua_senha_sql
    USE_WINDOWS_AUTH=false
    ```

5.  **Inicialize o Banco de Dados**
    Execute o script `database.py` para criar o banco de dados `radar_pet` e as tabelas `usuario` e `pet`.
    ```bash
    python database.py
    ```
    Você deverá ver mensagens de sucesso no terminal. Se ocorrer algum erro, verifique suas configurações no arquivo `.env`.

6.  **Execute a Aplicação**
    Com tudo configurado, inicie o servidor Flask.
    ```bash
    python app.py
    ```

7.  **Acesse o Site**
    Abra seu navegador e acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Estrutura do Projeto

radar-pet/
├── static/
│   ├── ... (outros css de página)
│   ├── main.js
│   ├── imagens/ (imagens do site)
│   └── uploads/ (imagens enviadas pelos usuarios)
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── ... (outros html)
├── app.py
├── models.py
├── database.py
├── config.py
├── .env
└── requirements.txt
