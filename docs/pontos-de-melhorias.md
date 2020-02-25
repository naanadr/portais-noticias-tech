# Pontos de Melhorias

A seguir serão descritos alguns pontos de melhorias para o projeto. Não necessariamente os pontos estão ordenados pela sua importância. 



1. Limpar comandos executas no Dockerfile
    * Quais pacotes realmente precisam ser instalados?
    * Quais pacotes podem ser removidos apos a instalação das libs utilizadas?
    
    > Com isso será possível otimizar o build da imagem. 
  
2. Subir Dockerfile para o EC2 na AWS
    > Ou para o dockerhub, ou seja, disponibilizar ele para outras pessoas e para uso em outros projetos.
 
3. Refatorar código:
   * Corrigir ativação e desativação de Pipelines

4. Adicionar passagem de parâmetro para o usuario escolher:
   * modo de persistencia de dados
   * spiders que serão executadas
   
   > Isso não ocorre hoje quando o usuário executa o script de inicialização das spiders

5. Utilizar outros sites para realizar extração:
   * A maioria dos sites obversados utilizam JS para carregar mais notícias
   * Inserir o Splash no projeto para poder carregar o JS das páginas e poder acessar mais notícias

6. Otimizar XPATHs utilizados nos sites, junto com a otimização de requisições. Dado que em alguns sites é possível chegar em uma mesma página por varíos fluxos. 

7. Adiciona requisição por batches e em paralelo, para otimizar as extrações. Alguns sites tem um tempo de resposta mais lento que outros e isso afeta a velocidade do script. 
