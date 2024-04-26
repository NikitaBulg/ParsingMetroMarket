import requests
import fake_headers, fake_useragent

class Browser():
    def __init__(self):
        pass

    @classmethod
    def gethtml(cls, url):
        """Write parsed html"""
        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(str(cls.request(url).text))

    @staticmethod
    def request(url):
        """Making fake information"""
        fake_header = fake_headers.Headers(browser='chrome', os='win', headers=True).generate()
        fake_header['User-Agent'] = fake_useragent.UserAgent()['google chrome']

        """Make main requests"""
        try:
            content = requests.get('{0}'.format(url), headers=fake_header)
            if content.status_code == 200:
                return content
            else:
                return -1
        except requests.exceptions.ConnectionError:
            return -1

if __name__ == '__main__':
    browser = Browser()
    browser.gethtml('https://online.metro-cc.ru/category/bakaleya/konservy/myasnye-konservy')