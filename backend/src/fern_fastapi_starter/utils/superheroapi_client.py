import requests
from typing import Dict, Union


class SuperHeroAPIClient:
    def __init__(self, access_token: str):
        self.base_url = "https://superheroapi.com/api"
        self.access_token = access_token

    def get_power_stats(self, hero_id: str) -> Union[Dict, None]:
        url = f"{self.base_url}/{self.access_token}/{hero_id}/powerstats"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get power stats for hero with ID {hero_id}. Status code: {response.status_code}")
            return None
