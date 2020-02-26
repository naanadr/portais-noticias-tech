# Pontos de Melhorias

A seguir serão descritos alguns pontos de melhorias para o projeto. Não necessariamente os pontos estão ordenados pela sua importância. 


## Dockerfile e docker-compose

* Refatorar o Dockerfile
   
   * Remover pacotes instalados no sistema após instalação das bibliotecas utilizadas
   * Ajustar variáveis utilizadas no docker-compose
   * **Por que?**
      * Otimização do build da imagem
      * Separar o ambiente de desenvolvimento e produção

* Utilizar o docker machine
   
   * Comunicar a imagem docker do projeto com o EC2 (AWS) 


## Otimização de execução

* Executar em uma instância EC2

* Refatorar o script de execução:
   
   * Receber como parâmetro a spider que será executada
   * Executar o script de forma separada no EC2 (AWS)
   * **Por que?**
      * Otimização no tempo de execução, eu teria duas spiders executando de forma simutânea.
      * O crawler não estará executando na minha máquina.

* Refatorar o código:
   
   * Extrair as principais urls, por exemplo, as catégorias principais de um site. Utilizar essas urls para serem start_urls de spiders secundárias, que executaram em paralelo.
   * Extrair apenas notícias novas. No caso, parar a execução após X notícias replicadas. Dado que é feito uma verificação antes das requisições, para validar se a url está presente no banco ou não. 
   * Receber como parâmetro o método utilizado para persistir os dados
      * S3 (AWS) e DynamoDB
      * JSON
      * MongoDB
 
## Obtenção de dados

* Utilizar outros sites para realizar extração:
 
   * A maioria dos sites obversados utilizam JavaScript para carregar mais notícias
      * Inserir o Splash no projeto para poder carregar o JavaScript das páginas e poder acessar mais notícias
   * Sites que disponibilizem informações sobre o engajamento de suas materias


