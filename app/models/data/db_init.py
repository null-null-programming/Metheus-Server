from category import category_data
from set_db_func import category_add_to_DB


def dbInit() -> None:
    def initCategory() -> None:
        for category in category_data:
            category_add_to_DB(category)

    def initAssumption() -> None:
        return

    def initArticle() -> None:
        return

    initCategory()
    initAssumption()
    initArticle()
    return
