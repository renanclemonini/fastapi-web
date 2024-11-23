# FastAPI Web

Este projeto é uma aplicação baseada no framework **FastAPI**, que utiliza templates **Jinja2** para renderizar páginas web de forma dinâmica.

O objetivo desta documentação é orientar sobre os passos necessários para configurar e rodar o projeto.

---

## Passos para Configuração

1. **Realizar o clone do projeto**
   - Clone o repositório na sua máquina local utilizando o comando:
     ```bash
     git clone https://github.com/renanclemonini/fastapi-web.git
     ```

2. **Criar um ambiente virtual**
   - Execute o seguinte comando no terminal, substituindo `nome_ambiente_virtual` pelo nome desejado (geralmente `venv`, `.venv` ou `.env`):
     ```bash
     python -m venv .nome_ambiente_virtual
     ```
   - **Observação:** É fundamental configurar um ambiente virtual antes de instalar as dependências.

3. **Inicializar o ambiente virtual**
   - No Linux/macOS, execute:
     ```bash
     .nome_ambiente_virtual\Scripts\activate
     ```
   - No Windows, execute:
     ```bash
     source .nome_ambiente_virtual/bin/activate
     ```

4. **Instalar as dependências**
   - Com o ambiente virtual ativado, instale as bibliotecas necessárias executando:
     ```bash
     pip install -r requirements.txt
     ```

5. **Iniciar o servidor FastAPI**
   - Para iniciar o servidor local, execute o seguinte comando no terminal:
     ```bash
     fastapi dev main.py
     ```
   - Certifique-se de substituir `main` pelo nome do arquivo Python que contém a instância do FastAPI (`app`).

---

## Informações Importantes
   - Sempre que for atualizar a lista do requirements.txt execute:
   ```bash
   pip freeze > requirements.txt
   ```

## Última atualização
23/11/2024 às 11:30
