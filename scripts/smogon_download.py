import os
import requests
import re

# The list of URLs you provided
urls = [
    "https://www.smogon.com/forums/attachments/650sb-png.290755/",
    "https://www.smogon.com/forums/attachments/651sb-png.275699/",
    "https://www.smogon.com/forums/attachments/652sb-png.492504/",
    "https://www.smogon.com/forums/attachments/653sb-png.273563/",
    "https://www.smogon.com/forums/attachments/654sb-png.492505/",
    "https://www.smogon.com/forums/attachments/655sb-png.492507/",
    "https://www.smogon.com/forums/attachments/656sb-png.273569/",
    "https://www.smogon.com/forums/attachments/657sb-png.653030/",
    "https://www.smogon.com/forums/attachments/658sb-png.273573/",
    "https://www.smogon.com/forums/attachments/659sb-png.276618/",
    "https://www.smogon.com/forums/attachments/660sb-png.653032/",
    "https://www.smogon.com/forums/attachments/661sb-png.653034/",
    "https://www.smogon.com/forums/attachments/662sb-png.653036/",
    "https://www.smogon.com/forums/attachments/663sb-png.273577/",
    "https://www.smogon.com/forums/attachments/664sb-png.653038/",
    "https://www.smogon.com/forums/attachments/665sb-png.290759/",
    "https://www.smogon.com/forums/attachments/666_1sb-png.274443/",
    "https://www.smogon.com/forums/attachments/666_2sb-png.274445/",
    "https://www.smogon.com/forums/attachments/666_3sb-png.274447/",
    "https://www.smogon.com/forums/attachments/666_4sb-png.274449/",
    "https://www.smogon.com/forums/attachments/666_5sb-png.274451/",
    "https://www.smogon.com/forums/attachments/666_6sb-png.274453/",
    "https://www.smogon.com/forums/attachments/666_7sb-png.274455/",
    "https://www.smogon.com/forums/attachments/666_8sb-png.274457/",
    "https://www.smogon.com/forums/attachments/666_9sb-png.274459/",
    "https://www.smogon.com/forums/attachments/666_10sb-png.274461/",
    "https://www.smogon.com/forums/attachments/666_11sb-png.274463/",
    "https://www.smogon.com/forums/attachments/666_12sb-png.274465/",
    "https://www.smogon.com/forums/attachments/666_13sb-png.274467/",
    "https://www.smogon.com/forums/attachments/666_14sb-png.274469/",
    "https://www.smogon.com/forums/attachments/666_15sb-png.274471/",
    "https://www.smogon.com/forums/attachments/666_16sb-png.274473/",
    "https://www.smogon.com/forums/attachments/666_17sb-png.274475/",
    "https://www.smogon.com/forums/attachments/666_18sb-png.274477/",
    "https://www.smogon.com/forums/attachments/666_19sb-png.274479/",
    "https://www.smogon.com/forums/attachments/666_20sb-png.274481/",
    "https://www.smogon.com/forums/attachments/667sb-png.276623/",
    "https://www.smogon.com/forums/attachments/668msb-png.653044/",
    "https://www.smogon.com/forums/attachments/668fsb-png.653042/",
    "https://www.smogon.com/forums/attachments/669_1sb-png.276627/",
    "https://www.smogon.com/forums/attachments/669_2sb-png.276631/",
    "https://www.smogon.com/forums/attachments/669_3sb-png.276635/",
    "https://www.smogon.com/forums/attachments/669_4sb-png.276639/",
    "https://www.smogon.com/forums/attachments/669_5sb-png.276643/",
    "https://www.smogon.com/forums/attachments/670_1sb-png.276647/",
    "https://www.smogon.com/forums/attachments/670_2sb-png.276651/",
    "https://www.smogon.com/forums/attachments/670_3sb-png.276655/",
    "https://www.smogon.com/forums/attachments/670_4sb-png.276659/",
    "https://www.smogon.com/forums/attachments/670_5sb-png.276663/",
    "https://www.smogon.com/forums/attachments/670_6sb-png.276667/",
    "https://www.smogon.com/forums/attachments/671_1sb-png.276671/",
    "https://www.smogon.com/forums/attachments/671_2sb-png.276675/",
    "https://www.smogon.com/forums/attachments/671_3sb-png.276679/",
    "https://www.smogon.com/forums/attachments/671_4sb-png.276683/",
    "https://www.smogon.com/forums/attachments/671_5sb-png.276687/",
    "https://www.smogon.com/forums/attachments/672sb-png.276691/",
    "https://www.smogon.com/forums/attachments/673sb-png.492509/",
    "https://www.smogon.com/forums/attachments/674sb-png.273640/",
    "https://www.smogon.com/forums/attachments/675sb-png.492510/",
    "https://www.smogon.com/forums/attachments/676_1sb-png.282242/",
    "https://www.smogon.com/forums/attachments/677sb-png.273646/",
    "https://www.smogon.com/forums/attachments/678msb-png.282248/",
    "https://www.smogon.com/forums/attachments/678fsb-png.282245/",
    "https://www.smogon.com/forums/attachments/679_2sb-png.492512/",
    "https://www.smogon.com/forums/attachments/679_1sb-png.492511/",
    "https://www.smogon.com/forums/attachments/680_2sb-png.653048/",
    "https://www.smogon.com/forums/attachments/680_1sb-png.653046/",
    "https://www.smogon.com/forums/attachments/682sb-png.273654/",
    "https://www.smogon.com/forums/attachments/683sb-png.290761/",
    "https://www.smogon.com/forums/attachments/684sb-png.273658/",
    "https://www.smogon.com/forums/attachments/685sb-png.284239/",
    "https://www.smogon.com/forums/attachments/686sb-png.492513/",
    "https://www.smogon.com/forums/attachments/688sb-png.293913/",
    "https://www.smogon.com/forums/attachments/690sb-png.273666/",
    "https://www.smogon.com/forums/attachments/692sb-png.273670/",
    "https://www.smogon.com/forums/attachments/693sb_1-png.653051/",
    "https://www.smogon.com/forums/attachments/694sb-png.293921/",
    "https://www.smogon.com/forums/attachments/696sb-png.492514/",
    "https://www.smogon.com/forums/attachments/697sb-png.276697/",
    "https://www.smogon.com/forums/attachments/698sb-png.492517/",
    "https://www.smogon.com/forums/attachments/699sb-png.492520/",
    "https://www.smogon.com/forums/attachments/700sb-png.492521/",
    "https://www.smogon.com/forums/attachments/701sb-png.273679/",
    "https://www.smogon.com/forums/attachments/702sb-png.282250/",
    "https://www.smogon.com/forums/attachments/703sb-png.290770/",
    "https://www.smogon.com/forums/attachments/704sb-png.284241/",
    "https://www.smogon.com/forums/attachments/705sb-png.492522/",
    "https://www.smogon.com/forums/attachments/706sb-png.492523/",
    "https://www.smogon.com/forums/attachments/707sb-png.284245/",
    "https://www.smogon.com/forums/attachments/708sb-png.290777/",
    "https://www.smogon.com/forums/attachments/710sb-png.273688/",
    "https://www.smogon.com/forums/attachments/712sb-png.282252/",
    "https://www.smogon.com/forums/attachments/713sb-png.492525/",
    "https://www.smogon.com/forums/attachments/714sb-png.492526/",
    "https://www.smogon.com/forums/attachments/716_1sb-png.653053/",
    "https://www.smogon.com/forums/attachments/716_2sb-png.653055/",
    "https://www.smogon.com/forums/attachments/717sb-png.653057/",
    "https://www.smogon.com/forums/attachments/718_1sb-png.275707/",
    "https://www.smogon.com/forums/attachments/718_4sb-png.275709/",
    "https://www.smogon.com/forums/attachments/718_5sb-png.275711/",
    "https://www.smogon.com/forums/attachments/719_1sb-png.653059/",
    "https://www.smogon.com/forums/attachments/720_1sb-png.275713/",
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
