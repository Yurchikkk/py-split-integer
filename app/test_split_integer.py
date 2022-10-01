from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    value = 5
    parts = split_integer(value, 2)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value = 8
    parts = split_integer(value, 4)
    assert parts[0] == parts[1]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 4
    parts = split_integer(value, 1)
    assert len(parts) == 1


def test_parts_should_be_sorted_when_they_are_not_equal():
    value = 15
    parts = split_integer(value, 7)
    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value = 3
    parts = split_integer(value, 6)
    assert parts == [0, 0, 0, 1, 1, 1]
