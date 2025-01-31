# telegram_scraper.py
import os
import json
from telethon import TelegramClient

# Import the Logger class
import sys
import os

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .logger_utils import Logger  # Assuming logger.py is in the parent directory

class TelegramScraper:
    def __init__(self, api_id, api_hash, session_name='session_name'):
        """
        Initialize the TelegramScraper with API credentials and session name.
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_name = session_name
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)
        self.logger = Logger(name="TelegramScraper").get_logger()  # Initialize the custom logger

    async def scrape_channel(self, channel_username, output_dir='scraped_data', limit=100):
        """
        Scrape text messages from a Telegram channel and save them to a JSON file.
        """
        try:
            self.logger.info(f"Scraping channel: {channel_username}")
            channel = await self.client.get_entity(channel_username)
            messages = await self.client.get_messages(channel, limit=limit)
            data = [{'id': msg.id, 'text': msg.text} for msg in messages]

            # Ensure output directory exists
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Save messages to a JSON file
            output_file = os.path.join(output_dir, f'{channel_username}.json')
            with open(output_file, 'w') as f:
                json.dump(data, f)
            self.logger.info(f"Saved {len(data)} messages from {channel_username} to {output_file}")
        except Exception as e:
            self.logger.error(f"Error scraping {channel_username}: {e}")

    async def scrape_images(self, channel_username, save_dir='scraped_images', limit=200):
        """
        Scrape images from a Telegram channel and save them to a directory.
        """
        try:
            self.logger.info(f"Scraping images from: {channel_username}")
            channel = await self.client.get_entity(channel_username)
            messages = await self.client.get_messages(channel, limit=limit)

            # Ensure save directory exists
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Download images
            for i, message in enumerate(messages):
                if message.photo:
                    await message.download_media(file=os.path.join(save_dir, f'image_{i}.jpg'))
            self.logger.info(f"Saved images from {channel_username} to {save_dir}")
        except Exception as e:
            self.logger.error(f"Error scraping images from {channel_username}: {e}")

    async def run(self, channels, image_channels, output_dir='scraped_data', image_dir='scraped_images'):
        """
        Run the scraper for the specified channels and image channels.
        """
        await self.client.start()
        for channel in channels:
            await self.scrape_channel(channel, output_dir)
        for channel in image_channels:
            await self.scrape_images(channel, image_dir)