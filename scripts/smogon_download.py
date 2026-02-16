import os
import requests
import re

# The list of URLs you provided
urls = [
    "https://www.smogon.com/forums/attachments/773_1-png.125062/",
    "https://www.smogon.com/forums/attachments/773_1b-png.170270/",
    "https://www.smogon.com/forums/attachments/773_1s-png.170238/",
    "https://www.smogon.com/forums/attachments/773_1sb-png.170294/",
    "https://www.smogon.com/forums/attachments/773_15-png.125076/",
    "https://www.smogon.com/forums/attachments/773_15b-png.170284/",
    "https://www.smogon.com/forums/attachments/773_15s-png.170252/",
    "https://www.smogon.com/forums/attachments/773_15sb-png.170308/",
    "https://www.smogon.com/forums/attachments/773_5-png.125066/",
    "https://www.smogon.com/forums/attachments/773_5b-png.170274/",
    "https://www.smogon.com/forums/attachments/773_5s-png.170242/",
    "https://www.smogon.com/forums/attachments/773_5sb-png.170298/",
    "https://www.smogon.com/forums/attachments/773_7-png.125068/",
    "https://www.smogon.com/forums/attachments/773_7b-png.170276/",
    "https://www.smogon.com/forums/attachments/773_7s-png.170244/",
    "https://www.smogon.com/forums/attachments/773_7sb-png.170300/",
    "https://www.smogon.com/forums/attachments/773_11-png.125072/",
    "https://www.smogon.com/forums/attachments/773_11b-png.170280/",
    "https://www.smogon.com/forums/attachments/773_11s-png.170248/",
    "https://www.smogon.com/forums/attachments/773_11sb-png.170304/",
    "https://www.smogon.com/forums/attachments/773_10-png.125071/",
    "https://www.smogon.com/forums/attachments/773_10b-png.170279/",
    "https://www.smogon.com/forums/attachments/773_10s-png.170247/",
    "https://www.smogon.com/forums/attachments/773_10sb-png.170303/",
    "https://www.smogon.com/forums/attachments/773_6-png.125067/",
    "https://www.smogon.com/forums/attachments/773_6b-png.170275/",
    "https://www.smogon.com/forums/attachments/773_6s-png.170243/",
    "https://www.smogon.com/forums/attachments/773_6sb-png.170299/",
    "https://www.smogon.com/forums/attachments/773_13-png.125074/",
    "https://www.smogon.com/forums/attachments/773_13b-png.170282/",
    "https://www.smogon.com/forums/attachments/773_13s-png.170250/",
    "https://www.smogon.com/forums/attachments/773_13sb-png.170306/",
    "https://www.smogon.com/forums/attachments/773_14-png.125075/",
    "https://www.smogon.com/forums/attachments/773_14b-png.170283/",
    "https://www.smogon.com/forums/attachments/773_14s-png.170251/",
    "https://www.smogon.com/forums/attachments/773_14sb-png.170307/",
    "https://www.smogon.com/forums/attachments/773_3-png.125064/",
    "https://www.smogon.com/forums/attachments/773_3b-png.170272/",
    "https://www.smogon.com/forums/attachments/773_3s-png.170240/",
    "https://www.smogon.com/forums/attachments/773_3sb-png.170296/",
    "https://www.smogon.com/forums/attachments/773_4-png.125065/",
    "https://www.smogon.com/forums/attachments/773_4b-png.170273/",
    "https://www.smogon.com/forums/attachments/773_4s-png.170241/",
    "https://www.smogon.com/forums/attachments/773_4sb-png.170920/",
    "https://www.smogon.com/forums/attachments/773_2-png.125063/",
    "https://www.smogon.com/forums/attachments/773_2b-png.170271/",
    "https://www.smogon.com/forums/attachments/773_2s-png.170239/",
    "https://www.smogon.com/forums/attachments/773_2sb-png.170295/",
    "https://www.smogon.com/forums/attachments/773_8-png.125069/",
    "https://www.smogon.com/forums/attachments/773_8b-png.170277/",
    "https://www.smogon.com/forums/attachments/773_8s-png.170245/",
    "https://www.smogon.com/forums/attachments/773_8sb-png.170301/",
    "https://www.smogon.com/forums/attachments/773_9-png.125070/",
    "https://www.smogon.com/forums/attachments/773_9b-png.170278/",
    "https://www.smogon.com/forums/attachments/773_9s-png.170246/",
    "https://www.smogon.com/forums/attachments/773_9sb-png.170302/",
    "https://www.smogon.com/forums/attachments/773_16-png.125077/",
    "https://www.smogon.com/forums/attachments/773_16b-png.170285/",
    "https://www.smogon.com/forums/attachments/773_16s-png.170253/",
    "https://www.smogon.com/forums/attachments/773_16sb-png.170309/",
    "https://www.smogon.com/forums/attachments/773_17-png.125078/",
    "https://www.smogon.com/forums/attachments/773_17b-png.170286/",
    "https://www.smogon.com/forums/attachments/773_17s-png.170254/",
    "https://www.smogon.com/forums/attachments/773_17sb-png.170310/",
    "https://www.smogon.com/forums/attachments/773_12-png.125073/",
    "https://www.smogon.com/forums/attachments/773_12b-png.170281/",
    "https://www.smogon.com/forums/attachments/773_12s-png.170249/",
    "https://www.smogon.com/forums/attachments/773_12sb-png.170305/",
    "https://www.smogon.com/forums/attachments/773_18-png.125079/",
    "https://www.smogon.com/forums/attachments/773_18b-png.170287/",
    "https://www.smogon.com/forums/attachments/773_18s-png.170255/",
    "https://www.smogon.com/forums/attachments/773_18sb-png.170311/",
    "https://www.smogon.com/forums/attachments/774_1-png.102500/",
    "https://www.smogon.com/forums/attachments/774_1-png.114025/",
    "https://www.smogon.com/forums/attachments/774_1s-png.272348/",
    "https://www.smogon.com/forums/attachments/774_1sb-png.272349/",
    "https://www.smogon.com/forums/attachments/774_2-png.114219/",
    "https://www.smogon.com/forums/attachments/774_2b-png.115297/",
    "https://www.smogon.com/forums/attachments/774_2s-png.272350/",
    "https://www.smogon.com/forums/attachments/774_2sb-png.272351/",
    "https://www.smogon.com/forums/attachments/774_3-png.114220/",
    "https://www.smogon.com/forums/attachments/774_3b-png.115298/",
    "https://www.smogon.com/forums/attachments/774_3s-png.272352/",
    "https://www.smogon.com/forums/attachments/774_3sb-png.272353/",
    "https://www.smogon.com/forums/attachments/774_4-png.114221/",
    "https://www.smogon.com/forums/attachments/774_4b-png.115299/",
    "https://www.smogon.com/forums/attachments/774_4s-png.272354/",
    "https://www.smogon.com/forums/attachments/774_4sb-png.272355/",
    "https://www.smogon.com/forums/attachments/774_5-png.114222/",
    "https://www.smogon.com/forums/attachments/774_5b-png.115300/",
    "https://www.smogon.com/forums/attachments/774_5s-png.272356/",
    "https://www.smogon.com/forums/attachments/774_5sb-png.272357/",
    "https://www.smogon.com/forums/attachments/774_2-png.102501/",
    "https://www.smogon.com/forums/attachments/774_2-png.114026/",
    "https://www.smogon.com/forums/attachments/774_6s-png.272358/",
    "https://www.smogon.com/forums/attachments/774_6sb-png.272359/",
    "https://www.smogon.com/forums/attachments/774_7-png.114223/",
    "https://www.smogon.com/forums/attachments/774_7b-png.115301/",
    "https://www.smogon.com/forums/attachments/774_7s-png.272360/",
    "https://www.smogon.com/forums/attachments/774_7sb-png.272361/",
    "https://www.smogon.com/forums/attachments/774_8-png.114224/",
    "https://www.smogon.com/forums/attachments/774_8b-png.115302/",
    "https://www.smogon.com/forums/attachments/774_8s-png.272362/",
    "https://www.smogon.com/forums/attachments/774_8sb-png.272363/",
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
