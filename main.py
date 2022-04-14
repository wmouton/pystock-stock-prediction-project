import streamlit as st
import yfinance as yf

from datetime import date
from fbprophet import yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("PyStock - Stock Prediction App")