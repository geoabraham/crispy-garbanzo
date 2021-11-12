from abc import abstractmethod, ABC


class PaymentService(ABC):

    @abstractmethod
    def fetch_payment_from_api(self):
        pass

    @abstractmethod
    def parse_http_event(self):
        pass


class PaymentServiceImpl(PaymentService):

    def fetch_payment_from_api(self):
        # Implemented logic
        ...

    def parse_http_event(self):
        """This impl does not need this... :'("""
        raise NotImplementedError()
