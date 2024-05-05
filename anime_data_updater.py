import os
import json

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'data.json')

    # Load existing data from data.json
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
        return

    # Automatically assign the ID as one more than the last entry's ID
    if existing_data:
        last_entry_id = existing_data[-1]['id']
    else:
        last_entry_id = 0
    new_entry_id = last_entry_id + 1

    # Ask the user 6 questions and store the answers in a dictionary
    user_data = {}
    user_data['id'] = new_entry_id
    user_data['anime_name'] = input("Enter Anime Name: ")
    user_data['artist'] = input("Enter Artist: ")
    user_data['song_name'] = input("Enter Song Name: ")
    user_data['genre'] = input("Enter Genre: ")
    user_data['description'] = input("Enter Description: ")
    user_data['osu'] = input("Enter OSU: ")

    # Append the user data to the existing list
    existing_data.append(user_data)

    # Write the updated data back to data.json
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("Data appended successfully.")

if __name__ == "__main__":
    main()
