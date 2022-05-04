""" This should only be used to run cProfile, outlined in the README """
import cProfile
from app.github.file import get_single_file_of_repo
from app.github.loc import get_account_loc

def test_file():
    print("=== TESTING GET_SINGLE_FILE_OF_REPO ===")
    cProfile.runctx("get_single_file_of_repo(username='alexmerren')", globals(), locals(), filename=None)

def test_loc():
    print("=== GET_ACCOUNT_LOC ===")
    cProfile.runctx("get_account_loc(username='alexmerren')", globals(), locals(), filename=None)

if __name__ == "__main__":
    test_file()
