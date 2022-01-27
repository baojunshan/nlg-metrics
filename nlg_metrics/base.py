from abc import abstractmethod, ABCMeta


class IMetrics(metaclass=ABCMeta):

    @property
    def name(self):
        pass

    @abstractmethod
    def calc(self, **kwargs):
        pass



