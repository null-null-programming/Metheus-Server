from models.create_all_db import createDB
from db_init import dbInit


def main() -> None:
    createDB()
    dbInit()
    return


if __name__ == "__main__":
    main()
