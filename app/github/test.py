""" This should only be used to run cProfile, outlined in the README """
import cProfile
from api import get_single_file_of_repo

def main():
    cProfile.runctx("get_single_file_of_repo(username='alexmerren')", globals(), locals(), filename=None)

if __name__ == "__main__":
    main()
