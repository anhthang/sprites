import os
import requests

# Configuration
FOLDER_PATH = "../sprites/pokemon/other/official-artwork"
API_BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"


def rename_pokemon_varieties():
    if not os.path.exists(FOLDER_PATH):
        print(f"Error: Folder '{FOLDER_PATH}' not found.")
        return

    for filename in os.listdir(FOLDER_PATH):
        # Only check files that contain a dash '-'
        if "-" in filename and filename.endswith(".png"):
            basename = filename.replace(".png", "")
            parts = basename.split("-")

            pokedex_num = parts[0]
            variety_name_part = parts[1].lower()

            print(
                f"Checking: {filename} (ID: {pokedex_num}, Variety: {variety_name_part})"
            )

            # Call PokéAPI for the species data
            response = requests.get(f"{API_BASE_URL}{pokedex_num}")

            if response.status_code == 200:
                data = response.json()
                species_name = data["name"]
                varieties = data["varieties"]

                # Target name to match (e.g., "morpeko-hangry")
                target_match_name = f"{species_name}-{variety_name_part}"

                new_id = None
                for v in varieties:
                    if v["pokemon"]["name"] == target_match_name:
                        # Extract ID from URL: https://pokeapi.co/api/v2/pokemon/10187/
                        url_parts = v["pokemon"]["url"].strip("/").split("/")
                        new_id = url_parts[-1]
                        break

                if new_id:
                    new_filename = f"{new_id}.png"
                    old_path = os.path.join(FOLDER_PATH, filename)
                    new_path = os.path.join(FOLDER_PATH, new_filename)

                    try:
                        os.rename(old_path, new_path)
                        print(f"  Success! Renamed to: {new_filename}")
                    except OSError as e:
                        print(f"  Error renaming: {e}")
                else:
                    print(f"  No matching variety found for {target_match_name}")
            else:
                print(f"  API Error: Could not find species {pokedex_num}")


if __name__ == "__main__":
    rename_pokemon_varieties()
