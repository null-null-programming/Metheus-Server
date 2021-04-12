from db_init import dbInit
from models.create_all_db import createDB


def main() -> None:
    createDB()
    dbInit()
    return


if __name__ == "__main__":
    main()
