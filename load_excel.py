import pandas as pd
import os


def portfolio_load():
    path = os.path.dirname(os.path.realpath(__file__))
    trade_path = '{}/test_port.xlsx'.format(path)
    df = pd.read_excel(r'{}'.format(trade_path), sheet_name=None)
    expenses = df.get('expenses')
    portfolio = df.get('portfolio')
    portfolio = portfolio.set_index('storage')
    portfolio.loc['total'] = portfolio.sum()

    trades = df.get('trades')
    return expenses, portfolio, trades


if __name__ == '__main__':
    expenses, portfolio, trades = portfolio_load()
    print(expenses)
    print(portfolio)
    print(trades)