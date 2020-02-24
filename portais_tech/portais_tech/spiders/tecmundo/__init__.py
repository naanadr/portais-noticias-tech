from datetime import datetime


def get_datetime(response):
    date = response.xpath('//time/@datetime').get()
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

    return date
