import sys
from config import DB_DETAILS
def main():
    print('hello world')
    env = sys.argv[1]
    db_details = DB_DETAILS[env]

if __name__ == '__main__' :
    main()