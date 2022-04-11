import os
import stat

file_dictionary = {}
hash_dictionary = {}
for dirpath, dirs, files in os.walk("./~"):
  for filename in files: 
    full_path = os.path.join(dirpath, filename)
    if "/dev" in full_path or "/proc/" in full_path or "/run/" in full_path or "/sys/" in full_path or "tmp" in full_path or "/var/lib/" in full_path or "/var/run/" in full_path or "/Downloads/"
      continue 
    file_dictionary[full_path] = filename
hashing()

def hashing()
  hashing = hashlib.sha256()
  for path in file_dictionary:
    time_date = os.stat(path)
    with open(file_dictionary[path], "rb") as f:
      for byte_block in iter(lamda: f.read(4096),b""):
        hashing.update(byte_block)
      new_values = [path, file_dictionary[path], time_date]
      hash_dictionary[hashing.hexdigest()] = new_values
  store_values()

store_values():
  #conditional if initial hashing
  #conditional if this is the update hashing (check)
  with open
      

  
        

