import requests


def get_data():
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return None



if __name__ == '__main__':
    print(get_data())