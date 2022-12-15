# videogames-sales-analysis

Exploratory analysis and correlation between sales of video games and consoles in the world.

## Index
0. **Introduction**

1. **Data Collection**

     - Video game sales dataset

     - Console sales dataset

2. **Data Processing**

     - Cleanup of datasets

     - Validity check of global sales

     - Publisher control with few published games

3. **Exploratory analysis**
    
     - Videogame datasets
    
     - Dataset consoles

4. **Testing**
     - Correlation calculation between video game sales in the various regions

     - Calculation of the monotonic correlation between the sale of a console and the sale of videogames developed for the same console

     - Calculation of the monotonic correlation between the number of video games developed and video game sales
    
5. **Results and conclusions**

## Repository files
- Analysis written in **Python** on a **Jupyter notebook** *(videogames-sales-analysis.ipynb)*, uses the following libraries:

   - **Pandas** (Import of datasets)
   
   - **NumPy** (Math functions)
   
   - **MissingNo** (Displaying null values in datasets)
   
   - **MatPlotLib** (Graphs and statistics)
   
   - **Seaborn** (Charts and stats)
   
- Game scraping script from [vgChartz](https://www.vgchartz.com/gamedb/) written in **Python** *(vgchartz-scraper.ipynb)*

- Video game sales dataset obtained from the scraping of [vgChartz](https://www.vgchartz.com/gamedb/) *(vgsales.csv)*

- Console sales dataset retrieved from [Kaggle.com](https://www.kaggle.com/datasets/jaimepazlopes/game-console-manufactor-and-sales) *(console.csv)*
