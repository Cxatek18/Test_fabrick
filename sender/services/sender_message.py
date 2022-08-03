import requests


class SenderMessage():
    API_URL = 'https://probe.fbrq.cloud/v1/send/'

    def __init__(self, jwt: str) -> None:
        self.headers = {'Authorization': F'Bearer {jwt}'}

    def send(self, user_id, user_phone, text):
        response = requests.post(
            f"{self.API_URL}{user_id}",
            {
                'phone': user_phone,
                'text': text
            },
            headers=self.headers
        )
