from hello import add, add2, subtract


def test_add():
    assert add(1, 2) == 3


def setup_function(function):
    print(f"Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f"Running teardown: {function.__name__} ")


# failed test
# def test_hello_add():
#     assert add2(test_hello_add.x) == 12


def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
