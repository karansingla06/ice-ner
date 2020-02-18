from abc import ABCMeta, abstractmethod

class AbstractIceEngine(object):
    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_extension(self):
        pass

class BaseEntityRecognizer(object, metaclass=ABCMeta):
    def __init__(self, serviceid):
        self.serviceid = serviceid
        if(serviceid=='DEFAULT'):
            self.model=self.load()
        else:
            self.model=None

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def predict(self, text, original_text, pos):
        pass

class BaseDefaultEntityRecognizer(BaseEntityRecognizer, metaclass=ABCMeta):
    def __init__(self,serviceid="DEFAULT"):
        super(BaseDefaultEntityRecognizer, self).__init__(serviceid)

class BaseCustomEntityRecognizer(BaseEntityRecognizer, metaclass=ABCMeta):
    def __init__(self, serviceid=None):
        super(BaseCustomEntityRecognizer, self).__init__(serviceid)

    @abstractmethod
    def prepare(self, corpus):
        """

        :param corpus:
        :return:
        """
        pass

    @abstractmethod
    def train(self, corpus):
        """

        :param corpus:
        :return:
        """
        pass

    @abstractmethod
    def save(self):
        """

        :param utterances:
        :return:
        """
        pass





