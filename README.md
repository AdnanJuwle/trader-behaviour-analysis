


# Trader Behavior Analysis

**Analyzing how trader behavior correlates with the crypto market's Fear & Greed Index.**

---

## Overview

This project explores the relationship between trader performance and market sentiment by examining historical trade data alongside the Crypto Fear & Greed Index. The objective is to uncover patterns in metrics such as profit and loss (PnL), trade size, and buy/sell ratios across varying emotional states of the market.

---

## Project Structure

```
trader-behavior-analysis/
├── data/
│   ├── fear_greed_index.csv         # Daily sentiment scores
│   └── historical_data.csv          # Trader PnL, size, and direction
├── src/
│   ├── __init__.py
│   ├── data_processing.py           # Data loading and cleaning functions
│   ├── feature_engineering.py       # Feature extraction and transformation
│   ├── analysis.py                  # Core statistical analysis
│   └── visualization.py             # Plotting and visual reporting
├── notebooks/
│   └── analysis.ipynb               # Interactive EDA and exploratory modeling
├── reports/
│   └── insights.md                  # Summary of key insights and observations
├── run_analysis.py                  # Main script to execute the full pipeline
├── requirements.txt                 # Python dependencies
├── README.md
```

---

## How to Run

1. **Clone the repository**

   ```bash
   git clone git@github.com:AdnanJuwle/trader-behaviour-analysis.git
   cd trader-behaviour-analysis
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main analysis**

   ```bash
   python3 run_analysis.py
   ```

4. *(Optional)* Explore the Jupyter notebook:

   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```

---

## Features and Analysis

* **Data Integration**: Automated loading and merging of sentiment and trading datasets.
* **Feature Engineering**: Computation of daily PnL, trade size, buy/sell ratios, and behavioral tagging.
* **Statistical Methods**: Includes ANOVA, correlation, and significance testing.
* **Visualization**: Graphical summaries of behavior under different sentiment classes.
* **Reporting**: Final insights and recommendations are documented in `reports/insights.md`.

---

## Notes

* Leverage-based analysis is excluded due to missing leverage data.
* All findings are based on available columns such as PnL, trade size, and trade direction.
* Ensure `data/` contains valid CSVs or modify paths as needed in `run_analysis.py`.

---

## Requirements

See `requirements.txt` for full dependency list.

Typical requirements include:

```
pandas
numpy
matplotlib
seaborn
scipy
```

---

