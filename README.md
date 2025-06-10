# I Giochi della II Olimpiade – Parigi 1900
Progetto editoriale digitale del Prof Ceravolo
Un progetto editoriale digitale che racconta la storia dei Giochi Olimpici di Parigi 1900.

## Descrizione del progetto

Questo progetto mira a documentare e raccontare la storia dei Giochi Olimpici di Parigi 1900, il primo evento olimpico ad includere le donne e caratterizzato da numerose discipline oggi scomparse.

Il progetto è strutturato in vari formati (PDF, ePub, HTML) ed è accessibile attraverso più canali.

## Output disponibili

I seguenti formati sono disponibili per il download:

### PDF
Puoi scaricare il PDF del progetto da [questo link](Progetto_Editoria_Digitale/output.pdf).

### ePub
Puoi scaricare l'ePub del progetto da [questo link](Progetto_Editoria_Digitale/output.epub).

### WebBook (HTML)
Puoi visualizzare o scaricare la versione WebBook (HTML) da [questo link](Progetto_Editoria_Digitale/output.html)

## Tecnologie utilizzate

- Markdown
- Pandoc
- LaTeX
- ePubCheck
- Git/GitHub

## Flusso di Produzione
```mermaid
flowchart LR
    A[Argomento Progetto] -->|Sport del 900'| B(Ricerca ed estrazione delle fonti)
    B --> C{Svolgimento tramite codici Python}
    C -->|1| D[Import dei dati da Wikipedia]
    C -->|2| E[Conversione nei tre formati: html, epub, pdf]
    C -->|3| F[Modifiche al markdown]
    C -->|2| G[Creazione schema.org e ONIX]
    D --> H(Modifiche estetiche al file .html tramite aggiunta .css)
    E --> H
    F --> H
    G --> H
    G --> I{Visualizzazione dei file completati}

