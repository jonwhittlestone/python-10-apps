import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, unit, loc')


def print_header():
    print('-------------------------------')
    print('       WEATHER APP             ')
    print('-------------------------------')


def get_post_code_from_user():
    return input('Please enter your post code: ')


def get_html_from_web(post_code):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(post_code)
    response = requests.get(url)

    return response.text


def parse_the_html(html):
    city_css = 'div#location h1'
    weather_condition_css = '#curCond span.wx-value'
    temp_css = '#curTemp .wx-value'
    temp_unit_css = '#curTemp .wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    temp_unit = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    temp_unit = cleanup_text(temp_unit)

    w = WeatherReport(loc=loc, cond=condition, temp=temp, unit=temp_unit)

    return w


def cleanup_text(text: str):
    if not text:
        return text
    return text.strip()


def main():
    print_header()
    post_code = get_post_code_from_user()
    html = get_html_from_web(post_code)
    report = parse_the_html(html)
    print('The weather in {} is {} with a temperature of {} {}' . format(report.loc,report.cond, report.temp, report.unit))


if __name__ == '__main__':
    main()
