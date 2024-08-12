import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://webhook.site/bc34bdc0-7bac-4c1c-a7b8-4dc8f5e7e064"

    def try_get_request(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return True
        else:
            return False
        
    def parse_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            data = response.json()
            if 'message' in data and data['message'] == "uwu":
                return True
            else:
                return False
        elif response.status_code == 404:
            data = response.json()
            if 'message' in data and data['message'] == "owo":
                return True
            else:
                return False
        else:
            return False
