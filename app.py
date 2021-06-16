import sys
from util import get_tables
from config import DB_DETAILS
def main():

    #env = sys.argv[1]
    #db_details = DB_DETAILS[env]
    tables = get_tables('table_list.txt')
    for i in tables['table_name']:
        print(i)
if __name__ == '__main__':
    main()