import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
import datetime
import keras
import tensorflow as tf
import numpy as np



def app():

    def load_data_live():

        sorted_coin = ['BTC-USD',
        'ETH-USD',
        'ADA-USD',
        'AVAX-USD',
        'BNB-USD',
        'BUSD-USD',
        'DAI-USD',
        'DOGE-USD',
        'DOT-USD',
        'SOL-USD',
        'TRX-USD',
        'USDC-USD',
        'USDT-USD',
        'XRP-USD',
        'WBTC-USD',
        ]


        for i in range(0,len(sorted_coin),1):
            coin = sorted_coin[i]

            if i == 0:
                df_btc = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 1:
                df_eth = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 2:
                df_ada = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 3:
                df_avax = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 4:
                df_bnb = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 5:
                df_busd = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 6:
                df_dai = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 7:
                df_doge = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 8:
                df_dot = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 9:
                df_sol = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 10:
                df_trx = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 11:
                df_usdc = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 12:
                df_usdt = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 13:
                df_xrp = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

            if i == 14:
                df_wbtc = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='1m'
                )

                continue

        return df_btc,df_eth,df_ada,df_avax,df_bnb,df_busd,df_dai,df_doge,df_dot,df_sol,df_trx,df_usdc,df_usdt,df_xrp,df_wbtc

    @st.cache
    def load_data():
        sorted_coin = ['BTC-USD',
        'ETH-USD',
        'ADA-USD',
        'AVAX-USD',
        'BNB-USD',
        'BUSD-USD',
        'DAI-USD',
        'DOGE-USD',
        'DOT-USD',
        'SOL-USD',
        'TRX-USD',
        'USDC-USD',
        'USDT-USD',
        'XRP-USD',
        'WBTC-USD',
        ]


        for i in range(0,len(sorted_coin),1):
            coin = sorted_coin[i]

            if i == 0:
                df_btc = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 1:
                df_eth = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 2:
                df_ada = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 3:
                df_avax = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 4:
                df_bnb = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 5:
                df_busd = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 6:
                df_dai = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 7:
                df_doge = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 8:
                df_dot = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 9:
                df_sol = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 10:
                df_trx = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 11:
                df_usdc = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 12:
                df_usdt = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 13:
                df_xrp = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

            if i == 14:
                df_wbtc = yf.download(
                tickers = coin,
                start = datetime.datetime.now() - datetime.timedelta(days=1),
                end = datetime.datetime.now(),
                interval='15m'
                )

                continue

        return df_btc,df_eth,df_ada,df_avax,df_bnb,df_busd,df_dai,df_doge,df_dot,df_sol,df_trx,df_usdc,df_usdt,df_xrp,df_wbtc






    # Page layout
    # Page expands to full width
    # st.set_page_config(layout="wide")

    # ---------------------------------#
    # Title

    st.title("Crypto Price App")


    # ---------------------------------#
    # About
    expander_bar = st.expander("About")
    expander_bar.markdown(
        """
    * **This Project was done by Sriram**
    """
    )


    # ---------------------------------#
    # Page layout (continued)
    # Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
    col1 = st.sidebar
    # col2, col3 = st.columns((2, 1))

    # ---------------------------------#
    # Sidebar + Main panel
    col1.header("Input Options")

    # Sidebar - Currency price unit
    currency_price_unit = "USD"



    # Sidebar - Cryptocurrency selections
    sorted_coin = ['BTC-USD',
       'ETH-USD',
       'ADA-USD',
       'AVAX-USD',
       'BNB-USD',
       'BUSD-USD',
       'DAI-USD',
       'DOGE-USD',
       'DOT-USD',
       'SOL-USD',
       'TRX-USD',
       'USDC-USD',
       'USDT-USD',
       'XRP-USD',
       'WBTC-USD',
       ]

    # selected_coin = col1.multiselect("Cryptocurrency", sorted_coin, sorted_coin)
    # currency_price_unit = col1.selectbox("Select currency for price", ("USD", "BTC", "ETH"))

    coin = col1.radio(
     "Select a Crypto Currency",
     ('BTC-USD',
       'ETH-USD',
       'ADA-USD',
       'AVAX-USD',
       'BNB-USD',
       'BUSD-USD',
       'DAI-USD',
       'DOGE-USD',
       'DOT-USD',
       'SOL-USD',
       'TRX-USD',
       'USDC-USD',
       'USDT-USD',
       'XRP-USD',
       'WBTC-USD'))




    df_btc_live,df_eth_live,df_ada_live,df_avax_live,df_bnb_live,df_busd_live,df_dai_live,df_doge_live,df_dot_live,df_sol_live,df_trx_live,df_usdc_live,df_usdt_live,df_xrp_live,df_wbtc_live = load_data_live()

    df_btc,df_eth,df_ada,df_avax,df_bnb,df_busd,df_dai,df_doge,df_dot,df_sol,df_trx,df_usdc,df_usdt,df_xrp,df_wbtc = load_data()





    if coin == 'BTC-USD':
        df = df_btc.copy()
        df_live = df_btc_live.copy()

    if coin == 'ETH-USD':
        df = df_eth.copy()
        df_live = df_eth_live.copy()

    if coin == 'ADA-USD':
        df = df_ada.copy()
        df_live = df_ada_live.copy()

    if coin == 'AVAX-USD':
        df = df_avax.copy()
        df_live = df_avax_live.copy()

    if coin == 'BNB-USD':
        df = df_bnb.copy()
        df_live = df_bnb_live.copy()

    if coin == 'BUSD-USD':
        df = df_busd.copy()
        df_live = df_busd_live.copy()

    if coin == 'DAI-USD':
        df = df_dai.copy()
        df_live = df_dai_live.copy()

    if coin == 'DOGE-USD':
        df = df_doge.copy()
        df_live = df_doge_live.copy()

    if coin == 'DOT-USD':
        df = df_dot.copy()
        df_live = df_dot_live.copy()

    if coin == 'SOL-USD':
        df = df_sol.copy()
        df_live = df_sol_live.copy()

    if coin == 'TRX-USD':
        df = df_trx.copy()
        df_live = df_trx_live.copy()

    if coin == 'USDC-USD':
        df = df_usdc.copy()
        df_live = df_usdc_live.copy()

    if coin == 'USDT-USD':
        df = df_usdt.copy()
        df_live = df_usdt_live.copy()

    if coin == 'XRP-USD':
        df = df_xrp.copy()
        df_live = df_xrp_live.copy()

    if coin == 'WBTC-USD':
        df = df_wbtc.copy()
        df_live = df_wbtc_live.copy()

    st.subheader("Live Data")

    if coin in sorted_coin:
        st.write(
            "Data Dimension: "
            + str(10)
            + " rows and "
            + str(df.shape[1])
            + " columns."
        )

    st.table(df_live.tail(10))


    fig = go.Figure()

    fig.add_trace(go.Candlestick(x=df.index,
                                 open = df['Open'],
                                 high = df['High'],
                                 low = df['Low'],
                                 close = df['Close'],name='market data'))

    fig.update_layout(
        title = 'Bitcoin live share price',
        yaxis_title = 'Stock Price in USD',
        height=700,
        width=1000
    )

    fig.update_xaxes(
        rangeslider_visible = False,
        rangeselector = dict(
            buttons = list([
                    dict(count=15,label='15m',step='minute',stepmode='backward'),
                    dict(count=45,label='45m',step='minute',stepmode='backward'),
                    dict(count=1,label='HTD',step='hour',stepmode='todate'),
                    dict(count=6,label='6h',step='hour',stepmode='todate'),
                    dict(step='all'),
            ])
        )
    )

    st.plotly_chart(fig)
