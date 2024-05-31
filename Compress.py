import zlib
import os

# Define the file paths
input_file_path = 'Example.txt'
compressed_file_path = 'compressed_file.zlib'
decompressed_file_path = 'decompressed_file.txt'

# Step 1: Read the input text file
with open(input_file_path, 'rb') as file:
    file_data = file.read()

# Step 2: Compress the data
compressed_data = zlib.compress(file_data)

# Step 3: Write the compressed data to a new file
with open(compressed_file_path, 'wb') as file:
    file.write(compressed_data)

# Optional Step 4: Decompress the data to verify
with open(compressed_file_path, 'rb') as file:
    compressed_data = file.read()

decompressed_data = zlib.decompress(compressed_data)

# Write the decompressed data to a new file
with open(decompressed_file_path, 'wb') as file:
    file.write(decompressed_data)

# Step 5: Check file sizes
original_size = os.path.getsize(input_file_path)
compressed_size = os.path.getsize(compressed_file_path)
decompressed_size = os.path.getsize(decompressed_file_path)

print(f"Original file size: {original_size} bytes")
print(f"Compressed file size: {compressed_size} bytes")
print(f"Decompressed file size: {decompressed_size} bytes")

# Verify if decompressed data matches original data
if file_data == decompressed_data:
    print("Success: Decompressed data matches the original data.")
else:
    print("Error: Decompressed data does not match the original data.")
