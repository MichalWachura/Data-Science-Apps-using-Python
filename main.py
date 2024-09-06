import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Apple !

""")

#define a ticker symbol

tickerSymbol = 'AAPL'

#get data in this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period="1d",start="2010-5-31",end="2020-5-31")

#open High Low Close Volume Dividends Stocks Splits
st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)





