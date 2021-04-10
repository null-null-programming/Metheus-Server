"""
TODO: あくまでサンプルなのでテスト書き始めたら消す
"""


def test_reverse_str():
    string = "Hello, World!"
    reversed_str = "!dlroW ,olleH"
    test = "This is test!!!!"
    print(test)

    assert string[::-1] == reversed_str


def test_sort():
    arr = [4, 5, 1, 3, 0, 6]
    sorted_arr = [0, 1, 3, 4, 5, 6]

    assert sorted(arr) == sorted_arr
