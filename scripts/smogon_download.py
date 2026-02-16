import os
import requests
import re

# The list of URLs you provided
urls = [
    "https://www.smogon.com/forums/attachments/666_1-png.273580/",
    "https://www.smogon.com/forums/attachments/666_2-png.273582/",
    "https://www.smogon.com/forums/attachments/666_3-png.273584/",
    "https://www.smogon.com/forums/attachments/666_4-png.273586/",
    "https://www.smogon.com/forums/attachments/666_5-png.273588/",
    "https://www.smogon.com/forums/attachments/666_6-png.273590/",
    "https://www.smogon.com/forums/attachments/666_7-png.273592/",
    "https://www.smogon.com/forums/attachments/666_8-png.273594/",
    "https://www.smogon.com/forums/attachments/666_9-png.273596/",
    "https://www.smogon.com/forums/attachments/666_10-png.273598/",
    "https://www.smogon.com/forums/attachments/666_11-png.273600/",
    "https://www.smogon.com/forums/attachments/666_12-png.273602/",
    "https://www.smogon.com/forums/attachments/666_13-png.273604/",
    "https://www.smogon.com/forums/attachments/666_14-png.273606/",
    "https://www.smogon.com/forums/attachments/666_15-png.273608/",
    "https://www.smogon.com/forums/attachments/666_16-png.273610/",
    "https://www.smogon.com/forums/attachments/666_17-png.273612/",
    "https://www.smogon.com/forums/attachments/666_18-png.273614/",
    "https://www.smogon.com/forums/attachments/666_19-png.273616/",
    "https://www.smogon.com/forums/attachments/666_20-png.273618/",
    "https://www.smogon.com/forums/attachments/669_1-png.276624/",
    "https://www.smogon.com/forums/attachments/669_2-png.276628/",
    "https://www.smogon.com/forums/attachments/669_3-png.276632/",
    "https://www.smogon.com/forums/attachments/669_4-png.276636/",
    "https://www.smogon.com/forums/attachments/669_5-png.276640/",
    "https://www.smogon.com/forums/attachments/670_1-png.276644/",
    "https://www.smogon.com/forums/attachments/670_2-png.276648/",
    "https://www.smogon.com/forums/attachments/670_3-png.276652/",
    "https://www.smogon.com/forums/attachments/670_4-png.276656/",
    "https://www.smogon.com/forums/attachments/670_5-png.276660/",
    "https://www.smogon.com/forums/attachments/670_6-png.276664/",
    "https://www.smogon.com/forums/attachments/671_1-png.276668/",
    "https://www.smogon.com/forums/attachments/671_2-png.276672/",
    "https://www.smogon.com/forums/attachments/671_3-png.276676/",
    "https://www.smogon.com/forums/attachments/671_4-png.276680/",
    "https://www.smogon.com/forums/attachments/671_5-png.276684/",
    "https://www.smogon.com/forums/attachments/669_1b-png.276625/",
    "https://www.smogon.com/forums/attachments/669_1s-png.276626/",
    "https://www.smogon.com/forums/attachments/669_1sb-png.276627/",
    "https://www.smogon.com/forums/attachments/669_2b-png.276629/",
    "https://www.smogon.com/forums/attachments/669_2s-png.276630/",
    "https://www.smogon.com/forums/attachments/669_2sb-png.276631/",
    "https://www.smogon.com/forums/attachments/669_3b-png.276633/",
    "https://www.smogon.com/forums/attachments/669_3s-png.276634/",
    "https://www.smogon.com/forums/attachments/669_3sb-png.276635/",
    "https://www.smogon.com/forums/attachments/669_4b-png.276637/",
    "https://www.smogon.com/forums/attachments/669_4s-png.276638/",
    "https://www.smogon.com/forums/attachments/669_4sb-png.276639/",
    "https://www.smogon.com/forums/attachments/669_5b-png.276641/",
    "https://www.smogon.com/forums/attachments/669_5s-png.276642/",
    "https://www.smogon.com/forums/attachments/669_5sb-png.276643/",
    "https://www.smogon.com/forums/attachments/670_1b-png.276645/",
    "https://www.smogon.com/forums/attachments/670_1s-png.276646/",
    "https://www.smogon.com/forums/attachments/670_1sb-png.276647/",
    "https://www.smogon.com/forums/attachments/670_2b-png.276649/",
    "https://www.smogon.com/forums/attachments/670_2s-png.276650/",
    "https://www.smogon.com/forums/attachments/670_2sb-png.276651/",
    "https://www.smogon.com/forums/attachments/670_3b-png.276653/",
    "https://www.smogon.com/forums/attachments/670_3s-png.276654/",
    "https://www.smogon.com/forums/attachments/670_3sb-png.276655/",
    "https://www.smogon.com/forums/attachments/670_4b-png.276657/",
    "https://www.smogon.com/forums/attachments/670_4s-png.276658/",
    "https://www.smogon.com/forums/attachments/670_4sb-png.276659/",
    "https://www.smogon.com/forums/attachments/670_5b-png.276661/",
    "https://www.smogon.com/forums/attachments/670_5s-png.276662/",
    "https://www.smogon.com/forums/attachments/670_5sb-png.276663/",
    "https://www.smogon.com/forums/attachments/670_6b-png.276665/",
    "https://www.smogon.com/forums/attachments/670_6s-png.276666/",
    "https://www.smogon.com/forums/attachments/670_6sb-png.276667/",
    "https://www.smogon.com/forums/attachments/671_1b-png.276669/",
    "https://www.smogon.com/forums/attachments/671_1s-png.276670/",
    "https://www.smogon.com/forums/attachments/671_1sb-png.276671/",
    "https://www.smogon.com/forums/attachments/671_2b-png.276673/",
    "https://www.smogon.com/forums/attachments/671_2s-png.276674/",
    "https://www.smogon.com/forums/attachments/671_2sb-png.276675/",
    "https://www.smogon.com/forums/attachments/671_3b-png.276677/",
    "https://www.smogon.com/forums/attachments/671_3s-png.276678/",
    "https://www.smogon.com/forums/attachments/671_3sb-png.276679/",
    "https://www.smogon.com/forums/attachments/671_4b-png.276681/",
    "https://www.smogon.com/forums/attachments/671_4s-png.276682/",
    "https://www.smogon.com/forums/attachments/671_4sb-png.276683/",
    "https://www.smogon.com/forums/attachments/671_5b-png.276685/",
    "https://www.smogon.com/forums/attachments/671_5s-png.276686/",
    "https://www.smogon.com/forums/attachments/671_5sb-png.276687/",
    "https://www.smogon.com/forums/attachments/666_1b-png.274442/",
    "https://www.smogon.com/forums/attachments/666_1s-png.273581/",
    "https://www.smogon.com/forums/attachments/666_1sb-png.274443/",
    "https://www.smogon.com/forums/attachments/666_2b-png.274444/",
    "https://www.smogon.com/forums/attachments/666_2s-png.273583/",
    "https://www.smogon.com/forums/attachments/666_2sb-png.274445/",
    "https://www.smogon.com/forums/attachments/666_3b-png.274446/",
    "https://www.smogon.com/forums/attachments/666_3s-png.273585/",
    "https://www.smogon.com/forums/attachments/666_3sb-png.274447/",
    "https://www.smogon.com/forums/attachments/666_4b-png.274448/",
    "https://www.smogon.com/forums/attachments/666_4s-png.273587/",
    "https://www.smogon.com/forums/attachments/666_4sb-png.274449/",
    "https://www.smogon.com/forums/attachments/666_5b-png.274450/",
    "https://www.smogon.com/forums/attachments/666_5s-png.273589/",
    "https://www.smogon.com/forums/attachments/666_5sb-png.274451/",
    "https://www.smogon.com/forums/attachments/666_6b-png.274452/",
    "https://www.smogon.com/forums/attachments/666_6s-png.273591/",
    "https://www.smogon.com/forums/attachments/666_6sb-png.274453/",
    "https://www.smogon.com/forums/attachments/666_7b-png.274454/",
    "https://www.smogon.com/forums/attachments/666_7s-png.273593/",
    "https://www.smogon.com/forums/attachments/666_7sb-png.274455/",
    "https://www.smogon.com/forums/attachments/666_8b-png.274456/",
    "https://www.smogon.com/forums/attachments/666_8s-png.273595/",
    "https://www.smogon.com/forums/attachments/666_8sb-png.274457/",
    "https://www.smogon.com/forums/attachments/666_9b-png.274458/",
    "https://www.smogon.com/forums/attachments/666_9s-png.273597/",
    "https://www.smogon.com/forums/attachments/666_9sb-png.274459/",
    "https://www.smogon.com/forums/attachments/666_10b-png.274460/",
    "https://www.smogon.com/forums/attachments/666_10s-png.273599/",
    "https://www.smogon.com/forums/attachments/666_10sb-png.274461/",
    "https://www.smogon.com/forums/attachments/666_11b-png.274462/",
    "https://www.smogon.com/forums/attachments/666_11s-png.273601/",
    "https://www.smogon.com/forums/attachments/666_11sb-png.274463/",
    "https://www.smogon.com/forums/attachments/666_12b-png.274464/",
    "https://www.smogon.com/forums/attachments/666_12s-png.273603/",
    "https://www.smogon.com/forums/attachments/666_12sb-png.274465/",
    "https://www.smogon.com/forums/attachments/666_13b-png.274466/",
    "https://www.smogon.com/forums/attachments/666_13s-png.273605/",
    "https://www.smogon.com/forums/attachments/666_13sb-png.274467/",
    "https://www.smogon.com/forums/attachments/666_14b-png.274468/",
    "https://www.smogon.com/forums/attachments/666_14s-png.273607/",
    "https://www.smogon.com/forums/attachments/666_14sb-png.274469/",
    "https://www.smogon.com/forums/attachments/666_15b-png.274470/",
    "https://www.smogon.com/forums/attachments/666_15s-png.273609/",
    "https://www.smogon.com/forums/attachments/666_15sb-png.274471/",
    "https://www.smogon.com/forums/attachments/666_16b-png.274472/",
    "https://www.smogon.com/forums/attachments/666_16s-png.273611/",
    "https://www.smogon.com/forums/attachments/666_16sb-png.274473/",
    "https://www.smogon.com/forums/attachments/666_17b-png.274474/",
    "https://www.smogon.com/forums/attachments/666_17s-png.273613/",
    "https://www.smogon.com/forums/attachments/666_17sb-png.274475/",
    "https://www.smogon.com/forums/attachments/666_18b-png.274476/",
    "https://www.smogon.com/forums/attachments/666_18s-png.273615/",
    "https://www.smogon.com/forums/attachments/666_18sb-png.274477/",
    "https://www.smogon.com/forums/attachments/666_19b-png.274478/",
    "https://www.smogon.com/forums/attachments/666_19s-png.273617/",
    "https://www.smogon.com/forums/attachments/666_19sb-png.274479/",
    "https://www.smogon.com/forums/attachments/666_20b-png.274480/",
    "https://www.smogon.com/forums/attachments/666_20s-png.273619/",
    "https://www.smogon.com/forums/attachments/666_20sb-png.274481/",
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
