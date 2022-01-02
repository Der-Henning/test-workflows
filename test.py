from os import environ
from random import random


def main():
  old_access_token = environ.get("ACCESS_TOKEN", None)
  print("Access Token from secret: {}".format(old_access_token))
  print("Correct Token: {}".format(print(old_access_token.startswith('ThisIsASecret'))))
  env_file = environ.get('GITHUB_ENV', None)
  if env_file:
    with open(env_file, "a") as file:
      file.write("NEW_ACCESS_TOKEN={}{}\n".format("ThisIsASecret", random()))

if __name__ == "__main__":
  main()
