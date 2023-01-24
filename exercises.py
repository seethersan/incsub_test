def remove_duplicates(arr):
    """
    Removes duplicates from a list of elements.

    Parameters:
    arr (list): The list of elements to remove duplicates from

    Returns:
    list: A new list with duplicates removed
    """
    return list(set(arr))


def sqrt_list(arr):
    """
    Returns the square of each element in a list of integers.

    Parameters:
    arr (list): The list of integers to square

    Returns:
    list: A new list with the square of each element
    None: If any element of the input is not a integer
    """
    if any([type(num) != int for num in arr]):
        return None
    return [num * num for num in arr]


def is_palindrome(word):
    """
    Check if a given word is a palindrome.

    Parameters:
    word (str): The word to check if it is a palindrome.

    Returns:
    bool: True if the word is a palindrome, False otherwise.
    None: If the input is not a string
    """
    if type(word) != str:
        return None
    return word == word[::-1]


def filter_results(results, type="GET", status=403):
    """
    Filters a list of results by type and status.

    Parameters:
    results (list): A list of results to filter.
    type (str): The type of result to filter for. Default is "GET".
    status (int): The status of result to filter for. Default is 403.

    Returns:
    list: A new list containing the filtered results.
    """
    return [
        result["page"]
        for result in results
        if (result["type"] == type and result["status"] == status)
    ]
