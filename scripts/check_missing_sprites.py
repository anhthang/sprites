import os
import pandas as pd

# CONFIGURATION
# Script is in: /Parent/sprites/scripts/
# Data is in:   /Parent/pokeapi/data/v2/csv/
POKEMON_CSV = "../../pokeapi/data/v2/csv/pokemon.csv"
FORMS_CSV = "../../pokeapi/data/v2/csv/pokemon_forms.csv"
VG_CSV = "../../pokeapi/data/v2/csv/version_groups.csv"

# Sprite directories relative to this script
BASE_PATH = "../sprites/pokemon"
PATHS = {
    "Front": BASE_PATH,
    "Front Shiny": os.path.join(BASE_PATH, "shiny"),
    "Back": os.path.join(BASE_PATH, "back"),
    "Back Shiny": os.path.join(BASE_PATH, "back/shiny"),
}


def check_sprites():
    # 1. Validate required files exist
    required_files = [POKEMON_CSV, FORMS_CSV, VG_CSV]
    for f in required_files:
        if not os.path.exists(f):
            print(f"❌ Error: Required CSV missing at: {os.path.abspath(f)}")
            return

    # 2. Prepare Data (Merge Pokemon + Forms + Version Groups to get Generation)
    print("🔍 Loading and merging Pokémon data...")
    df_pokemon = pd.read_csv(POKEMON_CSV)
    df_forms = pd.read_csv(FORMS_CSV)
    df_vg = pd.read_csv(VG_CSV)

    # We use the default form to determine the generation for the Pokemon ID
    # This covers both base pokemon and varieties (Megas, Alolan, etc.)
    df_forms_subset = df_forms[df_forms["is_default"] == 1][
        ["pokemon_id", "introduced_in_version_group_id"]
    ]

    # Merge to get generation_id
    df_merged = df_pokemon.merge(
        df_forms_subset, left_on="id", right_on="pokemon_id", how="left"
    )
    df_merged = df_merged.merge(
        df_vg[["id", "generation_id"]],
        left_on="introduced_in_version_group_id",
        right_on="id",
        how="left",
    )

    # Select final columns and rename for clarity
    pokemon_entries = (
        df_merged[["id_x", "identifier", "generation_id"]]
        .rename(columns={"id_x": "id"})
        .to_dict("records")
    )

    # Dictionary to store missing results
    results = {key: [] for key in PATHS.keys()}

    # 3. Check Local Files
    print(f"🧪 Comparing {len(pokemon_entries)} entries against local files...")

    for pokemon in pokemon_entries:
        p_id = pokemon["id"]
        name = pokemon["identifier"]
        gen = pokemon["generation_id"]
        filename = f"{p_id}.png"

        for label, folder in PATHS.items():
            if os.path.exists(folder):
                file_path = os.path.join(folder, filename)
                if not os.path.exists(file_path):
                    results[label].append(
                        {
                            "id": p_id,
                            "identifier": name,
                            "generation": int(gen) if pd.notnull(gen) else "Unknown",
                        }
                    )

    # 4. Detailed Console Output
    print("\n" + "=" * 50)
    print("             MISSING ASSETS REPORT")
    print("=" * 50)

    for label, missing_list in results.items():
        count = len(missing_list)
        icon = "✨" if "Shiny" in label else "👤"
        direction = "➡️" if "Front" in label else "⬅️"

        print(f"\n{icon} {direction} {label.upper()} ({count} missing):")

        if missing_list:
            # Sort by ID for the print preview
            missing_list.sort(key=lambda x: x["id"])
            for item in missing_list[:10]:
                print(
                    f"  - Gen {item['generation']} | {item['id']}: {item['identifier']}"
                )
            if count > 10:
                print(f"  ... and {count - 10} others.")

            # Export CSV for this category
            file_safe_name = label.lower().replace(" ", "_")
            pd.DataFrame(missing_list).to_csv(
                f"missing_{file_safe_name}.csv", index=False
            )
        else:
            print("  ✅ All assets present!")

    print("\n" + "=" * 50)
    print("📝 Results with Generation IDs saved to CSV files.")
    print("=" * 50)


if __name__ == "__main__":
    check_sprites()
