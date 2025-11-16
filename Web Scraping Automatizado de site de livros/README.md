# Raspagem Web Automatizada — Books to Scrape

## Objetivo:
Criar uma ferramenta automatizada para extrair informações de livros (título, preço e disponibilidade) do site Books to Scrape, salvando os dados em planilha CSV de forma simples e acessível por interface gráfica.

## Principais etapas realizadas:

- Rastreamento: Acesso automático a todas as 50 páginas do site por meio da biblioteca Requests.

- Extração de dados: Utilização do BeautifulSoup para identificar e capturar elementos HTML correspondentes aos títulos, preços e status de disponibilidade.

- Armazenamento estruturado: Organização dos dados em um DataFrame Pandas, com exportação para o arquivo Tabela_de_livros.csv.

- Interface gráfica: Criação de uma interface simples com Tkinter, permitindo que o usuário execute o scraping com apenas um clique.

- Compatibilidade ampliada: Sistema configurado para salvar o arquivo automaticamente na mesma pasta do script ou executável (.exe), facilitando o uso em qualquer ambiente.

## Resumo:
Aplicação de web scraping com Python, combinando Requests, BeautifulSoup, Pandas e Tkinter para oferecer uma solução completa, prática e interativa de coleta automatizada de dados. Ideal para demonstrações de automação e aprendizado em raspagem web.
