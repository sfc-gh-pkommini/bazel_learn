from src.name import get_name


def test_value():
    assert get_name() == "Bazel"


if __name__ == "__main__":
    test_value()
