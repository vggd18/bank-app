# 🏦 Sistema Bancário Simples (v2.0 - OOP)

Um projeto de console em Python que simula as operações básicas de um sistema bancário.

Este projeto foi inicialmente desenvolvido como um script procedural e, posteriormente, **refatorado para uma arquitetura completa de Programação Orientada a Objetos (OOP)**, demonstrando a separação de responsabilidades, encapsulamento e herança.

## ✨ Funcionalidades

O sistema permite que os usuários realizem as seguintes ações através de um menu interativo:

* **Gerenciamento de Clientes:**
    * Criação de novos clientes (Pessoa Física).
    * Autenticação de clientes (Login / Logout).
    * Prevenção de clientes duplicados (validação por CPF).
* **Gerenciamento de Contas:**
    * Criação de contas correntes (múltiplas contas por cliente).
    * Seleção de conta para realizar transações.
* **Operações Bancárias:**
    * **Depósito:** Adiciona valores à conta (apenas valores positivos).
    * **Saque:** Retira valores da conta, sujeito a regras de negócio.
    * **Extrato:** Exibe todo o histórico de transações e o saldo atual.
* **Regras de Negócio (Conta Corrente):**
    * Limite de **3 saques diários**.
    * Valor máximo de **R$ 500,00 por saque**.

## 🚀 Tecnologias Utilizadas

* **Python 3**
* Módulos nativos (`datetime`, `typing`)

## 🏛️ Arquitetura OOP

O projeto foi reestruturado em torno de classes para gerenciar o estado e a lógica de negócios de forma organizada.



* **`BankSystem`**: Classe orquestradora principal. Gerencia a lista de clientes, o cliente logado e o estado geral da aplicação, removendo a necessidade de variáveis globais.
* **`Client` / `Person`**: `Client` é uma classe base para clientes, e `Person` herda dela, adicionando atributos específicos (nome, CPF, etc.). Gerencia os dados do cliente e suas contas.
* **`Account` / `CurrencyAccount`**: `Account` é a classe base para contas, contendo a lógica de saldo e histórico. `CurrencyAccount` (Conta Corrente) herda de `Account` e sobrescreve o método `withdraw()` para implementar as regras de negócio (limites de saque).
* **`History`**: Uma classe dedicada a encapsular e formatar o histórico de transações.

## 🏃 Como Executar

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd seu-repositorio
    ```
3.  Execute o script Python (vamos supor que seu arquivo se chame `banco.py`):
    ```bash
    python main.py
    ```
4.  Siga as instruções no menu do console para interagir com o sistema.

## 🧪 Como Testar

O sistema pode ser testado manualmente seguindo o roteiro do menu, ou automaticamente via redirecionamento de entrada.

1.  Crie um arquivo `testes.txt` com a sequência de comandos (veja exemplo abaixo).
2.  Execute o script passando o arquivo como entrada:

    ```bash
    python banco.py < testes.txt
    ```
