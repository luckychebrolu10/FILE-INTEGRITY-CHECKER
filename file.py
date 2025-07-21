import hashlib
import os

def get_file_hash(filename):
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return None
    with open(filename, 'rb') as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

def check_integrity(original_file, copy_file):
    hash1 = get_file_hash(original_file)
    hash2 = get_file_hash(copy_file)

    if hash1 is None or hash2 is None:
        print("[WARNING] Could not compute hash due to missing file.")
        return

    print(f"Hash of {original_file}: {hash1}")
    print(f"Hash of {copy_file}:   {hash2}")
    
    if hash1 == hash2:
        print("\n[SUCCESS] File integrity maintained.")
    else:
        print("\n[WARNING] File has been modified!")

# Example usage
check_integrity("original.txt", "copy.txt")
