from load_excel import portfolio_load
from api import openmarketcap, exchangerates
import pandas as pd
import numpy as np


currency = 'EUR'
rates = exchangerates.get_data()
exchange_rate = rates['rates'][currency]



def calc_portfolio_fiat(portfolio):
    openmc_data = openmarketcap.get_data()
    openmc_df = pd.DataFrame(openmc_data['data'])
    portfolio_fiat = portfolio.copy()
    for token in list(portfolio):
        ls = openmc_df.loc[openmc_df['symbol'] == token.upper()]
        usd_price = float(ls.iloc[0]['price_usd'])
        portfolio_fiat.loc[:, token] *= usd_price * exchange_rate
    portfolio_fiat = portfolio_fiat.round(2)

    return portfolio_fiat, currency


if __name__ == '__main__':
    expenses, portfolio, trades = portfolio_load()
    portfolio_fiat, currency = calc_portfolio_fiat(portfolio)


