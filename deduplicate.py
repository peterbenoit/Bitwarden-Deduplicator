import json
from collections import defaultdict

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def find_duplicates(items):
    unique_items = []
    duplicates = defaultdict(list)
    seen = set()

    for item in items:
        if item["type"] == 1:  # Login
            unique_key = (
                item["name"],
                item["login"]["username"] if item.get("login") else None,
                tuple(uri["uri"] for uri in item["login"]["uris"]) if item.get("login") and item["login"].get("uris") else ()
            )
        elif item["type"] == 2:  # Secure Note
            unique_key = (item["name"], item["notes"])
        elif item["type"] == 3:  # Card
            unique_key = (item["name"], item["card"]["number"] if item.get("card") else None)
        elif item["type"] == 4:  # Identity
            unique_key = (
                item["name"],
                item["identity"]["firstName"] if item.get("identity") else None,
                item["identity"]["lastName"] if item.get("identity") else None
            )
        else:
            unique_key = (item["name"],)

        if unique_key in seen:
            duplicates[unique_key].append(item)
        else:
            seen.add(unique_key)
            unique_items.append(item)

    return unique_items, duplicates

def save_json(data, file_path):
    # Convert tuple keys to strings for JSON compatibility
    if "duplicates" in data:
        data["duplicates"] = {str(key): value for key, value in data["duplicates"].items()}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Load the Bitwarden JSON file
data = load_json("bitwarden-export.json")

# Process duplicates
unique_items, duplicates = find_duplicates(data["items"])

# Save unique items and duplicates to separate files
save_json({"items": unique_items}, "bitwarden_cleaned.json")
save_json({"duplicates": duplicates}, "bitwarden_duplicates.json")

print(f"Unique items saved to bitwarden_cleaned.json")
print(f"Duplicates saved to bitwarden_duplicates.json")
