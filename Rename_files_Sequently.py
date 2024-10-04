import os

# Specify the directory containing the images
output_folder = 'D:/frames'

# Get a list of all files in the directory
files = sorted(os.listdir(output_folder), key=lambda x: int(x.split('.')[0]))

# # Get a sorted list of files with names like "crop_1.jpg", "crop_2.jpg", etc.
# files = sorted(os.listdir(output_folder), key=lambda x: int(x.split('_')[1].split('.')[0]))

# Filter only .jpg files (if needed)
jpg_files = [f for f in files if f.endswith('.jpeg')]

# Rename files sequentially
for new_number, old_file in enumerate(jpg_files, start=1):
    # Construct old and new file paths
    old_file_path = os.path.join(output_folder, old_file)
    new_file_name = f"{new_number}.jpg"
    new_file_path = os.path.join(output_folder, new_file_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)
    print(f"Renamed: {old_file} to {new_file_name}")

print("Renaming completed.")