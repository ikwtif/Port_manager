from load_excel import portfolio_loadall
from api import openmarketcap, exchangerates
import pandas as pd
import numpy as np
import structlog
from conf import Configuration



logger = structlog.get_logger()

'''
def portfolio_crypto_generaldata(portfolio):
    openmc_data = openmarketcap.get_data()
    openmc_df = pd.DataFrame(openmc_data['data'])
    columns = ['rank', 'symbol', 'price_change', 'volume_usd', 'market_cap']
    portfolio_data = pd.DataFrame(columns=columns)

    for token in list(portfolio):
        ls = openmc_df.loc[openmc_df['symbol'] == token.upper()]
        for data in list(portfolio_data):
            portfolio_data.loc[:, token] = ls[data]
    print(portfolio_data)
'''

def portfolio_crypto_format(portfolio_crypto):
    logger.info("formatting crypto_portfolio")

    portfolio_crypto = portfolio_crypto.set_index('token')
    portfolio_crypto = portfolio_crypto.T
    portfolio_crypto.index.name = 'storage'
    portfolio_crypto.loc['total'] = portfolio_crypto.sum()

    return portfolio_crypto


def portfolio_crypto_fiat(portfolio):
    conf = Configuration()
    currency = conf.settings_main['currency']
    rates = exchangerates.get_data()
    try:
        exchange_rate = rates['rates'][currency]
    except:
        key_list = ['USD']
        for key in rates['rates'].keys():
            key_list.append(key)
        logger.warn('{} not found in exchangerates, possible symbols are: {}'.format(currency, key_list))
        raise

    logger.info("Calculating crypto portfolio value in {}".format(currency))

    openmc_data = openmarketcap.get_data()
    openmc_df = openmarketcap.parse_data(openmc_data)
    portfolio_fiat = portfolio_crypto_format(portfolio)
    print(list(portfolio_fiat))
    portfolio_fiat = portfolio_fiat.copy()
    for token in list(portfolio_fiat):
        ls = openmc_df.loc[openmc_df['symbol'] == token.upper()]
        if ls.empty:
            logger.warn("{} not found in openmarketcap api data".format(token.upper()))
        usd_price = float(ls.iloc[0]['price_usd'])
        token_rank = float(ls.iloc[0]['rank'])
        price_change = ls.iloc[0]['price_change']
        token_volume = float(ls.iloc[0]['volume_usd'])
        portfolio_fiat.loc[:, token] *= usd_price * exchange_rate
        #portfolio_fiat.loc[:, token] *= usd_price * exchange_rate
        #portfolio_fiat.loc[:, token] *= usd_price * exchange_rate
        #portfolio_fiat.loc[:, token] *= usd_price * exchange_rate
    portfolio_fiat = portfolio_fiat.round(2)

    return portfolio_fiat, currency


if __name__ == '__main__':
    expenses, portfolio, trades = portfolio_loadall()
    portfolio_fiat, currency = portfolio_crypto_fiat(portfolio)
    #portfolio_datas(portfolio)


