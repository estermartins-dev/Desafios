# Sistema de Loja Simples

Este projeto consiste em um sistema de gerenciamento de uma loja simples desenvolvido em Python. O foco da aplicação está na modularidade do código, validação robusta de dados e organização da estrutura de arquivos.

O sistema permite o cadastro de produtos, realização de vendas com controle de estoque, aplicação automática de descontos e geração de relatórios detalhados das vendas realizadas.

---

## Funcionalidades

**Cadastro de Produtos:**
Permite registrar produtos com nome, preço e quantidade em estoque, com validações para evitar nomes duplicados, valores inválidos ou negativos.

**Realização de Vendas:**
O usuário pode selecionar produtos por nome ou índice, informar a quantidade desejada e realizar a compra com validação de estoque disponível.

**Cálculo de Valores:**

* Valor bruto calculado automaticamente (preço × quantidade)
* Aplicação de desconto de 5% para compras com mais de 10 unidades
* Atualização automática do estoque após cada venda

**Geração de Relatório:**
Exibição detalhada de todas as vendas realizadas, incluindo:

* Nome do cliente
* Produto
* Quantidade
* Valor bruto
* Desconto aplicado
* Valor final

Além disso, é exibido o total arrecadado pela loja.

**Persistência em Arquivo:**
Permite salvar o relatório de vendas em um arquivo de texto dentro de um diretório específico.

**Funcionalidades Extras:**

* Atualização de estoque de produtos
* Histórico das últimas 5 vendas utilizando estrutura de pilha

---

## Estrutura do Projeto

A organização dos arquivos segue boas práticas de separação de responsabilidades:

**DESAFIO/**: Diretório raiz do projeto

**relatorios/**: Pasta destinada ao armazenamento dos relatórios gerados

**src/**: Contém os módulos principais do sistema

* ****init**.py**: Define o diretório como pacote Python
* **cadastro.py**: Responsável pelo cadastro e validação de produtos
* **calculos.py**: Contém as regras de negócio e cálculos das vendas
* **utils.py**: Funções auxiliares para relatórios, arquivos e pilha de vendas

**main.py**: Arquivo principal que executa o sistema e controla o menu interativo

---

## Instruções de Execução

1. Certifique-se de possuir o Python 3.x instalado em seu sistema
2. Abra o terminal ou prompt de comando na pasta raiz do projeto
3. Execute o programa com o comando:

```
python main.py
```

---

## Tecnologias Utilizadas

**Python:** Linguagem principal utilizada no desenvolvimento

**Biblioteca OS:** Utilizada para manipulação de arquivos e diretórios

---

## Desenvolvido por

Nome: Ester Martins Silva
RA: 5172842
Professor: Maxwell
Projeto de Sistemas de Informação - Desafio de Programação em Python
