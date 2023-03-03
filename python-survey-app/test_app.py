from extract import get_input 

filename = "python-survey-app/results.csv"

# Ticket 1

def test_input_is_list():
    # Arrange
    expected_output = list

    # Act
    output = get_input(filename)

    # Assert
    assert type(output) == expected_output


def test_input_is_correct():
    # Arrange
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expected_rowcount = 25

    # Act
    output = get_input(filename)
    actual_columns = output[0]
    actual_rowcount = len(output[1:])
    # actual_rowcount = len(output) - 1

    # Assert
    # assert output_df.columns == expected_columns
    # assert output[0] == expected_columns
    # assert output_df.shape[0] == expected_rowcount
    assert actual_columns == expected_columns
    assert actual_rowcount == expected_rowcount

# shape[0] would show the number of rows
# shape[1] would show the number of columns


def test_input_fails_if_file_not_found():
    pass

# Ticket 2

def test_remove_duplicates():
    # Arrange
    expected_rowcount = 21

    # Act
    output = get_input(filename)

    # items in a set list are unordered, so it will appear in random order
    appeared = set()
    uniq = []
    for row in output:
        if row[0] not in appeared:
            appeared.add(row[0])
            uniq.append(row)     

    actual_rowcount = len(uniq[1:])
    
    # Assert
    assert actual_rowcount == expected_rowcount

