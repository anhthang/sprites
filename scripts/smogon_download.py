import os
import requests
import re

# The list of URLs you provided
urls = [
    "https://www.smogon.com/forums/attachments/1017_1-png.732406/",
    "https://www.smogon.com/forums/attachments/1017_1s-png.732407/",
    "https://www.smogon.com/forums/attachments/1017_2-png.732408/",
    "https://www.smogon.com/forums/attachments/1017_2s-png.732409/",
    "https://www.smogon.com/forums/attachments/1017_3-png.732410/",
    "https://www.smogon.com/forums/attachments/1017_3s-png.732411/",
    "https://www.smogon.com/forums/attachments/1017_4-png.732412/",
    "https://www.smogon.com/forums/attachments/1017_4s-png.732413/",
]

# Set a User-Agent to prevent Smogon from blocking the request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.31"
}


def download_sprites():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
        print("📁 Created 'downloads' directory.")

    print(f"🚀 Starting download of {len(urls)} files...")

    for url in urls:
        try:
            # 1. Extract filename from URL
            # Example: 652sb-png.492504/ -> 652sb.png
            match = re.search(r"attachments/([\w-]+)-png\.\d+/?", url)
            if match:
                base_name = match.group(1)
                filename = f"{base_name}.png"
            else:
                # Fallback if regex fails
                filename = url.split("/")[-2].split("-")[0] + ".png"

            save_path = os.path.join("downloads", filename)

            # 2. Download the file
            response = requests.get(url, headers=HEADERS, stream=True)

            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"✅ Downloaded: {filename}")
            else:
                print(f"❌ Failed: {url} (Status: {response.status_code})")

        except Exception as e:
            print(f"⚠️ Error downloading {url}: {e}")

    print("\n" + "=" * 30)
    print("Download process finished.")
    print(f"Files are located in: {os.path.abspath('downloads')}")
    print("=" * 30)


if __name__ == "__main__":
    download_sprites()
