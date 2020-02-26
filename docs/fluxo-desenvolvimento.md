# Fluxo de Desenvolvimento

## Escolha dos alvos

Para escolher os alvos foi priorizado portais que fornecesse informações (ou que fosse possível descobrir) sobre a quantidade de notícias há no portal. Além disso, foi utilizado também como requisito sites que tivessem uma paginação simples.

### Escolha das categorias

Alguns portais possuem diversas categorias. Algumas não se adequavam ao projeto, por isso foram retiradas do fluxo de extração.

### Otimização das consultas

Para otimizar o acesso as páginas das notícias, foi adicionado ao [DownloaderMiddleware](https://github.com/naanadr/portais-noticias-tech/blob/301baab2ccc0921d3045294f154fa36a5ca0bdde/portais_tech/portais_tech/middlewares.py#L39) uma função que verificava se a url (que tivesse callback de `extract_info_pages`) já hávia sido acessada e armazenada no banco. Caso essa url (e suas informações) já estivesse armazenada no banco, a requisição seria ignorada. 

### Fluxo de consulta das spiders

Após acessar a página principal do portal de notícia, a spider busca as urls relacionadas as categorias e armazena-as. Assim, a spider segue para a segunda etapa que consiste de acessar as categorias coletadas e extrair as urls das notícias presentes na página principal. Após todas as urls das notícias tiverem sido acessadas e extraídas, ele segue para a proxima página.

## Modo de armazenamento
