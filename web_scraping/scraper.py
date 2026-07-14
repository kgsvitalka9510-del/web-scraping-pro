"""Core scraper."""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

class Scraper:
    def __init__(self, use_proxies: bool = False, delay: float = 1.0):
        self.use_proxies = use_proxies
        self.delay = delay
        self.session = requests.Session()
    
    def scrape(self, url: str, selectors: Dict[str, str] = None) -> Dict[str, Any]:
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        if selectors:
            return {k: soup.select_one(v).text for k, v in selectors.items() if soup.select_one(v)}
        
        return {"title": soup.title.string if soup.title else None, "status": response.status_code}
