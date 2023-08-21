import requests
import selectorlib
from send_gmail import send


URL = 'https://www.linkedin.com/jobs/search?keywords=Python%20Django%20Developer&location=India&locationId=&geoId' \
      '=102713980&f_TPR=r604800&f_PP=105214831%2C105556991%2C106888327%2C103671728&f_E=1%2C2%2C3&position=1&pageNum=0'


def get_source(url):
    response = requests.get(url=url)
    page_source = response.text
    return page_source


def extract_data(page_source):
    extractor = selectorlib.Extractor.from_yaml_file('jobs.yaml')
    job_data = extractor.extract(page_source)
    return job_data


def send_data():
    email_content = "Subject: Today's Latest Job posting on Linkedin\n"
    if data['job_title'] and data['location'] and data['posted'] and data['link'] is not None:
        email_content = email_content + data['job_title'] + '\n' + \
                        'Location: ' + data['location'] + '\n' + \
                        'Posted: ' + data['posted'] + '\n' + \
                        'Link: '+data['link'] + 2 * '\n'
        send(email_content)
        print('Mail sent successfully..')
    else:
        print('Mail not sent as no data was found')


if __name__ == '__main__':
    source = get_source(URL)
    data = extract_data(source)
    send_data()

