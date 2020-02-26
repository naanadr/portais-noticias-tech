# Fluxo de Desenvolvimento

## Escolha das tecnologias

Foi escolhido tecnologias que a desenvolvedora Core desse repositório tem familiaridade e que tivessem uma boa documentação.

Em alguns casos, como o Docker, contratempos surgiram e dado a boa documentação os contratempos foram possíveis de ser resolvidos. 


## Escolha dos alvos

Para escolher os alvos foi priorizado portais que fornecessem informações (ou que fosse possível descobrir) sobre a quantidade de notícias no portal. Além disso, foi utilizado também como requisito sites que tivessem uma paginação simples, no caso, que não precisassem de javascript para carregar mais notícias no site (como as infinity scroll).

### Escolha das categorias

Alguns portais possuem diversas categorias. Algumas não se adequavam ao projeto, por isso foram retiradas do fluxo de extração. Por exemplo, a categoria [Udemy](https://www.tecmundo.com.br/udemy) no TecMundo.

> Isso não se aplica ao [Olhar Digital](https://olhardigital.com.br/noticias/), pois todas as notícias estão listadas em uma única página. 


### Otimização das consultas

Para otimizar o acesso as páginas de notícias, foi adicionado ao [DownloaderMiddleware](https://github.com/naanadr/portais-noticias-tech/blob/301baab2ccc0921d3045294f154fa36a5ca0bdde/portais_tech/portais_tech/middlewares.py#L39) uma função que verificava se a url (que tivesse callback de `extract_info_pages`) já foi acessada e armazenada no banco. Caso essa url (e suas informações) já estivesse armazenada no banco, a requisição seria ignorada. 

> Isso foi necessário, porque algumas notícias estavam presentes em mais de uma categoria. Outro ponto, que foi utilizado a `url` como primary key, pois ela sempre será única, diferente do titulo que em alguns casos se repete.


### Fluxo de consulta das spiders

Após acessar a página principal do portal de notícia, a spider busca as urls relacionadas as categorias e armazena-as. Assim, a spider segue para a segunda etapa que consiste de acessar as categorias coletadas e extrair as urls das notícias presentes na página principal. Após todas as urls das notícias tiverem sido acessadas e extraídas, ela segue para a proxima página, onde será caletada mais urls que serão utilizadas na extração. 

No caso do Olhar Digital que não possui a troca de categoria, o fluxo é o mesmo, mudando apenas a primeira etapa. Dado que não será necessário buscar categorias e apenas extrair as urls das notícias.


### Fluxo de extração das spiders

Os campos que a spider procurará nas páginas das notícias são:

  * url
  * título
  * quantidade de comentários
  * autor
  * revisor
  * data de publicação
  * referência
  * conteúdo relacionado
  * tags

Esses campos foram escolhidos, pois estavam presentes em quase todas as notícias observadas. Além de ser campos possíveis de extrair.

#### Observações

Sabe-se que alguns campos não são fornecidos pelos portais escolhidos, como por exemplo, o nome do revisor da matéria. Mesmo assim, o campo `revisor` foi mantido, para caso um terceiro portal seja inserido e este tenha essa informação o campo já estará disponível. 

Outros campos, como por exemplo, o `quantidade de comentários` estão presentes na página mas não foram possíveis de extrair (no caso do Olhar Digital). 

> A seção de comentários do Olhar Digital é um iframe de uma página do Facebook. Porém na requisição do Scrapy não foi retornado a div do iframe, para que assim fosse extraida a url. Como esse projeto possuí uma data limite para ser entregue, não foi priorizado resolver esse contratempo.

## Modo de armazenamento

Para armazenar os dados por default é utilizado o MongoDB, no caso, ainda não foi implementado a funcionalidade que permita desativar o MongoDB. A segunda opção de persistência dos dados é utilizando Json, onde cada spider armazenará seus dados em um json separado.

Não é preciso trabalhar inicialmente com um Json, pois no Notebook de análise dos dados ele faz conexão com o MongoDB da sua máquina. 

## Análise dos dados

Para facilitar a visualização dos dados foi optado utilizar o Jupyter Notebook, mas também poderia ter feito um script Python para tal. 

O fluxo de análise consiste de carregar em memória os dados presentes no MongoDB ou Json, esses dados serão utilizados para instânciar um objeto DataFrame. Que será utilizado nas análises. 

> Escolheu-se utilizar Pandas, pois a documentação é detalhada e a desenvolvedora possuí experiência. Além do mais, é possível realizar análises e pós-processamento mais facilmente do que trabalhar com json puro.

