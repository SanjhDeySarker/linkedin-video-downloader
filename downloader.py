import yt_dlp
import os
import time


class LinkedInVideoDownloader:
    def __init__(self, url: str, output_dir: str = "downloads"):
        """
        Initialize the LinkedIn Video Downloader.

        Args:
            url (str): LinkedIn post URL containing the video.
            output_dir (str): Directory to save downloaded videos.
        """
        self.url = url
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def validate_url(self) -> bool:
        """Check if the given URL is a LinkedIn link."""
        return "linkedin.com" in self.url

    def download_video(self) -> str:
        """
        Download LinkedIn video using yt-dlp.

        Returns:
            str: Path to the downloaded video file.
        """
        if not self.validate_url():
            raise ValueError("❌ Invalid LinkedIn URL provided")

        # Generate unique filename using timestamp
        timestamp = int(time.time())
        outtmpl = os.path.join(self.output_dir, f"linkedin_{timestamp}.%(ext)s")

        ydl_opts = {
            "outtmpl": outtmpl,            # output template
            "quiet": False,                # show progress
            "noplaylist": True,            # avoid playlists
            "format": "bestvideo+bestaudio/best",  # highest quality
            "merge_output_format": "mp4"   # merge audio+video into mp4
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
        except Exception as e:
            raise RuntimeError(f"❌ Failed to download video: {e}")

        print(f"✅ Download complete! File saved in: {self.output_dir}")
        return self.output_dir
