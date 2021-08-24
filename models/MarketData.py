from dotenv import load_dotenv
from helper import RequestHandler


class MarketData(RequestHandler):

    def get_response(self, endpoint):
        load_dotenv()
        endpoint = endpoint
        response = self.get_data(endpoint)
        return response
