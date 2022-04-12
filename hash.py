import os
import stat
import glob
import hashlib
from deepdiff import DeepDiff

file_dictionary = {}
hash_dictionary = {}

def compare(time): #Checks if file contents changed and if there is any missing or added files
    log_list = sorted(glob.glob('log*.txt')) #logs sorted by last accessed date
    old = log_list[-2]
    with open(old, 'r') as old:
        old_opened = old.readlines()
    old_dic = old_opened[0]
    with open('log' + time + ".txt", 'w') as new: #log file is saved with  name of date and time last accessed
        new_opened = new.readlines()
    new_dic = new_opened[0]
    diff = DeepDiff(old_dic, new_dic) #compares the two VM dictionaries
    if old_dic == new_dic:
        print("Nothing has been changed!")
    else:
        print(diff) #Prints out changes

def store_values(time):
    with open('log' + time + ".txt", 'w') as f:  #Creates log file to store hashses
        f.write(hash_dictionary)
    if file_dictionary[glob.glob("log*.txt")] == true: #If a log file exists, it will be compared to current log file
        #log file in code
        compare(time)

def hashing(): #Hashes files
  hashing = hashlib.sha256()
  for path in file_dictionary:
    time_date = os.stat(path) #last accessed
    with open(file_dictionary[path], "rb") as f:
      for byte_block in iter(lambda: f.read(4096),b""):
        hashing.update(byte_block)
      new_values = [path, file_dictionary[path], time_date] #stores full path, filename, and last access time
      hash_dictionary[hashing.hexdigest()] = new_values #Hash is the key
      store_values(time_date)


def main():
    for dirpath, dirs, files in os.walk("/"): #Iterates through directories
      for filename in files:
        full_path = os.path.join(dirpath, filename) #Joins the path and the filename to create a full path
        if "/dev" in full_path or "inst" in full_path or "uuid" in full_path or "gz" in full_path or "deep" in full_path or "/proc/" in full_path or "/run/" in full_path or "vmlinuz" in full_path or "initrd" in full_path or "/sys/" in full_path or "tmp" in full_path or "/var/lib/" in full_path or "/var/run/" in full_path or "/Downloads/" in full_path:
          continue #If any of these phrases are a part of directory or file name, then it is ignored
        file_dictionary[full_path] = filename   #Appends the full path as key and
    hashing()


if __name__== "__main__":
    main()
