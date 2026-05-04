Sistema de Folha de Pagamento Este projeto consiste em um sistema de gerenciamento de folha de pagamento desenvolvido em Python. O foco da melhoria está na modularidade do código, robustez no tratamento de dados e organização da estrutura de arquivos. O sistema permite o cadastro de funcionários nas categorias CLT, Estagiário e Freelancer, realizando o planejamento automático de faturamento, impostos e descontos específicos para cada modalidade.

Funcionalidades Cadastro de Funcionários: Coleta de dados com validação de entrada, impedindo o registro de nomes vazios ou valores numéricos negativos.

Cálculo de Tributação:

CLT: Aplicação de desconto de 8% para INSS e 10% para IRRF (incidente apenas sobre faturamento bruto superior a 2.000,00).

Freelancer: Aplicação de desconto fixo de 5% sobre o valor bruto total.

Estagiário: Cálculo baseado em valor fixo, sem incidência de descontos.

Geração de Relatório: Exposição detalhada de ganhos e descontos por colaborador e cálculo do custo total da folha para a empresa.

Persistência em Arquivo: Opção para exportar o relatório final em formato de texto para um diretório específico.

Estrutura do Projeto A organização dos arquivos segue padrões de desenvolvimento para separação de responsabilidades:

DESAFIO/: Diretório raiz do projeto.

relatorios/: Pasta destinada ao armazenamento dos arquivos de texto gerados.

src/: Pasta contendo o código-fonte do sistema.

init.py: Arquivo para definição do diretório como pacote Python.

cadastro.py: Módulo responsável pela interface de entrada e validação de dados.

calculos.py: Módulo contendo regras de negócio e fórmulas matemáticas.

main.py: Ponto de entrada do programa e controle do menu principal.

utils.py: Funções utilitárias para formatação de texto e manipulação de arquivos.

Instruções de Execução Certifique-se de possuir o Python 3.x instalado em seu sistema.

Abra o terminal ou prompt de comando na pasta raiz do projeto.

Navegue até o diretório de código-fonte: cd src

Iniciando a aplicação: python main.py

Tecnologias Utilizadas Python: Linguagem de programação utilizada para o desenvolvimento da lógica.

Git: Ferramenta de controle de versão.

GitHub: Plataforma de hospedagem de código e colaboração.

Biblioteca OS: Utilizada para gerenciamento de caminhos e criação de diretórios no sistema operacional.

Desenvolvido por: Nome: Ester Martins Silva RA: 5172842 Projeto de Sistemas de Informação - Desafio de Programação em Python esse foi um exemplo, com base no exemplo crie um sobre o projeto atual
