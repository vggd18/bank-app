# Sistema Bancário Simples

Uma simulação de sistema bancário simples via linha de comando, escrita em Python. O projeto permite depositar, sacar, verificar o saldo e o extrato.

## Funcionalidades

O sistema oferece as seguintes operações:

* **[d] Depositar:** Adiciona um valor positivo ao saldo da conta.
* **[w] Sacar:** Retira um valor da conta, sujeito a regras de limite.
* **[b] Saldo:** Exibe o saldo atual e um extrato com todas as transações realizadas.
* **[q] Sair:** Encerra a aplicação.

## Regras de Negócio

A operação de saque possui as seguintes restrições:

1.  O valor do saque deve ser positivo.
2.  O valor do saque não pode exceder o saldo em conta.
3.  O limite máximo por saque é de **R$ 500,00**.
4.  O limite máximo é de **3 saques por dia**.

*Nota: O estado da conta (saldo, histórico) não é persistente e será resetado toda vez que o script for executado.*

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

3.  **Dependências:** Este projeto não possui dependências externas e utiliza apenas bibliotecas padrão do Python.

4.  Execute o script principal (supondo que você o salvou como `main.py`):

    ```bash
    python main.py
    ```

5.  Siga as instruções no terminal para interagir com o sistema.