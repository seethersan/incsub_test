import unittest

from exercises import remove_duplicates, sqrt_list, is_palindrome, filter_results


class TestExercises(unittest.TestCase):
    def test_remove_duplicates(self):
        # Test with a list of integers
        arr = [1, 2, 2, 3, 4, 4, 5]
        assert remove_duplicates(arr).sort() == [1, 2, 3, 4, 5].sort()

        # Test with a list of strings
        arr = ["a", "b", "b", "c", "d", "d"]
        assert remove_duplicates(arr).sort() == ["a", "b", "c", "d"].sort()

        # Test with a list that is already free of duplicates
        arr = [1, 2, 3, 4, 5]
        assert remove_duplicates(arr).sort() == [1, 2, 3, 4, 5].sort()

    def test_sqrt_list(self):
        # Test with a list of integers
        arr = [1, 2, 3, 4, 5]
        assert sqrt_list(arr) == [1, 4, 9, 16, 25]

        # Test with a list of integers and a float
        arr = [1, 2, 3, 4.5, 5]
        assert sqrt_list(arr) == None

        # Test with a list of integers and a string
        arr = [1, 2, 3, "4", 5]
        assert sqrt_list(arr) == None

        # Test with an empty list
        arr = []
        assert sqrt_list(arr) == []

    def test_is_palindrome(self):
        # Test with a palindrome string
        word = "madam"
        assert is_palindrome(word) == True

        # Test with a non-palindrome string
        word = "hello"
        assert is_palindrome(word) == False

        # Test with an integer
        word = 12321
        assert is_palindrome(word) == None

        # Test with a float
        word = 12.21
        assert is_palindrome(word) == None

    def test_filter_results(self):
        # Test with a list of results
        results = [
            {"type": "GET", "status": 200, "page": "example.com/one"},
            {"type": "POST", "status": 200, "page": "example.com/two"},
            {"type": "GET", "status": 404, "page": "example.com/three"},
            {"type": "POST", "status": 403, "page": "example.com/four"},
            {"type": "GET", "status": 500, "page": "example.com/five"},
            {"type": "GET", "status": 403, "page": "example.com/six"},
            {"type": "POST", "status": 403, "page": "example.com/seven"},
            {"type": "GET", "status": 403, "page": "example.com/eight"},
        ]
        assert filter_results(results) == ["example.com/six", "example.com/eight"]
        assert filter_results(results, type="POST") == [
            "example.com/four",
            "example.com/seven",
        ]
        assert filter_results(results, status=404) == ["example.com/three"]
        assert filter_results(results, type="POST", status=201) == []


if __name__ == "__main__":
    unittest.main()
