# trader-sentiment-analysis
# Trader Performance vs Market Sentiment (Fear vs Greed)

## Objective
The objective of this project is to analyze how Bitcoin market sentiment
(Fear vs Greed) influences trader behavior and performance on the
Hyperliquid trading platform, and to derive actionable insights that
can inform smarter trading strategies.

## Datasets
1. Bitcoin Market Sentiment dataset containing daily Fear/Greed labels
2. Hyperliquid historical trader transaction data

## Methodology
- Loaded and validated both datasets (checked missing values and duplicates)
- Converted timestamps and aligned data at a daily level
- Aggregated trade-level data to account-day metrics
- Engineered key features such as daily PnL, win rate, trade frequency,
  average trade size, and long/short ratio
- Compared performance and behavior across Fear vs Greed market regimes
- Segmented traders based on activity level and consistency

## Key Insights
- Trader performance differs significantly between Fear and Greed periods,
  with Greed days showing higher average profitability.
- Traders increase trade frequency and position size during Greed,
  indicating more aggressive behavior.
- Consistent traders achieve more stable profitability than high-activity
  traders, highlighting the importance of disciplined trading behavior.

## Strategy Recommendations
- During Fear periods, high-activity traders should reduce trade frequency
  and exposure to limit drawdowns.
- During Greed periods, consistent traders can selectively increase
  participation due to improved win rates.

## How to Run
1. Install dependencies: `pip install pandas numpy matplotlib`
2. Open and run the Jupyter notebook end-to-end

(Optional)
- To run the Streamlit dashboard: `streamlit run app.py`
