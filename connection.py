from urllib.request import urlopen, Request

class Connection:
    """connection class TODO"""
    def __init__(self, url):
        self.url = url
        self.connection = None

    @property
    def connect(self):
        if self.connection:
            return self.connection
        else:
            self.connect = self.url

    @connect.setter
    def connect(self, url):
        try:
            self.connection = urlopen(Request(url, headers={'User-Agent':'Mozilla/5.0'}))
        except:
            self.connection.close()
            print('erro')

            
    def __enter__(self):
        self.connect
        return self

    def __exit__(self, e_type, e_value, e_tb):
        self.connection.close()

if __name__ == '__main__':
    with Connection("https://e-kursy-walut.pl/kurs-lisk/") as c:
        print(c.__doc__)
        print(c.url)
        print(c.connect)
