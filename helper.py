import os
import requests
from dotenv import load_dotenv


class RequestHandler:
    load_dotenv()
    url: str = os.environ.get("BASE_URL")

    def get_data(self, endpoint: str):
        """
        :param endpoint: {str} only append the endpoint to the base url
        :return:
        """
        response = requests.get(self.url + endpoint,
                                headers={
                                    "Authorization": "Bearer "+os.environ.get("TOKEN_KEY")
                                })

        return response.json()
