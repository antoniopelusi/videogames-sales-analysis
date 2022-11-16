# videogames-sales-analysis
Analisi esplorativa e di correlazione tra le vendite di videogiochi e consoles nel mondo.

## Indice
0. **Introduzione**

1. **Collezione dei dati**

    - Dataset vendite videogiochi

    - Dataset vendite consoles

2. **Elaborazione dei dati**

    - Pulizia dei dataset

    - Controllo validità delle vendite globali

    - Controllo editori con pochi giochi pubblicati

3. **Analisi esplorativa**
    
    - Dataset videogames
    
    - Dataset consoles

4. **Testing**
    - Calcolo correlazione tra le vendite dei videogiochi nelle varie regioni

    - Calcolo della correlazione monotona tra la vendita di una console e la vendita dei videogiochi sviluppati per la stessa console

    - Calcolo della correlazione monotona tra il numero di videogiochi sviluppati e le vendite di videogiochi
    
5. **Risultati e conclusioni**

## Files della repository
- Analisi scritta in **Python** su un **notebook Jupyter** *(videogames-sales-analysis.ipynb)*, utilizza le seguenti librerie:
  - **Pandas** (Importazione dei datasets)
  - **NumPy** (Funzioni matematiche)
  - **MissingNo** (Visualizzazione valori nulli nei datasets)
  - **MatPlotLib** (Grafici e statistiche)
  - **Seaborn** (Grafici e statistiche)
- Script per lo scraping dei videogiochi da [vgChartz](https://www.vgchartz.com/gamedb/) scritto in **Python** *(vgchartz-scraper.ipynb)*
- Dataset vendite dei videogiochi ricavato dallo scraping di [vgChartz](https://www.vgchartz.com/gamedb/) *(vgsales.csv)*
- Dataset vendite di console recuperato da [Kaggle.com](https://www.kaggle.com/datasets/jaimepazlopes/game-console-manufactor-and-sales) *(console.csv)*
