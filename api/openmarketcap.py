import requests
import structlog
import pandas as pd

logger = structlog.get_logger()


def get_data():
    logger.info("Retrieving openmarketcap api data")
    response = requests.get("http://api.openmarketcap.com/api/v1/tokens")
    if response.status_code == 200:
        return response.json()
    else:
        logger.warn("Error retrieving openmarketcap api data")
        return None

def parse_data(openmc_data):
    logger.info("Parsing openmarketcap api data to df")
    openmc_df = pd.DataFrame(openmc_data['data'])

    return openmc_df

if __name__ == '__main__':
    print(get_data())