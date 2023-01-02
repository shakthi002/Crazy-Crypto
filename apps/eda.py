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
from plotly.subplots import make_subplots

def app():

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
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 1:
                df_eth = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 2:
                df_ada = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 3:
                df_avax = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 4:
                df_bnb = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 5:
                df_busd = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 6:
                df_dai = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 7:
                df_doge = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 8:
                df_dot = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 9:
                df_sol = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 10:
                df_trx = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 11:
                df_usdc = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 12:
                df_usdt = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 13:
                df_xrp = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 14:
                df_wbtc = yf.download(
                tickers = coin,
                start = "2021-01-01",
                end = datetime.datetime.now()
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
       'WBTC-USD',
       'Comparision'
       # 'All'
       ))



    df_btc,df_eth,df_ada,df_avax,df_bnb,df_busd,df_dai,df_doge,df_dot,df_sol,df_trx,df_usdc,df_usdt,df_xrp,df_wbtc = load_data()

    st.subheader("Sample Price Data of Selected Cryptocurrency")



    if coin == 'BTC-USD':
        df = df_btc.copy()

    if coin == 'ETH-USD':
        df = df_eth.copy()

    if coin == 'ADA-USD':
        df = df_ada.copy()

    if coin == 'AVAX-USD':
        df = df_avax.copy()

    if coin == 'BNB-USD':
        df = df_bnb.copy()

    if coin == 'BUSD-USD':
        df = df_busd.copy()

    if coin == 'DAI-USD':
        df = df_dai.copy()

    if coin == 'DOGE-USD':
        df = df_doge.copy()

    if coin == 'DOT-USD':
        df = df_dot.copy()

    if coin == 'SOL-USD':
        df = df_sol.copy()

    if coin == 'TRX-USD':
        df = df_trx.copy()

    if coin == 'USDC-USD':
        df = df_usdc.copy()

    if coin == 'USDT-USD':
        df = df_usdt.copy()

    if coin == 'XRP-USD':
        df = df_xrp.copy()

    if coin == 'WBTC-USD':
        df = df_wbtc.copy()

    if coin == 'Comparision':
        num_coin = col1.slider("Display Top N Coins", 2, 3, 3)

    if coin in sorted_coin:
        st.write(
            "Data Dimension: "
            + str(3)
            + " rows and "
            + str(df.shape[1])
            + " columns."
        )

        st.table(df.tail(3))

        def filedownload(df):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
            href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
            return href


        st.markdown(filedownload(df), unsafe_allow_html=True)

        # fig = px.line(df,x=df.index,y=df['Close'])
        # fig = px.line(df,x=df.index,y=['Close','Open'])
        fig =go.Figure()

        fig.add_trace(
            go.Scatter(x=df.index,y=df['Close'],name='Close')
        )

        fig.add_trace(
            go.Scatter(x=df.index,y=df['Open'],name='Open')
        )

        fig.update_layout(
            title = 'Open and Closing Prices',
            yaxis_title = 'Stock Price in USD',
            height=700,
            width=1300
        )


        st.text("")
        st.text("")
        st.text("")


        st.subheader(f'Opening and Closing Prices of {coin}')
        st.plotly_chart(fig)

        # fig_vol = px.line(df,x=df.index,y=df['Volume'])
        fig_vol =go.Figure()

        fig_vol.add_trace(
            go.Scatter(x=df.index,y=df['Volume'],name='Volume')
        )


        fig_vol.update_layout(
            title = 'Volume Sold',
            yaxis_title = 'Stock Price in USD',
            height=700,
            width=1300
        )

        st.text("")
        st.text("")
        st.text("")

        st.subheader(f'Volume of {coin} sold')
        st.plotly_chart(fig_vol)


    elif coin == 'Comparision':
        if num_coin == 2:
            fig =go.Figure()

            fig.add_trace(
                go.Scatter(x=df_btc.index,y=df_btc['Close'],name='Close_BTC')
            )

            fig.add_trace(
                go.Scatter(x=df_eth.index,y=df_eth['Close'],name='Close_ETH')
            )

            fig.update_layout(
                title = 'Open and Closing Prices',
                yaxis_title = 'Stock Price in USD',
                height=700,
                width=1300
            )


            st.text("")
            st.text("")
            st.text("")

            st.plotly_chart(fig)

            # fig_vol = px.line(df,x=df.index,y=df['Volume'])
            fig_vol =go.Figure()

            fig_vol.add_trace(
                go.Scatter(x=df_btc.index,y=df_btc['Volume'],name='Volume_BTC')
            )


            fig_vol.add_trace(
                go.Scatter(x=df_eth.index,y=df_eth['Volume'],name='Volume_ETH')
            )


            fig_vol.update_layout(
                title = 'Volume Sold',
                yaxis_title = 'Stock Price in USD',
                height=700,
                width=1300
            )

            st.text("")
            st.text("")
            st.text("")

            st.plotly_chart(fig_vol)

        elif num_coin == 3:
            fig =go.Figure()

            fig.add_trace(
                go.Scatter(x=df_btc.index,y=df_btc['Close'],name='Close_BTC')
            )

            fig.add_trace(
                go.Scatter(x=df_eth.index,y=df_eth['Close'],name='Close_ETH')
            )

            fig.add_trace(
                go.Scatter(x=df_usdt.index,y=df_usdt['Close'],name='Close_USDT')
            )

            fig.update_layout(
                title = 'Open and Closing Prices',
                yaxis_title = 'Stock Price in USD',
                height=700,
                width=1300
            )


            st.text("")
            st.text("")
            st.text("")

            st.plotly_chart(fig)

            # fig_vol = px.line(df,x=df.index,y=df['Volume'])
            fig_vol =go.Figure()

            fig_vol.add_trace(
                go.Scatter(x=df_btc.index,y=df_btc['Volume'],name='Volume_BTC')
            )


            fig_vol.add_trace(
                go.Scatter(x=df_eth.index,y=df_eth['Volume'],name='Volume_ETH')
            )

            fig_vol.add_trace(
                go.Scatter(x=df_usdt.index,y=df_usdt['Volume'],name='Volume_USDT')
            )


            fig_vol.update_layout(
                title = 'Volume Sold',
                yaxis_title = 'Stock Price in USD',
                height=700,
                width=1300
            )

            st.text("")
            st.text("")
            st.text("")

            st.plotly_chart(fig_vol)

        # elif coin == 'All':

        #     fig = make_subplots(rows=3,cols=1)

        #     fig.add_trace(
        #         go.Scatter(x=df_btc.index,y=df_btc['Close'],name='Close_BTC'),
        #         row=1,col=1
        #     )

        #     fig.add_trace(
        #         go.Scatter(x=df_eth.index,y=df_eth['Close'],name='Close_ETH'),
        #         row=2,col=1
        #     )

        #     fig.add_trace(
        #         go.Scatter(x=df_usdt.index,y=df_usdt['Close'],name='Close_USDT'),
        #         row=3,col=1
        #     )

        #     fig.update_layout(
        #         yaxis_title = 'Stock Price in USD',
        #         height=700,
        #         width=1300
        #     )


        #     st.text("")
        #     st.text("")
        #     st.text("")

        #     st.plotly_chart(fig)






