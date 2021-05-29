# :bar_chart: Análise Exploratória Dados do SUS :bar_chart:

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Logo_SUS.svg/1200px-Logo_SUS.svg.png)

# Sobre o projeto

Olá, meu nome é Pedro Henrique, e esse é meu repositório referente ao projeto final do módulo 1 do [Bootcamp De Data Science Aplicada](https://www.alura.com.br/bootcamp/data-science-aplicada/matriculas-abertas) promovido pela [Alura](https://www.alura.com.br/), sobre Python e pandas para análise de dados reais. Esse projeto teve como objetivo realizar uma análise exploratória em dados reais do Sistema Único de Saúde(SUS).

A análise exploratória tem como objetivo encontrar possíveis padrões de uma forma muito flexível procurando pistas e indícios sobre o comportamento dos dados, seu próposito é levantar hipóteses sobre a distribuição dos dados sem uma definição prévia e sem tranformações estatística.

O projeto foi dividido em 3 pastas diferentes, são elas:
 
### [Dados brutos](https://github.com/Pedro-correa-almeida/Projeto_modulo_1/tree/main/dados_brutos): 

Nesse diretório estão os dados coletados diretos da fonte sem nenhuma limpeza, no total foram coletados 5 bases de dados, 3 delas do [datasus](http://tabnet.datasus.gov.br/cgi/menu_tabnet_php.htm#), referentes ao valor dos serviços hospitalares, número de AIHs(Autorização de Internação Hospitalar) aprovadas e média de permanência dos pacientes, todas foram coletadas com as colunas indicando o mês e o ano, e o index a Unidade Federativa correspondente.

Além disso foram utilizadas duas bases de dados auxiliares do [IBGE](https://www.ibge.gov.br/pt/inicio.html), uma referente à população dos estados a cada ano, com o objetivo de realizar uma análise proporcional à população, e a outra referente ao valor do IPCA(Índice Nacional de Preços ao Consumidor Amplo) por mês, e foi utilizado para realizar uma correção nos valores hospitalares a fim de tentar passar uma visão mais real dos gastos ao longo do tempo.

### [Dados limpos](https://github.com/Pedro-correa-almeida/Projeto_modulo_1/tree/main/dados_limpos):

Aqui estão as bases de dados após todos os tratamentos e limpeza realizados a fim de deixar as bases de dados em um padrão que fosse possível comparar todos os valores juntos.
<br>
Observação: a base de dados referente ao IPCA foi utilizada como uma base de dados auxiliar apenas para corrigir os valores gastos, portanto ela não foi utilizada na análise final e não precisou ser salva no repositório de dados limpos.

### [Notebooks](https://github.com/Pedro-correa-almeida/Projeto_modulo_1/tree/main/notebooks)

Aqui se encontram os 5 notebooks utilizados na análise e além disso um [arquivo python](https://github.com/Pedro-correa-almeida/Projeto_modulo_1/blob/main/notebooks/funcoes_datasus.py) com as funções utilizadas nos notebooks, desses 5 notebooks, em 4 deles foram realizadas as transformações e limpeza necessárias a fim de deixar o notebook com a [análise final] mais limpo e focado na análise exploratória
