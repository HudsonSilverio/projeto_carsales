# WebScraping
<label>Acessando a internet, coletando os dados e apresentando-os</label>

<div align=center>
<img src="https://user-images.githubusercontent.com/109561598/197368807-89056542-fbeb-430d-a4c7-dd05c9330790.jpg" width=800 alt=imagem logo do projeto" />
</div>

<!-- ************************************* Título ********************************************* -->
<h1 align="center"> Coelta com Scrapy dados Merdado Livre Carros Usados </h1>

<!-- ************************************* Baadges ********************************************* -->

## 🚀 Sobre o Projeto

Caso de mercado:  O cliente  tem uma revendedora de carros  gostaria de realizar uma análise dos preços de veículos para ajustar sua estratégia de price na sua concessionária e realizar a previsão de tendência de preços. 
      Seu objetivo é comparar os preços de seus veículos com os preços de veículos semelhantes no Mercado Livre, considerando o mesmo ano, modelo e quilometragem e quais são os anos de fabricação, modelos e faixas de quilometragem mais frequentemente listados no Mercado Livre.

## Etapa 01 - Fazendo o setup da para integração com o github

  <li> instalado a versão escolhida - pyenv local 3.12.1</li>

## Etapa 02 - Criando um ambiente isolado para o projeto
  
  <li>
    python -m venv .venv (criando o ambiente);</li>
  <li>
   source .venv/Scripts/activate (ativando o ambiente)
;</li>

## Etapa 03 - Criando um arquivo .gitignore
  <li>
    Crie esse tipo de arquivo no vscode.  Esse arquivo irá armazenar tudo que eu não quero que fique salvo no meu git</li>
  

## Etapa 04 - Integrando seu projeto com o github
 <li>     
    →Primeiro, crie um repositório no GITHUB  !   Através dos códigos que estão na página no projeto no github, vamos copiar e colar os códigos no bash da página no vscode .

  <li>
   Copie e cole todos os codigos que aparecem na apagina inicial de criacao do repositorio no terminal ;</li>
  
        
## Etapa 05 - Coletando os Dados

 <li> Instalar o scrapy - pip install scrapy

  <li> A biblioteca Scrapy é uma ferramenta open-source em Python usada para fazer web scraping, ou seja, para extrair dados de websites de forma automática

<li> Execute esse codigo no terminal: scrapy startproject coleta ( esse comando cria uma pasta com toda a divisão do seu projeto de web scraping)

<li> Crie uma pasta chamada src de certa forma que a pasta coleta esteja dentro dela

<li> scrapy genspider "nome_do _seu_arquivo", ' URL do site " → (este comando inicia a coleta no site que for direcionado)

<li> Realizando a coleta dos dados através do scrapy shell ( entra dentro de um terminal e faz a requisição no site e navegar dentro do html antes de desenvolver o código ) - muito util para testar os cod antes de ir para o arquivo principal.

<li> Caso der o erro 403 e na mensagem de erro aparecer pedindo o USER AGENT, iremos simular um usuário para nao ser barrado pelo site colocando o USER AGENT da sua maquina: pesquise por 'agent user my' no Google e coloque dentro do arquivo 'settings.py' e digite dentro de USER_AGENT = e coloque  o agente user da sua máquina. (não esqueça das aspas)

<li> Saia do terminal e rode o código no bash scrapy shell

<li> Abre o terminal, faça o comando fetch("URL do site") - se aparecer o cod 200 correu tudo certo(acesso permitido)

<li> Digite o código no terminal 'response.text', para poder retornar no terminal  para você todo o HTML da página

<li> → quando esse código é executado ele cria dentro da pasta spiders um arquivo py com o nome que você colocou (ex: mercadolivre) - nesse porte que será responsável por fazer os códigos para coletar as informações do site.

 ## Etapa 06 - Inspeção Visual dentro do HTML

 <li> Agora nessa etapa de inspecionar no HTML da página como estão as informações que você deseja coletar. Deve-se procurar visualmente qual a parte que se deseja coletar no código html. Dica: clicar onde exatamente na página onde se quer coletar o dado e inspecionar a página com o botão direito conforme as figuras 1 e 2 abaixo.

 



