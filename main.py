from connection import Connection
from Source import Source
from Currency import Currency


with Connection("https://e-kursy-walut.pl/kurs-lisk/") as con:
    source = Source(con.connect, 'lxml')
    currency = Currency(source().body.find('div', class_="left").find("span").text)
    print('Lisk: ', currency.currency)
