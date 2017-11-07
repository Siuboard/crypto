from SourceClass import Source as Src
from bs4 import BeautifulSoup

class Source(Src):

    """
    gets connected_url, and source_format('lxml', 'html' ...)
    """

    
    def __init__(self, opened_connection, source_format):
        self.source_format = source_format
        self.opened_connection = opened_connection

    def get_source(self):
        return self.opened_connection.read()

    def parse_source(self):
        return BeautifulSoup(self.get_source(), self.source_format)

    def __call__(self):
        return self.parse_source()

    
