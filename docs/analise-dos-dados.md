# Análise dos Dados

> As análises realizadas foram com os dados obtidos durante 12h de execução de código. 

As análises foram realizadas utilizando um Jupyter Notebook, que pode ser encontrado nesse [arquivo](../analises/analises.ipynb).

Para executar esse arquivo você precisará instalar o ambiente de desenvolvimento que está configurado no Poetry (veja o [README](../README.md) para mais informações). 

Os arquivos utilizados nesse Jupyter, são os JsonLines gerados a partir da execução das spiders. Como esse projeto possui apenas duas spiders, os jsons são o [olhardigital.jsonl](../portais_tech/olhardigital.jsonl) e o [tecmundo.jsonl](../portais_tech/tecmundo.jsonl). Ao final da execução do notebook você terá dois arquivos novos, o primeiro conterá todos as notícias extraídas dos portais escolhidos (após um pós-processamento) e o segundo conterá as notícias organizadas a partir das tags que elas possuírem (no caso, apenas notícias que possuam tags serão armazenadas nesse json). 

Para mais informações sobre como foi realizado esse processo, veja o [notebook](../analises/analises.ipynb).
