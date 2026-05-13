"""
Kalodata API client for n8n Code nodes.
"""

from typing import List, Dict, Optional
import requests


class KalodataClient:
    BASE_URL = "https://api.kalodata.com"

    def __init__(self, api_key: str):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def list_trending_products(self, country: str = "US", limit: int = 50) -> List[Dict]:
        """Fetch trending TikTok Shop products. [Not shown]"""
        pass

    def get_competitor_videos(self, product_id: str) -> List[Dict]:
        """Top performing videos for a product. [Not shown]"""
        pass
