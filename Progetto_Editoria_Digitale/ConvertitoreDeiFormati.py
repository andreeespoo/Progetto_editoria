# convertitore_formati.py
import yaml
import subprocess

def load_metadata(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def convert_with_pandoc(input_files, output_file, metadata_file,  pdf_engine='pdflatex'):
    command = [
        'pandoc', *input_files,
        '--metadata-file', metadata_file,
        '--output', output_file
    ]
    if pdf_engine:
        command.extend(['--pdf-engine', pdf_engine])

    try:
        subprocess.run(command, check=True)
        print(f"Generato con successo: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Errore nella generazione di {output_file}: {e}")

def main():
    yaml_file = 'Metadati.YAML'
    metadata = load_metadata(yaml_file)

    input_files = metadata.get('gestione_documentale', {}).get('input_files', [])
    output_formats = metadata.get('gestione_documentale', {}).get('output_formats', [])

    if not input_files:
        print("Nessun file di input specificato nel file YAML.")
        return

    for format in output_formats:
        output_file = f"output.{format}"
        convert_with_pandoc(input_files, output_file, yaml_file)

if __name__ == "__main__":
    main()
