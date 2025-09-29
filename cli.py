from downloader import LinkedInVideoDownloader

def main():
    url = input("🔗 Enter LinkedIn post URL: ").strip()
    try:
        downloader = LinkedInVideoDownloader(url)
        downloader.download_video()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
