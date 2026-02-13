import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment")
st.markdown(
    "Interactive dashboard to explore how **Fear vs Greed** market sentiment "
    "impacts trader behavior and performance on Hyperliquid."
)

@st.cache_data
def load_data():
    sentiment = pd.read_csv(r"C:\Users\Karunya S\Documents\trader-sentiment-analysis\data\fear_greed_index.csv")

    trades= pd.read_csv(r"C:\Users\Karunya S\Documents\trader-sentiment-analysis\data\historical_data.csv")


    # Sentiment processing
    sentiment['timestamp'] = pd.to_datetime(sentiment['timestamp'])
    sentiment['date'] = sentiment['timestamp'].dt.date

    # Trader processing
    trades['Timestamp'] = pd.to_datetime(trades['Timestamp'])
    trades['date'] = trades['Timestamp'].dt.date

    daily_trades = trades.groupby(['Account', 'date']).agg(
        daily_pnl=('Closed PnL', 'sum'),
        trade_count=('Closed PnL', 'count'),
        avg_trade_size=('Size USD', 'mean'),
        long_trades=('Side', lambda x: (x == 'BUY').sum()),
        short_trades=('Side', lambda x: (x == 'SELL').sum())
    ).reset_index()

    daily_trades['long_short_ratio'] = (
        daily_trades['long_trades'] / (daily_trades['short_trades'] + 1)
    )

    merged = daily_trades.merge(
        sentiment[['date', 'classification']],
        on='date',
        how='left'
    )

    merged['win'] = merged['daily_pnl'] > 0

    win_rate = (
        merged.groupby('Account')['win']
        .mean()
        .reset_index(name='win_rate')
    )

    merged = merged.merge(win_rate, on='Account', how='left')
    merged['drawdown_proxy'] = merged['daily_pnl'].clip(upper=0)

    merged['activity_segment'] = pd.qcut(
        merged['trade_count'], q=2,
        labels=['Low Activity', 'High Activity']
    )

    merged['consistency_segment'] = merged['win_rate'].apply(
        lambda x: 'Consistent' if x >= 0.5 else 'Inconsistent'
    )

    return merged

df = load_data()

st.sidebar.header("🔎 Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Market Sentiment",
    options=df['classification'].dropna().unique(),
    default=df['classification'].dropna().unique()
)

activity_filter = st.sidebar.multiselect(
    "Select Activity Segment",
    options=df['activity_segment'].unique(),
    default=df['activity_segment'].unique()
)

filtered_df = df[
    (df['classification'].isin(sentiment_filter)) &
    (df['activity_segment'].isin(activity_filter))
]

st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Daily PnL",
    round(filtered_df['daily_pnl'].mean(), 2)
)

col2.metric(
    "Win Rate",
    f"{round(filtered_df['win'].mean() * 100, 2)}%"
)

col3.metric(
    "Avg Trades / Day",
    round(filtered_df['trade_count'].mean(), 2)
)

st.subheader("🔥 Performance by Market Sentiment")

perf = filtered_df.groupby('classification')[['daily_pnl', 'win']].mean()
st.dataframe(perf)

fig, ax = plt.subplots()
perf['daily_pnl'].plot(kind='bar', ax=ax)
ax.set_title("Average Daily PnL by Sentiment")
ax.set_ylabel("Daily PnL")
st.pyplot(fig)

st.subheader("👥 Trader Segmentation")

seg = filtered_df.groupby('consistency_segment')[
    ['daily_pnl', 'trade_count']
].mean()

st.dataframe(seg)
