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
from keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense



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
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 1:
                df_eth = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 2:
                df_ada = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 3:
                df_avax = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 4:
                df_bnb = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 5:
                df_busd = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 6:
                df_dai = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 7:
                df_doge = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 8:
                df_dot = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 9:
                df_sol = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 10:
                df_trx = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 11:
                df_usdc = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 12:
                df_usdt = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 13:
                df_xrp = yf.download(
                tickers = coin,
                start = "2012-01-01",
                end = datetime.datetime.now()
                )

                continue

            if i == 14:
                df_wbtc = yf.download(
                tickers = coin,
                start = "2012-01-01",
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
       'WBTC-USD'))



    df_btc,df_eth,df_ada,df_avax,df_bnb,df_busd,df_dai,df_doge,df_dot,df_sol,df_trx,df_usdc,df_usdt,df_xrp,df_wbtc = load_data()





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

    st.subheader("Model for Crypto Currency Closing Prices Using LSTM")

    close_data = df['Close'].values
    close_data = close_data.reshape((-1,1))



    split_percent = 0.90
    split = int(split_percent*len(close_data))

    close_train = close_data[:split]
    close_test = close_data[split:]

    date_train = df.index[:split]
    date_test = df.index[split:]


    look_back = 15

    train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20)
    test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)



    model = Sequential()
    model.add(
        LSTM(10,
            activation='relu',
            input_shape=(look_back,1))
    )
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    num_epochs = 25
    model.fit_generator(train_generator, epochs=50, verbose=1)


    prediction = model.predict_generator(test_generator)

    close_train = close_train.reshape((-1))
    close_test = close_test.reshape((-1))
    prediction = prediction.reshape((-1))

    trace1 = go.Scatter(
        x = date_train,
        y = close_train,
        mode = 'lines',
        name = 'Data'
    )
    trace2 = go.Scatter(
        x = date_test,
        y = prediction,
        mode = 'lines',
        name = 'Prediction'
    )
    trace3 = go.Scatter(
        x = date_test,
        y = close_test,
        mode='lines',
        name = 'Ground Truth'
    )
    layout = go.Layout(
        title = f"{coin} Close Price Prediction",
        xaxis = {'title' : "Date"},
        yaxis = {'title' : "Close"},
        height=700,
        width=1300
    )
    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

    st.plotly_chart(fig)


    close_data = close_data.reshape((-1))

    def predict(num_prediction, model):
        prediction_list = close_data[-look_back:]

        for _ in range(num_prediction):
            x = prediction_list[-look_back:]
            x = x.reshape((1, look_back, 1))
            out = model.predict(x)[0][0]
            prediction_list = np.append(prediction_list, out)
        prediction_list = prediction_list[look_back-1:]

        return prediction_list

    def predict_dates(num_prediction):
        last_date = df.index.values[-1]
        prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
        return prediction_dates

    num_prediction = 30
    forecast = predict(num_prediction, model)
    forecast_dates = predict_dates(num_prediction)

    pred = pd.DataFrame(forecast,index=forecast_dates,columns=['Close'])

    fig =go.Figure()

    fig.add_trace(
        go.Scatter(x=df.index,y=df['Close'],name='Past Data')
    )

    fig.add_trace(
        go.Scatter(x=pred.index,y=pred['Close'],name='Predicted Future Data')
    )

    fig.update_layout(
        title = 'Bitcoin future price Prediction',
        yaxis_title = 'Stock Price in USD',
        height=700,
        width=1300
    )

    st.plotly_chart(fig)
