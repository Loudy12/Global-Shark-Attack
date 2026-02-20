# Global Shark Attack Analysis

An R-based data analysis project exploring patterns in global shark incidents.  
Includes data cleaning, exploratory analysis, and statistical testing (including chi-squared tests).

## Questions Explored
This project investigates questions such as:
- Where do shark incidents occur most often?
- How do incident characteristics vary by activity (surfing, swimming, fishing, etc.)?
- Are certain variables statistically related (tested with chi-squared)?

## Tech Stack
- R / RStudio
- R Markdown (`.Rmd`)
- Tidyverse (dplyr, ggplot2, etc.)

## Repo Structure
- `data/` — dataset(s) used in the analysis
- `*.Rmd` — R Markdown report(s)
- `docs/` or output files — exported report/figures (if included)

## How To Run
### Option A: Knit the R Markdown report (recommended)
1. Open the `.Rmd` file in RStudio
2. Install packages if prompted
3. Click **Knit** to generate the report (HTML/PDF depending on your settings)


## Key Methods
- Data cleaning (handling missing values + inconsistent categories)
- Exploratory analysis and visualization
- **Chi-squared tests** to evaluate whether certain categorical variables are related


## Notes on Data
Dataset source: https://sharkattackfile.net/  
This repo is for educational analysis and does not claim causation—only observed relationships in the dataset.

## Author
Connor Loudermilk  
GitHub: https://github.com/Loudy12
