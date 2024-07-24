try:
    import requests
    from bs4 import BeautifulSoup
    
    print("Bibliotecas importadas com sucesso.")
except ImportError as e:
    print(f"Erro de importação: {e}. Por favor, instale a biblioteca necessária usando pip.")
    exit(1)

def pegando_dolar_by_request():
    try:
        # URL da página que você deseja extrair o título:
        url = 'https://dolarhoje.com'
        print(f"Acessando a URL: {url}")

        # Faz a requisição GET para a página:
        response = requests.get(url)
        print("Requisição GET feita com sucesso.")

        # Cria um objeto BeautifulSoup com o conteúdo da página:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Conteúdo HTML analisado.")

        # Pega o conteúdo especifico da página:
        texto = soup.find_all('span', attrs={'class': 'cotMoeda nacional'})
        print("Conteúdo específico extraído.")

        parte1 = False
        parte2 = False
        
        for elemento in texto:
            parte1 = elemento.find('span').text
            parte2 = elemento.find('input').get('value')

        if parte1 and parte2:
            valor_dolar = f'OOOOOOO valor do Dolár Hoje é igual a: {parte1}{parte2}'
            print(valor_dolar)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


pegando_dolar_by_request()

