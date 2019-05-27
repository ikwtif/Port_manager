import pandas as pd
import os
import sys

def portfolio_load():
    #######COMMENT IN FOR PYINSTALLER#######
    '''
    basedir = sys.executable
    last_dir = basedir.rfind("/")
    basedir = basedir[:last_dir]
    trade_path = '{}/test_port.xlsx'.format(basedir)
    '''
    #######COMMENT OUT FOR PYINSTALLER#######
    path = os.path.dirname(os.path.realpath(__file__))
    print(path)
    trade_path = '{}/portfolio.xlsx'.format(path)
    ##########################################

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