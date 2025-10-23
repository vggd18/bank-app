# Sistema Bancário Simples (Multiusuário)

Uma simulação de sistema bancário multiusuário via linha de comando, escrita em Python. O projeto permite que múltiplos usuários se cadastrem, façam login, criem múltiplas contas correntes e realizem operações de depósito, saque e extrato.

## Funcionalidades

O sistema é dividido entre ações globais (sem login) e ações do usuário (logado):

### Ações Globais

  * **[c] Create User:** Cadastra um novo usuário no sistema (Nome, CPF, Senha, Endereço, Data de Nascimento).
  * **[lin] Login:** Permite que um usuário cadastrado acesse sua conta usando CPF e Senha.
  * **[q] Quit:** Encerra a aplicação.

### Ações do Usuário (Requer Login)

  * **[ca] Create Checking Account:** Cria uma nova conta corrente vinculada ao usuário logado (Agência `0001` e um número de conta único).
  * **[d] Deposit:** Adiciona um valor positivo ao saldo de uma conta específica do usuário.
  * **[w] Withdraw:** Retira um valor de uma conta específica, sujeito a regras de limite.
  * **[b] Balance:** Exibe o extrato (histórico de transações e saldo) de todas as contas vinculadas ao usuário.
  * **[lout] Logout:** Desconecta o usuário atual, retornando ao menu global.

## Regras de Negócio

A operação de saque possui as seguintes restrições, aplicadas **individualmente por conta**:

1.  O valor do saque deve ser positivo.
2.  O valor do saque não pode exceder o saldo da conta selecionada.
3.  O limite máximo por saque é de **R$ 500,00**.
4.  O limite máximo é de **3 saques por dia** *para aquela conta específica*.

*Nota: Todos os dados (usuários, contas, saldos) são armazenados em memória e serão perdidos quando o script for encerrado.*

## Como Usar

### Pré-requisitos

  * Python 3.x

### Instalação e Execução

1.  Clone este repositório (ou apenas baixe o arquivo `.py`).

2.  (Opcional, mas recomendado) Crie e ative um ambiente virtual (`venv`):

    ```bash
    # Criar o ambiente virtual
    python -m venv venv
    ```

    ```bash
    # Ativar no Windows
    .\venv\Scripts\activate
    ```

    ```bash
    # Ativar no Linux/macOS
    source venv/bin/activate
    ```

3.  **Dependências:** Este projeto não possui dependências externas e utiliza apenas bibliotecas padrão do Python (como `datetime`).

4.  Execute o script principal (supondo que você o salvou como `main.py`):

    ```bash
    python main.py
    ```

5.  Siga as instruções no terminal para criar um usuário, fazer login e interagir com o sistema.
