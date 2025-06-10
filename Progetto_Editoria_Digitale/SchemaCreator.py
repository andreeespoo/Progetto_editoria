import yaml
import json
import os
def load_yaml(yaml_file):
    print("Current working directory:", os.getcwd())
    """Carica il file YAML."""
    with open(yaml_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
yaml_file = r"Metadati.YAML"
data = load_yaml(yaml_file)


def convert_to_onix(data):  #converte in onix
    """Converte i metadati YAML nel formato ONIX."""
    onix = {  #faccio un mapping degli attributi
        "Product": {
            "Title": data["distribuzione"]["onix"]["title"], #ho l'attributo distribuzione, all'interno di distribuzione onix e poi ho i diversi attributi
            "Contributor": { #faccio un mapping del vocabolario,se ho gia utilizzato un vocabolario compatibile con onix sto semplicemente riscrivendo questo contenuto 
                "PrimaryAuthor": data["distribuzione"]["onix"]["contributor"]["primary_author"],
                "OtherAuthors": data["distribuzione"]["onix"]["contributor"]["other_authors"],
            },
            "Publisher": data["distribuzione"]["onix"]["publisher"],
            "PublicationDate": data["distribuzione"]["onix"]["publication_date"],
            "ISBN": data["distribuzione"]["onix"],
            "Audience": data["distribuzione"]["onix"]["audience"],
            "Format": data["distribuzione"]["onix"]["format"],
            "Price": data["distribuzione"]["onix"]["price"],
        }
    }
    return onix

def convert_to_schema_org(data): #la conversione su schema.org
    """Converte i metadati YAML nel formato Schema.org."""
    schema_org = { #attributi necessari per lo schema.org (context,type...)
        "@context": "https://schema.org",
        "@type": "Book",
        "name": data["distribuzione"]["schema_org"]["name"],
        "author": [ #inizio a mappare i diversi attributi
            { #nel momento devo creare un elemento complesso devo dichiarare tutto
                "@type": "Person",
                "name": author["name"]
            } for author in data["distribuzione"]["schema_org"]["author"]
        ],
        "datePublished": data["distribuzione"]["schema_org"]["datePublished"],
        "publisher": {
            "@type": "Organization",
            "name": data["distribuzione"]["schema_org"]["publisher"]["name"]
        },
        "genre": data["distribuzione"]["schema_org"]["genre"],
        "language": data["distribuzione"]["schema_org"]["language"],
        "inLanguage": data["distribuzione"]["schema_org"]["inLanguage"],
        "format": data["distribuzione"]["schema_org"]["format"],
    }
    return schema_org

def save_to_file(data, file_path, format="json"):  #funzione per salvataggio finale
    """Salva i dati in un file (ONIX o Schema.org)."""
    with open(file_path, "w", encoding="utf-8") as file:
        if format == "json":
            json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            file.write(str(data))  # Default string format
    print(f"Salvato in: {file_path}")

# Trasformazione ONIX
onix_data = convert_to_onix(data)
save_to_file(onix_data, "relazione_onix.json", format="json")

# Trasformazione Schema.org
schema_org_data = convert_to_schema_org(data)
save_to_file(schema_org_data, "relazione_schema_org.json", format="json")