import os
import requests
import time

# Configuration
ROOT_FOLDER = "../sprites/pokemon/other"
API_BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"

# Simple in-memory cache to store API responses
# Format: { "877": { ...api_data... } }
species_cache = {}


def get_species_data(pokedex_num):
    """Fetches data from API or returns from cache if already fetched."""
    if pokedex_num in species_cache:
        return species_cache[pokedex_num]

    print(f"--> Fetching API data for Species ID: {pokedex_num}...")
    try:
        response = requests.get(f"{API_BASE_URL}{pokedex_num}")
        if response.status_code == 200:
            data = response.json()
            species_cache[pokedex_num] = data
            return data
        elif response.status_code == 429:
            print("!!! Being rate limited. Sleeping for 5 seconds...")
            time.sleep(5)
            return get_species_data(pokedex_num)
        else:
            print(f"!!! API Error {response.status_code} for ID {pokedex_num}")
            return None
    except Exception as e:
        print(f"!!! Request failed: {e}")
        return None


def process_folders():
    if not os.path.exists(ROOT_FOLDER):
        print(f"Error: Folder '{ROOT_FOLDER}' not found.")
        return

    # os.walk travels through every child folder automatically
    for root, dirs, files in os.walk(ROOT_FOLDER):
        for filename in files:
            # Match files like '877-hangry.png'
            if "-" in filename and filename.endswith(".png"):
                basename = filename.replace(".png", "")
                parts = basename.split("-")

                pokedex_num = parts[0]
                variety_suffix = parts[1].lower()

                species_data = get_species_data(pokedex_num)

                if species_data:
                    species_name = species_data["name"]
                    varieties = species_data["varieties"]

                    # Target name logic: "species-variety" (e.g., "morpeko-hangry")
                    target_match_name = f"{species_name}-{variety_suffix}"

                    new_id = None
                    for v in varieties:
                        if v["pokemon"]["name"] == target_match_name:
                            # Extract numeric ID from the URL string
                            url_parts = v["pokemon"]["url"].strip("/").split("/")
                            new_id = url_parts[-1]
                            break

                    if new_id:
                        old_path = os.path.join(root, filename)
                        new_filename = f"{new_id}.png"
                        new_path = os.path.join(root, new_filename)

                        # Prevent overwriting if the file already exists
                        # if not os.path.exists(new_path):
                        os.rename(old_path, new_path)
                        print(f"Success: [{root}] {filename} -> {new_filename}")
                        # else:
                        #     print(f"Skipped: {new_filename} already exists in {root}")
                    # else:
                    #     print(
                    #         f"Notice: No variety match for '{target_match_name}' in {filename}"
                    #     )


if __name__ == "__main__":
    start_time = time.time()
    process_folders()
    duration = time.time() - start_time
    print(f"\nFinished! Processed folders in {duration:.2f} seconds.")
