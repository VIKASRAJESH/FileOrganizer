import os
import shutil

# Define file type categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".doc"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv"],
    "Others": []  # Catch-all for unknown extensions
}

# Get the directory path
dir_path = input("Enter the directory path: ")

# Loop through each file in the directory
for filename in os.listdir(dir_path):
    # Get file extension
    file_extension = os.path.splitext(filename)[1].lower()

    # Find the category for the extension
    category = None
    for category_name, extensions in file_categories.items():
        if file_extension in extensions:
            category = category_name
            break

    # If no category found, put it in "Others"
    if not category:
        category = "Others"

    # Create the category folder if it doesn't exist
    category_path = os.path.join(dir_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    # Move the file to the category folder
    source_file = os.path.join(dir_path, filename)
    destination_file = os.path.join(category_path, filename)
    shutil.move(source_file, destination_file)

print("Files organized successfully!")