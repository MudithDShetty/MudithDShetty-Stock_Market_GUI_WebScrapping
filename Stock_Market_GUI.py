from tkinter import *
import tkinter as tk
import pandas as pd
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
import plotly.graph_objs as go
from PIL import ImageTk, Image
import plotly.express
from datetime import date, timedelta
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

##################################################################################################################
stock_code=''
#####################################################################################################################
def search():
    global stock_code
    stock_code=enter_1.get()
    root.destroy()
    main2()
def search2():
    global stock_code
    stock_code = enter_1.get()
    lol.destroy()
    main()
def des():
    global stock_code
    stock_code = enter_1.get()
    win.destroy()
    main()
######################################################################################################################
def mf():
    yf.pdr_override()
    df = yf.download(tickers=stock_code, period='1d', interval='1m')

    print(df)
    fig = go.Figure()

    fig.add_trace(go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'], name='market data'))

    fig.update_layout(
        title=str(stock_code) + ' Live Share Price:',
        yaxis_title='Stock Price (USD per Shares)')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.show()
#######################################################################################################################
Start = date.today() - timedelta(365)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')
def closing_price(ticker):
    plot = pd.DataFrame(yf.download(ticker, start=Start,
      end=End)['Adj Close'])
    return plot


#########################################################################################################################
def main():
    global root
    url = f"https://finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=fin-srch"
    r = requests.get(url).text
    a = BeautifulSoup(r, 'lxml')
    name = a.find("div", {"id": "mrt-node-Lead-5-QuoteHeader"}).get_text()
    #################################################################################################################
    prev_close = a.find("td", {"data-test": "PREV_CLOSE-value"}).get_text()
    bid = a.find("td", {"data-test": "BID-value"}).get_text()
    ask = a.find("td", {"data-test": "ASK-value"}).get_text()
    days = a.find("td", {"data-test": "DAYS_RANGE-value"}).get_text()
    weeks = a.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).get_text()
    vol = a.find("td", {"data-test": "TD_VOLUME-value"}).get_text()
    avg_vol = a.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).get_text()
    op = a.find("td", {"data-test": "OPEN-value"}).get_text()
    ################################################################################################################
    cap = a.find("td", {"data-test": "MARKET_CAP-value"}).get_text()
    beta = a.find("td", {"data-test": "BETA_5Y-value"}).get_text()
    pe = a.find("td", {"data-test": "PE_RATIO-value"}).get_text()
    earn = a.find("td", {"data-test": "EARNINGS_DATE-value"}).get_text()
    eps = a.find("td", {"data-test": "EPS_RATIO-value"}).get_text()
    divandyeild = a.find("td", {"data-test": "DIVIDEND_AND_YIELD-value"}).get_text()
    exdiv = a.find("td", {"data-test": "EX_DIVIDEND_DATE-value"}).get_text()
    target = a.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).get_text()
    namereal = ''
    for i in name:
        if ')' == i:
            namereal += i
            break
        else:
            namereal += i
    b = a.find("div", {"class": "D(ib) Mend(20px)"}).get_text()
    stock_rate = a.find("fin-streamer", {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    stock_porl = a.find("fin-streamer", {'class': "Fw(500) Pstart(8px) Fz(24px)"}).get_text()
    h = a.find("div", {"class": "D(ib) Mend(20px)"}).get_text()
    l = b.split()
    global enter_1
    root = Tk()
    root.title("Stock Market Application")
    root.geometry("2000x2000")
    root.config(bg='#222222')
    enter_1 = Entry(root, width=90)
    enter_1.place(x=370, y=40)
    label = tk.Label(root, text="Enter The Stock code", fg="white", bg='#222222', font=('Times', 22)).place(x=50, y=30)
    button_border = tk.Frame(root, highlightbackground="#39FF14", highlightthickness=100, bd=10).place(x=1000, y=40)
    bttn = tk.Button(button_border, text='Search', fg='#39FF14', bg='#4A4357', font=(("Times New Roman"), 15),
                     command=search).place(x=1000, y=40)
    name_label = Label(root, text=namereal + '                \n' +
                                  '                \n' +
                                  '                \n'
                                  '                \n'
                                  '                \n', fg="white", bg='#4A4357', font=('Times', 22, 'bold')).place(
        x=100, y=100)

    ##################################################################################################################################
    Prev = Label(root, text=f'Previous Close            {prev_close}                  ', fg="white", bg='#4A4357',
                 font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=100)
    Bid = Label(root, text=f'Bid                              {bid}         ', fg="white", bg='#4A4357',
                font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=150)
    Ask = Label(root, text=f'Ask                              {ask}        ', fg="white", bg='#4A4357',
                font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=200)
    Days = Label(root, text=f'Days Range                 {days}      ', fg="white", bg='#4A4357', font=('Times', 22),
                 borderwidth=5, relief="solid").place(x=700, y=250)
    Weeks = Label(root, text=f'52 Weeks Range         {weeks}    ', fg="white", bg='#4A4357', font=('Times', 22),
                  borderwidth=5, relief="solid").place(x=700, y=300)
    Vol = Label(root, text=f'Volume                       {vol}         ', fg="white", bg='#4A4357', font=('Times', 22),
                borderwidth=5, relief="solid").place(x=700, y=350)
    Avg = Label(root, text=f'Average Volume         {avg_vol}         ', fg="white", bg='#4A4357', font=('Times', 22),
                borderwidth=5, relief="solid").place(x=700, y=400)
    opn = Label(root, text=f'Open                            {op}                  ', fg="white", bg='#4A4357',
                font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=450)
    #################################################################################################################################
    Market_Cap = Label(root,
                       text=f'Market Cap                                 {cap}                                   ',
                       fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=100)
    Beta = Label(root, text=f'Beta (5Y Monthly)                     {beta}                                      ',
                 fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=150)
    PE_Ratio = Label(root, text=f'PE Ratio (TTM)                        {pe}                                     ',
                     fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=200)
    EPS = Label(root, text=f'EPS (TTM)                               {eps}                                       ',
                fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=250)
    Earnings = Label(root, text=f'Earnings Date                            {earn}', fg="white", bg='#4A4357',
                     font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=300)
    DivandYield = Label(root, text=f'Foward Divident & Yield         {divandyeild}                         ',
                        fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150,
                                                                                                           y=350)
    Ex_div = Label(root, text=f'Ex-Divident Date                      {exdiv}                        ', fg="white",
                   bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=400)
    Target = Label(root, text=f'1y Target Est                            {target}                                     ',
                   fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=450)
    ##################################################################################################################################3
    Price = Label(root, text=stock_rate, fg='white', bg='#4A4357', font=('Times', 50)).place(x=100, y=150)
    if '-' in stock_porl:
        Profit = Label(root, text=stock_porl, fg='red', bg='#4A4357', font=('Times', 24)).place(x=100, y=250)
        P = Label(root, text=l[1][0:-2], fg='red', bg='#4A4357', font=('Times', 24)).place(x=200, y=250)
    else:
        Profit = Label(root, text=stock_porl, fg='#39FF14', bg='#4A4357', font=('Times', 24)).place(x=100, y=250)
        P = Label(root, text=l[1][0:-2], fg='#39FF14', bg='#4A4357', font=('Times', 24)).place(x=200, y=250)
    button_border1 = tk.Frame(root, highlightbackground="#39FF14", highlightthickness=100, bd=10).place(x=100, y=350)
    bttn1 = tk.Button(button_border1, text='More info', fg='#39FF14', bg='#4A4357', font=(("Times New Roman"), 15),
                      command=mf).place(x=100, y=350)
    stock_plot = closing_price(stock_code)
    plt.figure(facecolor='#4A4357')
    plt.xlabel("Dates")
    plt.rcParams.update({'text.color': "#39FF14"})
    ax = plt.axes()
    ax.xaxis.label.set_color('#39FF14')
    ax.yaxis.label.set_color('#39FF14')
    ax.tick_params(axis="x", colors="#39FF14")
    ax.tick_params(axis="y", colors="#39FF14")
    ax.spines['bottom'].set_color('#39FF14')
    ax.spines['left'].set_color('#39FF14')
    plt.ylabel("Stock Price(USD)")
    plt.title(namereal)
    plt.grid()
    plt.plot(stock_plot)
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0, padx=50, pady=50)
    canvas.get_tk_widget().pack()
    bttn.pack()
    bttn1.pack()
    root.mainloop()
##############################################################################################
def main2():
    global lol
    url = f"https://finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=fin-srch"
    r = requests.get(url).text
    a = BeautifulSoup(r, 'lxml')
    name = a.find("div", {"id": "mrt-node-Lead-5-QuoteHeader"}).get_text()
    #################################################################################################################
    prev_close = a.find("td", {"data-test": "PREV_CLOSE-value"}).get_text()
    bid = a.find("td", {"data-test": "BID-value"}).get_text()
    ask = a.find("td", {"data-test": "ASK-value"}).get_text()
    days = a.find("td", {"data-test": "DAYS_RANGE-value"}).get_text()
    weeks = a.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).get_text()
    vol = a.find("td", {"data-test": "TD_VOLUME-value"}).get_text()
    avg_vol = a.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).get_text()
    op = a.find("td", {"data-test": "OPEN-value"}).get_text()
    ################################################################################################################
    cap = a.find("td", {"data-test": "MARKET_CAP-value"}).get_text()
    beta = a.find("td", {"data-test": "BETA_5Y-value"}).get_text()
    pe = a.find("td", {"data-test": "PE_RATIO-value"}).get_text()
    earn = a.find("td", {"data-test": "EARNINGS_DATE-value"}).get_text()
    eps = a.find("td", {"data-test": "EPS_RATIO-value"}).get_text()
    divandyeild = a.find("td", {"data-test": "DIVIDEND_AND_YIELD-value"}).get_text()
    exdiv = a.find("td", {"data-test": "EX_DIVIDEND_DATE-value"}).get_text()
    target = a.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).get_text()
    namereal = ''
    for i in name:
        if ')' == i:
            namereal += i
            break
        else:
            namereal += i
    b = a.find("div", {"class": "D(ib) Mend(20px)"}).get_text()
    stock_rate = a.find("fin-streamer", {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    stock_porl = a.find("fin-streamer", {'class': "Fw(500) Pstart(8px) Fz(24px)"}).get_text()
    h = a.find("div", {"class": "D(ib) Mend(20px)"}).get_text()
    l = b.split()
    global enter_1
    lol = Tk()
    lol.title("Stock Market Application")
    lol.geometry("2000x2000")
    lol.config(bg='#222222')
    enter_1 = Entry(lol, width=90)
    enter_1.place(x=370, y=40)
    label = tk.Label(lol, text="Enter The Stock code", fg="white", bg='#222222', font=('Times', 22)).place(x=50, y=30)
    button_border = tk.Frame(lol, highlightbackground="#39FF14", highlightthickness=100, bd=10).place(x=1000, y=40)
    bttn = tk.Button(button_border, text='Search', fg='#39FF14', bg='#4A4357', font=(("Times New Roman"), 15),
                     command=search2).place(x=1000, y=40)
    name_label = Label(lol, text=namereal + '                \n' +
                                  '                \n' +
                                  '                \n'
                                  '                \n'
                                  '                \n', fg="white", bg='#4A4357', font=('Times', 22, 'bold')).place(
        x=100, y=100)
##################################################################################################################################
    Prev = Label(lol, text=f'Previous Close            {prev_close}                  ', fg="white", bg='#4A4357',
                 font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=100)
    Bid = Label(lol, text=f'Bid                              {bid}         ', fg="white", bg='#4A4357',
                font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=150)
    Ask = Label(lol, text=f'Ask                              {ask}        ', fg="white", bg='#4A4357',
                font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=200)
    Days = Label(lol, text=f'Days Range                 {days}      ', fg="white", bg='#4A4357', font=('Times', 22),
                 borderwidth=5, relief="solid").place(x=700, y=250)
    Weeks = Label(lol, text=f'52 Weeks Range         {weeks}    ', fg="white", bg='#4A4357', font=('Times', 22),
                  borderwidth=5, relief="solid").place(x=700, y=300)
    Vol = Label(lol, text=f'Volume                       {vol}         ', fg="white", bg='#4A4357', font=('Times', 22),
                borderwidth=5, relief="solid").place(x=700, y=350)
    Avg = Label(lol, text=f'Average Volume         {avg_vol}         ', fg="white", bg='#4A4357', font=('Times', 22),
                borderwidth=5, relief="solid").place(x=700, y=400)
    opn = Label(lol, text=f'Open                            {op}                  ', fg="white", bg='#4A4357',
                font=('Times', 22), borderwidth=5, relief="solid").place(x=700, y=450)
    #################################################################################################################################
    Market_Cap = Label(lol,
                       text=f'Market Cap                                 {cap}                                   ',
                       fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=100)
    Beta = Label(lol, text=f'Beta (5Y Monthly)                     {beta}                                      ',
                 fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=150)
    PE_Ratio = Label(lol, text=f'PE Ratio (TTM)                        {pe}                                     ',
                     fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=200)
    EPS = Label(lol, text=f'EPS (TTM)                               {eps}                                       ',
                fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=250)
    Earnings = Label(lol, text=f'Earnings Date                            {earn}', fg="white", bg='#4A4357',
                     font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=300)
    DivandYield = Label(lol, text=f'Foward Divident & Yield         {divandyeild}                         ',
                        fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150,
                                                                                                           y=350)
    Ex_div = Label(lol, text=f'Ex-Divident Date                      {exdiv}                        ', fg="white",
                   bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=400)
    Target = Label(lol, text=f'1y Target Est                            {target}                                     ',
                   fg="white", bg='#4A4357', font=('Times', 22), borderwidth=5, relief="solid").place(x=1150, y=450)
    ##################################################################################################################################3
    Price = Label(lol, text=stock_rate, fg='white', bg='#4A4357', font=('Times', 50)).place(x=100, y=150)
    if '-' in stock_porl:
        Profit = Label(lol, text=stock_porl, fg='red', bg='#4A4357', font=('Times', 24)).place(x=100, y=250)
        P = Label(lol, text=l[1][0:-2], fg='red', bg='#4A4357', font=('Times', 24)).place(x=200, y=250)
    else:
        Profit = Label(lol, text=stock_porl, fg='#39FF14', bg='#4A4357', font=('Times', 24)).place(x=100, y=250)
        P = Label(lol, text=l[1][0:-2], fg='#39FF14', bg='#4A4357', font=('Times', 24)).place(x=200, y=250)
    button_border1 = tk.Frame(lol, highlightbackground="#39FF14", highlightthickness=100, bd=10).place(x=100, y=350)
    bttn1 = tk.Button(button_border1, text='More info', fg='#39FF14', bg='#4A4357', font=(("Times New Roman"), 15),
                      command=mf).place(x=100, y=350)
    stock_plot = closing_price(stock_code)
    plt.figure(facecolor='#4A4357')
    plt.xlabel("Dates")
    plt.rcParams.update({'text.color': "#39FF14"})
    ax = plt.axes()
    ax.xaxis.label.set_color('#39FF14')
    ax.yaxis.label.set_color('#39FF14')
    ax.tick_params(axis="x", colors="#39FF14")
    ax.tick_params(axis="y", colors="#39FF14")
    ax.spines['bottom'].set_color('#39FF14')
    ax.spines['left'].set_color('#39FF14')
    plt.ylabel("Stock Price(USD)")
    plt.title(namereal)
    plt.grid()
    plt.plot(stock_plot)
    canvas1 = FigureCanvasTkAgg(plt.gcf(), master=lol)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0, padx=50, pady=50)
    canvas1.get_tk_widget().pack()
    bttn.pack() 
    bttn1.pack()
    lol.mainloop()
###############################################################################################
win = Tk()
win.title("Stock Market Application")
win.geometry("2000x2000")
win.config(bg='#222222')
Title = tk.Label(win, text="Stock Market App", fg="#39FF14", bg='#222222', font=('Times', 50)).place(x=750, y=150)
Title = tk.Label(win, text="C106 Mudith D Shetty   C096 Samarth Roy Chowdhury", fg="#39FF14", bg='#222222', font=('Times', 30)).place(x=570, y=300)
label1 = tk.Label(win, text="Enter The Stock code", fg="white", bg='#222222', font=('Times', 30)).place(x=800, y=400)
button_border3 = tk.Frame(win, highlightbackground="#39FF14", highlightthickness=100, bd=10).place(x=1300, y=500)
bttn3 = tk.Button(button_border3, text='Search', fg='#39FF14', bg='#4A4357', font=(("Times New Roman"), 15),
                 command=des).place(x=1300, y=500)
enter_1 = Entry(win, width=90)
enter_1.place(x=700, y=500)
############################################################################################################################
file = open("C:\\Users\\ASUS\\Downloads\\Top 2000 Valued Companies with Ticker Symbols.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()
list1 = tk.StringVar(value=data)
lst = tk.Listbox(win,
                 listvariable=list1,width=50,bg='black',fg='green').place(x=820,y=600)
win.mainloop()