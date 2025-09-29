import requests
from bs4 import BeautifulSoup
import re
import os

class LinkedInVideoDownloader:
    def __init__(self, url: str, output_dir: str = "downloads"):
        self.url = url
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def validate_url(self) -> bool:
        """Check if URL looks like a LinkedIn post"""
        return "linkedin.com/posts" in self.url

    def fetch_html(self) -> str:
        """Fetch HTML content from LinkedIn post"""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return response.text

    def extract_video_url(self, html: str) -> str:
        """Extract direct video URL from LinkedIn post HTML"""
        soup = BeautifulSoup(html, "lxml")

        # Look for <video> tag
        video_tag = soup.find("video")
        if video_tag and video_tag.get("src"):
            return video_tag["src"]

        # Fallback: regex for .mp4 links
        match = re.search(r"https://.*\.mp4", html)
        if match:
            return match.group(0)

        raise ValueError("No video found in this LinkedIn post.")

    def download_video(self, video_url: str, filename: str = "linkedin_video.mp4"):
        """Download video in chunks with progress"""
        filepath = os.path.join(self.output_dir, filename)
        response = requests.get(video_url, stream=True)

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        downloaded = 0

        with open(filepath, "wb") as f:
            for data in response.iter_content(block_size):
                f.write(data)
                downloaded += len(data)
                percent = (downloaded / total_size) * 100 if total_size else 0
                print(f"\rDownloading: {percent:.2f}%", end="")

        print(f"\n✅ Download complete! Saved at {filepath}")
        return filepath

    def run(self):
        if not self.validate_url():
            raise ValueError("Invalid LinkedIn post URL")
        html = self.fetch_html()
        video_url = self.extract_video_url(html)
        return self.download_video(video_url)
