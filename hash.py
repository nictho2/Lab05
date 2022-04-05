import os

for dirpath, dirs, files in os.walk("./~"):
  for filename in files: 
    
    full_path = os.path.join(dirpath, filename)
    if "/dev" in full_path or "/proc/" in full_path or "/run/" in full_path or "/sys/" in full_path or "tmp" in full_path or "/var/lib/" in full_path or "/var/run/" in full_path or "/Downloads/"
      continue 
    with open(full_path) as myfile:
      print(myfile.read())
