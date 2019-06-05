import pandas as pd
import os
import sys
import structlog
logger = structlog.get_logger()


def portfolio_loadall():
    """
    Loads data from excel file sheets [expenses, crypto_portfolio, trades]
    :return: dataframe for each excel sheet
    """
    logger.info("Loading portfolio.xlsx file")

    #######COMMENT IN FOR PYINSTALLER LINUX#######
    '''
    basedir = sys.executable
    last_dir = basedir.rfind("/")
    basedir = basedir[:last_dir]
    path = '{}/test_port.xlsx'.format(basedir)
    '''
    #######COMMENT IN FOR PYINSTALLER WINDOWS#######
    '''
    path = os.path.dirname(sys.executable)
    ------
    or
    -----
    basedir = sys.executable
    last_dir = basedir.rfind("\\")
    path = basedir[:last_dir]
    '''
    #######COMMENT OUT FOR PYINSTALLER#######
    path = os.path.dirname(os.path.realpath(__file__))
    ##########################################

    trade_path = '{}/portfolio.xlsx'.format(path)
    try:
        expenses = pd.read_excel(r'{}'.format(trade_path), sheet_name='expenses')
        portfolio_crypto = pd.read_excel(r'{}'.format(trade_path), sheet_name='portfolio')
        trades = pd.read_excel(r'{}'.format(trade_path), sheet_name='trades')
    except:
        logger.warn("Failed loading portfolio.xlsx file")
    '''
    for name, sheet in {"expenses": expenses, "portfolio": portfolio_crypto, "trades": trades}.items():
        if sheet is None:
            logger.warn("Excel Sheet {} not found".format(name))
    '''
    return expenses, portfolio_crypto, trades


if __name__ == '__main__':
    expenses, portfolio_crypto, trades = portfolio_load()
    print("expenses", expenses)
    print("portfolio_crypto", portfolio_crypto)
    print("trades", trades)