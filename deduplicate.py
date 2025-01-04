import json
import argparse
from collections import defaultdict

# Function to load the JSON file
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Function to find duplicates
def find_duplicates(items, type_filter=None):
    unique_items = []
    duplicates = defaultdict(list)
    seen = set()

    for item in items:
        # Skip if type doesn't match the filter
        if type_filter and item["type"] != type_filter:
            continue

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

# Function to save JSON data
def save_json(data, file_path):
    # Convert tuple keys to strings for JSON compatibility
    if "duplicates" in data:
        data["duplicates"] = {str(key): value for key, value in data["duplicates"].items()}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bitwarden Deduplication Script")
    parser.add_argument("input", help="Path to the Bitwarden JSON export file")
    parser.add_argument("--type", type=int, choices=[1, 2, 3, 4], help="Filter by type: 1 (Login), 2 (Secure Note), 3 (Card), 4 (Identity)")
    parser.add_argument("--output-unique", action="store_true", help="Save only unique items")
    parser.add_argument("--output-duplicates", action="store_true", help="Save only duplicate items")
    parser.add_argument("--output-both", action="store_true", help="Save both unique and duplicate items (default)")

    args = parser.parse_args()

    # Load the input JSON file
    data = load_json(args.input)

    # Process duplicates
    unique_items, duplicates = find_duplicates(data["items"], type_filter=args.type)

    # Save results based on the selected options
    if args.output_unique or args.output_both:
        save_json({"items": unique_items}, "bitwarden_cleaned.json")
        print("Unique items saved to bitwarden_cleaned.json")

    if args.output_duplicates or args.output_both:
        save_json({"duplicates": duplicates}, "bitwarden_duplicates.json")
        print("Duplicates saved to bitwarden_duplicates.json")

# Entry point
if __name__ == "__main__":
    main()
