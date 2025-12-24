import pickle
import subprocess
import hashlib

PASSWORD = "12345"

def dangerous_eval(user_input):
  return eval(user_input)

def load_data(data):
  return pickle.loads(data)

def clean_cache():
  subprocess.call("rm -rf /tmp", shell=True)

def weak_hash(data):
  return hashlib.md5(data.encode()).hexdigest()
if __name__=="__main__":
  print("PKI Tool running....")
