import glob
import shutil
import os

# 1. Initialize the source and destination paths
source_path = '..\\source\\*'
destination_path = '..\\destination'

# 2. Get the source files with locations
source_objects = glob.glob(source_path)

# Loop through each source file
for object_path in source_objects:
    # Print information for debugging
    print("Source Path:", source_path)
    print("Source Objects:", source_objects)
    print("Object Path:", object_path)

    # Extract filename and extension
    filename = os.path.basename(object_path)
    basename, extension = os.path.splitext(filename)

    # 3. Copy the source file to the server directory with postfixes
    for postfix in range(1, 4):
        new_filename = f"{basename}_{postfix}{extension}"  # Construct new filename with postfix
        destination_file_path = os.path.join(destination_path, new_filename)  # Construct destination file path

        # Copy the source file to the destination with the new filename
        shutil.copy(object_path, destination_file_path)
        print("Copied to:", destination_file_path)

    # Remove the original source file
    os.remove(object_path)

# Print completion message
print("Process completed successfully.")
