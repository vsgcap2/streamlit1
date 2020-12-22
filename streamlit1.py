import streamlit as st
import pandas as pd 
from PIL import Image

st.write("""
Thiru Praturi's Stock Market Web Application..\n
This is testing waters (a warmup exercise) using Python based Web Apps where you can select a stock and look at its price chart\n
A **Lot MORE** coming very soon on this site (including Predictive Analysis and Portfolio Optimization tools)
""")

image = Image.open("image1.JPG")
st.image(image,use_column_width=True)
st.sidebar.header ("User Input")

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2017-09-20")
    end_date = st.sidebar.text_input("End Date", "2018-03-25")
    stock_symbol = st.sidebar.text_input("Symbol", "AAPL")
    return start_date, end_date, stock_symbol

#option = st.selectbox('Symbol', ('AAPL','GOOG','INTC'))
#st.write('Stock Symbol:', option)

def get_data(start, end, symbol):
    if symbol.upper() == "AAPL":
        df = pd.read_csv("aaplDat.csv")
    elif symbol.upper() == "GOOG":
        df = pd.read_csv("googDat.csv")
    elif symbol.upper() == "INTC":
        df = pd.read_csv("intcDat.csv")
    else:
        df = pd.DataFrame(columns = ['Date','Close','Open','High','Low','Adj. Close','Volume'])

    start= pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]

start, end, symbol = get_input()
df = get_data(start, end, symbol)

st.header(symbol+" Close Price\n")
st.line_chart(df['Close'])

st.header(symbol+ " Volume\n")
st.line_chart(df['Volume'])

st.header('Data Statistics')
st.write(df.describe())











