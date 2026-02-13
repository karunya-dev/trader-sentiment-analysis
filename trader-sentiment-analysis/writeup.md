# Trader Performance vs Market Sentiment – Summary

## Objective
This project analyzes the relationship between Bitcoin market sentiment
(Fear vs Greed) and trader behavior and performance on the Hyperliquid
platform, with the goal of identifying actionable trading insights.

## Data & Methodology
Two datasets were used: a daily Bitcoin Fear/Greed sentiment dataset and
historical Hyperliquid trader transaction data. After validating data
quality, timestamps were aligned at a daily level. Trade-level data was
aggregated per account per day to compute performance and behavior metrics
such as daily PnL, win rate, trade frequency, average trade size, and
long/short ratio.

## Key Insights
1. Trader performance varies significantly across sentiment regimes, with
   Greed days exhibiting higher average PnL and win rates.
2. Traders tend to increase trading frequency and position size during
   Greed periods, reflecting more aggressive behavior.
3. Consistent traders demonstrate more stable profitability compared to
   high-activity traders, emphasizing disciplined trading over volume.

## Actionable Strategies
1. During Fear periods, high-activity traders should reduce exposure and
   trade frequency to control drawdowns.
2. During Greed periods, consistent traders can cautiously increase
   participation, as sentiment conditions favor higher success rates.

## Conclusion
Market sentiment plays a meaningful role in shaping trader behavior and
outcomes. Incorporating sentiment-aware rules into trading strategies can
improve risk management and decision-making.
