# main.py
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from  scripts.telegram_scraper_utility import TelegramScraper
from  dotenv import load_dotenv
import os, sys
# Configuration
load_dotenv('.env')
API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
CHANNELS = ['DoctorsET', 'lobelia4cosmetics', 'yetenaweg', 'EAHCI']
IMAGE_CHANNELS = ['lobelia4cosmetics']

# Create an instance of the TelegramScraper
scraper = TelegramScraper(api_id=API_ID, api_hash=API_HASH)

# Run the scraper
with scraper.client:
    scraper.client.loop.run_until_complete(
        scraper.run(channels=CHANNELS, image_channels=IMAGE_CHANNELS)
    )