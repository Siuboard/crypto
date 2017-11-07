from abc import ABCMeta, abstractmethod

class Source(metaclass = ABCMeta):

    """
    TODO
    functions:
    connection(self, url)
    get_source(self)
    pretty_source(self, source, source_format)
    """


    def connect(self, url):
        """get access to given url"""
        pass

    @abstractmethod
    def get_source(self):
        """reads source of given url"""
        pass

    @abstractmethod
    def parse_source(self, source, source_format):
        """makes source more useful, and readable"""
        pass
