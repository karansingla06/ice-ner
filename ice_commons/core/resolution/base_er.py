from abc import abstractmethod


class BaseResolutionNER(object):

    @abstractmethod
    def resolve(self, text):
        pass

