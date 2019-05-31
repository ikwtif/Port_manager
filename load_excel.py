import pandas as pd
import os
import sys
import structlog
logger = structlog.get_logger()


def portfolio_loadall():
    logger.info("Loading portfolio xlsx file")

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
    try:
        df = pd.read_excel(r'{}'.format(trade_path), sheet_name=None)
    except:
        logger.warn("Failed loading portfolio.xlsx file")

    expenses = df.get('expenses')
    portfolio_crypto = df.get('portfolio')
    trades = df.get('trades')

    for name, sheet in {"expenses": expenses, "portfolio": portfolio_crypto, "trades": trades}.items():
        if sheet is None:
            logger.warn("Excel Sheet {} not found".format(name))



    return expenses, portfolio_crypto, trades


if __name__ == '__main__':
    expenses, portfolio_crypto, trades = portfolio_load()
    print("expenses", expenses)
    print("portfolio_crypto", portfolio_crypto)
    print("trades", trades)