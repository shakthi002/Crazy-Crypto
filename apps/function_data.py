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
from keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np


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
