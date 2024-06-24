# Row-Copier-for-ICC
This Python script is designed to copy rows in the project.json file of a CYOA created with ICC. (https://hikawasisters.neocities.org/ICCPlus/)

# How It Works
1. The script takes four command-line arguments:
- Path to the JSON file
- ID of the source row to be copied
- ID of the target row (the new row will be inserted after this)
- New row number for the copied row
2. It loads the JSON data from the specified file.
3. The script then copies the source row and inserts it after the target row.
4. All IDs within the copied row are updated to reflect the new row number. This includes:
- The main row ID
- IDs of nested elements
- Any fields named 'id', 'reqId', or 'req' that contain a hyphen
5. The updated JSON is then written back to the file.

# Usage
Run the script from the command line as follows:

`python ICCRowCopier.py <path_to_json_file> <source_row_id> <target_row_id> <new_row_number>`

For example: `python ICCRowCopier.py project.json row-1 row-2 9`
This will copy the row with ID "row-1", insert it after "row-2", and update all its IDs to use the number 9.

# Notes
The original row should have IDs of the form row-1, choice-1, etc. All hyphenated and with one serial number. 
All these sequence numbers will be replaced by the one you specified, including in the requirements. 
