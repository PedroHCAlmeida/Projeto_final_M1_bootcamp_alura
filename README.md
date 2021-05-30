# :bar_chart: Análise Exploratória Dados do SUS :bar_chart:

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Logo_SUS.svg/1200px-Logo_SUS.svg.png)

# Sobre o projeto

Olá, meu nome é Pedro Henrique, e esse é meu repositório referente ao projeto final do módulo 1 do [Bootcamp De Data Science Aplicada](https://www.alura.com.br/bootcamp/data-science-aplicada/matriculas-abertas) promovido pela [Alura](https://www.alura.com.br/), esse módulo tratou sobre Python e pandas para análise de dados reais. Esse projeto teve como objetivo realizar uma análise exploratória em dados reais do Sistema Único de Saúde(SUS).

A análise exploratória tem como objetivo encontrar possíveis padrões de uma forma muito flexível procurando pistas e indícios sobre o comportamento dos dados, seu próposito é levantar hipóteses sobre a distribuição dos dados sem uma definição prévia e sem tranformações estatísticas.

O projeto foi dividido em 3 pastas diferentes, são elas:
 
### [Dados brutos](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/tree/main/dados_limpos): 

Nesse diretório estão os dados coletados diretos da fonte sem nenhuma limpeza, no total foram coletados 5 bases de dados, 3 delas do [datasus](http://tabnet.datasus.gov.br/cgi/menu_tabnet_php.htm#), referentes ao valor dos serviços hospitalares, número de AIHs(Autorização de Internação Hospitalar) aprovadas e média de permanência dos pacientes, todas foram coletadas com as colunas indicando o mês e o ano, e o index a Unidade Federativa correspondente.

Além disso foram utilizadas duas bases de dados auxiliares do [IBGE](https://www.ibge.gov.br/pt/inicio.html), uma referente à população dos estados a cada ano, com o objetivo de realizar uma análise proporcional à população, e a outra referente ao valor do IPCA(Índice Nacional de Preços ao Consumidor Amplo) por mês, e foi utilizado para realizar uma correção nos valores hospitalares a fim de tentar passar uma visão mais real dos gastos ao longo do tempo.

### [Dados limpos](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/tree/main/dados_limpos):

Aqui estão as bases de dados após todos os tratamentos e limpeza realizados a fim de deixar as bases de dados em um padrão que fosse possível comparar todos os valores juntos.
<br>
Observação: a base de dados referente ao IPCA foi utilizada como uma base de dados auxiliar apenas para corrigir os valores gastos, portanto ela não foi utilizada na análise final e não precisou ser salva no repositório de dados limpos, além disso a base de dados sobre a população dos estados por ano foi tratada junto com as AIHs aprovadas e esses dados estão juntos no arquivo [AIH_aprovadas_e_populacao](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/blob/main/dados_limpos/AIH_aprovadas_e_populacao.csv).

### [Notebooks](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/tree/main/notebooks)

Aqui se encontram os 5 notebooks utilizados na análise e além disso um [arquivo python](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/tree/main/notebooks/funcoes_datasus.py) com as funções utilizadas nos notebooks, desses 5 notebooks, em 4 deles foram realizadas as transformações e limpeza necessárias a fim de deixar o notebook com a [análise final](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/blob/main/notebooks/analise_exploratoria_final.ipynb) mais limpo e focado na análise exploratória.

# Escopo do projeto

## 1- Limpeza dos dados brutos

Aqui foi realizada a limpeza dos dados brutos, uma das partes mais importantes do projeto e mais trabalhosas, e, por essa razão, essa parte foi dividida em vários notebooks, seguindo o mesmo padrão:

-Dados restringidos entre Fevereiro de 2008 e Dezembro de 2019, pois ao se analisar dados reais, principalmente envolvendo saúde, temos que tomar cuidado com dados que apresentam dados faltantes ou desatualizados.
<br>
-Os dados foram manipulados para ter uma coluna só para as datas, uma coluna só para os estados, uma coluna para região do estado, e por fim uma coluna para os dados numéricos.

## 2 - Leitura dos dados limpos

Foi realizada a leitura dos dados limpos que estão em 3 arquivos diferentes em 'DataFrames' do pandas, são eles:

-[AIH aprovadas e população](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/blob/main/dados_limpos/AIH_aprovadas_e_populacao.csv) - arquivo csv dividido em 7 colunas: UF(estado), regiao, data(formato ano-mês-dia), AIH_aprovadas(números de AIH no período pelo estado), ano, pop(população naquele ano), AIH_por_mil(AIHs aprovadas a cada mil habitantes daquele estado)
<br>
-[Média de permanência](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/blob/main/dados_limpos/media_permanencia.csv) - arquivo csv dividido em 4 colunas: UF(estado), regiao, data(formato ano-mês-dia), perm_media(permanência média dos pacientes no período pelo estado)
<br>
-[Valor hospitalar corrigido](https://github.com/Pedro-correa-almeida/Projeto_final_M1_bootcamp_alura/blob/main/dados_limpos/valor_hospitalar_corrigido.csv) - arquivo csv dividido em 5 colunas: UF(estado), regiao, data(formato ano-mês-dia), valor_hospitalar(valor dos serviços hospitalares referente às AIH aprovadas no período), valor_corrigido(valor hospitalar gasto corrigido pelo IPCA no período pelo estado)

## 3 - Funções

Nessa parte estão as funções utilizadas nos notebooks.

## 4 - Concatenação dos dados

Nessa etapa do projeto todos três arquivos foram unidos em apenas um 'DataFrame' do pandas a fim de comparar todos os dados obtidos, além disso foi criada mais uma coluna(valor_corrigido_por_mil) calculando se o valor gasto corrigido a cada mil habitantes do estado, e foi criado outro 'DataFrame' agrupando os dados pela região.

## 5 - Análise Exploratória
