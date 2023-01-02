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
from pages import MultiPage
from apps import crypto,eda,model,live

app = MultiPage()

# Page layout
# Page expands to full width
st.set_page_config(layout="wide")



# app.add_page("Home",crypto.app)
app.add_page("Analysis",eda.app)
app.add_page("Forecasting",model.app)
app.add_page("Live Data",live.app)

app.run()
