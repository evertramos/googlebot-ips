import os
import requests 
            
"""
Download Google's IP addresses for verification purposes.
from: https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot?hl=pt-br
"""


def baixar_arquivos_googlebots():
    urls = {
        "googlebot": "https://developers.google.com/search/apis/ipranges/googlebot.json",
        "special-crawlers": "https://developers.google.com/search/apis/ipranges/special-crawlers.json",
        "user-triggered-fetchers": "https://developers.google.com/search/apis/ipranges/user-triggered-fetchers.json",
        "user-triggered-fetchers-google": "https://developers.google.com/search/apis/ipranges/user-triggered-fetchers-google.json"
    }

    try:
        # for url in urls.values():
            # response = requests.get(url)
            # response.raise_for_status()
        # print("Todos os arquivos foram baixados com sucesso.")
        for nome, url in urls.items():
            r = requests.get(url)
            with open(f"{nome}.json", "w") as f:
                f.write(r.text)
            print(f"{nome}.json salvo.")
            print("Salvo em:", os.getcwd())

    except requests.RequestException as e:
        print(f"Erro ao baixar os arquivos: {e}")
