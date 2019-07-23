import requests


def get_data():
    response = requests.get('http://httpbin.org/get')
    return response.status_code


if __name__ == '__main__':
    get_data()
