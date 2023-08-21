import requests

URL = 'https://www.linkedin.com/jobs/search?keywords=Python%20Django%20Developer&location=India&locationId=&geoId' \
      '=102713980&f_TPR=r604800&f_PP=105214831%2C105556991%2C106888327%2C103671728&f_E=1%2C2%2C3&position=1&pageNum=0'


def get_source(url):
    response = requests.get(url=url)
    source = response.text
    return source


if __name__ == '__main__':
    print(get_source(URL))
