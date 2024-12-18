def get_test_data():
    """
    Returns a list of dictionaries containing test data.
    """
    try:
        test_data = [
            {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "age": 25, "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"},
            {"id": 4, "name": "Diana", "age": 28, "email": "diana@example.com"}
        ]
        return test_data
    except Exception as e:
        print(f"Error fetching test data: {e}")
        return []


