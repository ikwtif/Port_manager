import requests


def get_data():
    response = requests.get("http://api.openmarketcap.com/api/v1/tokens")
    if response.status_code == 200:
        return response.json()
    else:
        return None



if __name__ == '__main__':
    print(get_data())