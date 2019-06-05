from load_excel import portfolio_loadall
from api import openmarketcap, exchangerates
import structlog
from conf import Configuration
import pandas as pd
import datetime

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
    """
    Formats Dataframe, setting Token column as index and adding Total column
    :param portfolio_crypto: Dataframe with crypto portfolio
    :return: Dataframe
    """
    logger.info("formatting crypto_portfolio")
    portfolio_crypto = portfolio_crypto.set_index('token')
    portfolio_crypto['total'] = portfolio_crypto.sum(axis=1)
    portfolio_crypto = portfolio_crypto.rename_axis('storage', axis=1)

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

    openmarketcap_data = openmarketcap.get_data()
    openmc_df = openmarketcap.parse_data(openmarketcap_data)

    portfolio_fiat = portfolio_crypto_format(portfolio)
    portfolio_fiat = portfolio_fiat.copy()

    for token in list(portfolio_fiat.index.values):
        ls = openmc_df.loc[openmc_df['symbol'] == token.upper()]
        if ls.empty:
            logger.warn("{} not found in openmarketcap api data".format(token.upper()))
        usd_price = float(ls.iloc[0]['price_usd'])
        portfolio_fiat.loc[token, :] *= usd_price * exchange_rate

    portfolio_fiat = portfolio_fiat.round(2)

    return portfolio_fiat, currency


def expenses_format(expenses):
    print(expenses)
    now = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    print('now', now)
    print(type(now))
    
    expenses = expenses.fillna(0)
    print(expenses['Start'][0])
    print(type(expenses['Start'][0].to_pydatetime()))
    print(expenses['End'][0] - expenses['Start'][0])
    #print(datetime.timedelta(expenses['Start'][0].to_pydatetime()-now))
    #expenses['Start'] = pd.to_datetime(expenses['Start'].dt.strftime['%d-%m-%Y'])
    #print(expenses)

    #expenses['Start'] = expenses['Start'].map(lambda x: x.strtime('%d/%m/%Y') if x == str() else '')


if __name__ == '__main__':
    expenses, portfolio, trades = portfolio_loadall()
    #portfolio_crypto_format(portfolio)
    #portfolio_fiat, currency = portfolio_crypto_fiat(portfolio)
    #portfolio_datas(portfolio)
    expenses_formatted = expenses_format(expenses)

