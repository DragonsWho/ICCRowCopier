import json
import sys
import copy
import re

def update_ids_and_titles(row, new_row_number):
    # Update row ID
    row['id'] = f'row-{new_row_number}'
    
    # Update row Title
    row['title'] = f"row-{new_row_number}"

    # Function to update ID
    def update_id(id_string):
        parts = id_string.rsplit('-', 1)
        if len(parts) == 2:
            return f"{parts[0]}-{new_row_number}"
        return id_string

    # Recursive function to traverse all nested elements
    def recursive_update(element):
        if isinstance(element, dict):
            for key, value in element.items():
                if key in ['id', 'reqId', 'req'] and isinstance(value, str) and '-' in value:
                    element[key] = update_id(value)
                elif key != 'image':  # Ignore 'image' key
                    recursive_update(value)
        elif isinstance(element, list):
            for item in element:
                recursive_update(item)

    # Apply recursive update to the entire row
    recursive_update(row)

def copy_row(data, source_row_id, target_row_id, new_row_number):
    try:
        source_index = next(i for i, row in enumerate(data['rows']) if row['id'] == source_row_id)
    except StopIteration:
        print(f"Error: Source row with id '{source_row_id}' not found.")
        return

    try:
        target_index = next(i for i, row in enumerate(data['rows']) if row['id'] == target_row_id)
    except StopIteration:
        print(f"Error: Target row with id '{target_row_id}' not found.")
        return

    new_row = copy.deepcopy(data['rows'][source_index])
    update_ids_and_titles(new_row, new_row_number)
    new_row['rowNumber'] = new_row_number

    data['rows'].insert(target_index + 1, new_row)

    print(f"Row successfully copied. New id: {new_row['id']}")

def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py <path_to_json_file> <source_row_id> <target_row_id> <new_row_number>")
        return

    json_file = sys.argv[1]
    source_row_id = sys.argv[2]
    target_row_id = sys.argv[3]
    new_row_number = sys.argv[4]

    with open(json_file, 'r') as f:
        data = json.load(f)

    copy_row(data, source_row_id, target_row_id, new_row_number)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()