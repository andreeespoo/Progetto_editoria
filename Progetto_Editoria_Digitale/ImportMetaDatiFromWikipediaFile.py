import requests
from bs4 import BeautifulSoup 
import yaml

def get_wikipedia_metadata(title, language):
    url = f"https://{language}.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": title,
        "format": "json",
        "prop": "text",
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "parse" in data and "text" in data["parse"]:
            return data["parse"]["text"]["*"]  # Contenuto HTML della pagina
        else:
            print(f"Nessun contenuto trovato per '{title}'.")
            return None
    else:
        print(f"Errore nel download della pagina: {response.status_code}")
        return None

def extract_metadata(html_content):
    soup = BeautifulSoup(html_content, "html.parser")    
    metadata = {}
    infobox = soup.find("table", class_="infobox") # Estrazione dati strutturati
    if infobox:
        rows = infobox.find_all("tr")
        for row in rows:
            if row.th and row.td:
                key = row.th.get_text(strip=True)
                value = row.td.get_text(strip=True)
                metadata[key] = value
    cda_section = soup.find("table", class_="metadata plainlinks") # Estrazione del Controllo di Autorità(CdA)
    if cda_section:
        links = cda_section.find_all("a", href=True)
        metadata["Controllo_di_autorità"] = {link.text: link["href"] for link in links}
    return metadata

def save_metadata_to_yaml(metadata, filename):
    with open(filename, "w", encoding="utf-8") as file:
        yaml.dump(metadata, file, allow_unicode=True, default_flow_style=False)
    print(f"Metadati salvati in '{filename}'.")

#Input
page_title = "Giochi della II Olimpiade"
language = "it"

html_content = get_wikipedia_metadata(page_title, language)
if html_content:
    metadata = extract_metadata(html_content)
    print("Metadati trovati:")
    print(yaml.dump(metadata, allow_unicode=True, default_flow_style=False))  # Anteprima
    save_metadata_to_yaml(metadata, f"{page_title}_metadata.yaml")