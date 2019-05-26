import pandas as pd
import os


def load_portfolio():

    path = os.path.dirname(os.path.realpath(__file__))

    port_path = '{}/test_portfolio.xlsx'.format(path)
    df = pd.read_excel(r'{}'.format(port_path))
    return df

def load_trade():
    path = os.path.dirname(os.path.realpath(__file__))
    trade_path = '{}/test_trading.xlsx'.format(path)
    df = pd.read_excel(r'{}'.format(trade_path))
    return df

def load_port():
    path = os.path.dirname(os.path.realpath(__file__))
    trade_path = '{}/test_port.xlsx'.format(path)
    df = pd.read_excel(r'{}'.format(trade_path), sheet_name=None)
    expenses = df.get('expenses')
    portfolio = df.get('portfolio')
    trades = df.get('trades')
    return expenses, portfolio, trades



if __name__ == '__main__':
    expenses, portfolio, trades = load_port()
    print(expenses)
    print(portfolio)
    print(trades)