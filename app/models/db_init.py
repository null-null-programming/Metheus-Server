from assumption.biology_assumption_data import biology_data
from assumption.chemistory_assumption_data import chemistory_data
from assumption.computer_assumption_data import computer_data
from assumption.mathmatics_assumpton_data import mathmatics_data
from assumption.physics_assumption_data import physics_data
from category.category_data import category_data
from set_db_func import assumption_add_to_DB, category_add_to_DB

data_list = [
    biology_data,
    chemistory_data,
    computer_data,
    mathmatics_data,
    physics_data,
]


def dbInit() -> None:
    def initCategory() -> None:
        for category in category_data:
            category_add_to_DB(category)

    def initAssumption() -> None:
        for assumptions in data_list:
            for data in assumptions:
                assumption_add_to_DB(data)

    initCategory()
    initAssumption()
    return


if __name__ == "__main__":
    dbInit()
