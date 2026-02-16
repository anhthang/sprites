import os
import requests
import re

# The list of URLs you provided
urls = [
    "https://www.smogon.com/forums/attachments/025_7-png.272407/",
    "https://www.smogon.com/forums/attachments/025_7b-png.272408/",
    "https://www.smogon.com/forums/attachments/025_7s-png.272409/",
    "https://www.smogon.com/forums/attachments/025_7sb-png.272410/",
    "https://www.smogon.com/forums/attachments/025_8-png.272411/",
    "https://www.smogon.com/forums/attachments/025_8b-png.272412/",
    "https://www.smogon.com/forums/attachments/025_8s-png.272413/",
    "https://www.smogon.com/forums/attachments/025_8sb-png.272414/",
    "https://www.smogon.com/forums/attachments/025_9-png.272415/",
    "https://www.smogon.com/forums/attachments/025_9b-png.272416/",
    "https://www.smogon.com/forums/attachments/025_9s-png.272417/",
    "https://www.smogon.com/forums/attachments/025_9sb-png.272418/",
    "https://www.smogon.com/forums/attachments/025_10-png.272419/",
    "https://www.smogon.com/forums/attachments/025_10b-png.272420/",
    "https://www.smogon.com/forums/attachments/025_10s-png.272421/",
    "https://www.smogon.com/forums/attachments/025_10sb-png.272422/",
    "https://www.smogon.com/forums/attachments/025_11-png.272423/",
    "https://www.smogon.com/forums/attachments/025_11b-png.272424/",
    "https://www.smogon.com/forums/attachments/025_11s-png.272425/",
    "https://www.smogon.com/forums/attachments/025_11sb-png.272426/",
    "https://www.smogon.com/forums/attachments/025_12-png.272427/",
    "https://www.smogon.com/forums/attachments/025_12b-png.272428/",
    "https://www.smogon.com/forums/attachments/025_12s-png.272429/",
    "https://www.smogon.com/forums/attachments/025_12sb-png.272430/",
    "https://www.smogon.com/forums/attachments/025_13-png.272431/",
    "https://www.smogon.com/forums/attachments/025_13b-png.272432/",
    "https://www.smogon.com/forums/attachments/025_13s-png.272433/",
    "https://www.smogon.com/forums/attachments/025_13sb-png.272434/",
    "https://www.smogon.com/forums/attachments/025_15-png.266706/",
    "https://www.smogon.com/forums/attachments/025_15b-png.266707/",
    "https://www.smogon.com/forums/attachments/025_15s-png.266708/",
    "https://www.smogon.com/forums/attachments/025_15sb-png.266709/",
    "https://www.smogon.com/forums/attachments/025_1-png.273720/",
    "https://www.smogon.com/forums/attachments/025_1b-png.273721/",
    "https://www.smogon.com/forums/attachments/025_1s-png.273722/",
    "https://www.smogon.com/forums/attachments/025_1sb-png.273723/",
    "https://www.smogon.com/forums/attachments/025_2-png.273724/",
    "https://www.smogon.com/forums/attachments/025_2b-png.273725/",
    "https://www.smogon.com/forums/attachments/025_2s-png.273726/",
    "https://www.smogon.com/forums/attachments/025_2sb-png.273727/",
    "https://www.smogon.com/forums/attachments/025_3-png.273728/",
    "https://www.smogon.com/forums/attachments/025_3b-png.273729/",
    "https://www.smogon.com/forums/attachments/025_3s-png.273730/",
    "https://www.smogon.com/forums/attachments/025_3sb-png.273731/",
    "https://www.smogon.com/forums/attachments/025_4-png.273732/",
    "https://www.smogon.com/forums/attachments/025_4b-png.273733/",
    "https://www.smogon.com/forums/attachments/025_4s-png.273734/",
    "https://www.smogon.com/forums/attachments/025_4sb-png.273735/",
    "https://www.smogon.com/forums/attachments/025_5-png.273736/",
    "https://www.smogon.com/forums/attachments/025_5b-png.273737/",
    "https://www.smogon.com/forums/attachments/025_5s-png.273738/",
    "https://www.smogon.com/forums/attachments/025_5sb-png.273739/",
    "https://www.smogon.com/forums/attachments/025_6-png.273740/",
    "https://www.smogon.com/forums/attachments/025_6b-png.273741/",
    "https://www.smogon.com/forums/attachments/025_6s-png.273742/",
    "https://www.smogon.com/forums/attachments/025_6sb-png.273743/",
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
