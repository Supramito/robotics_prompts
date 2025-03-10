#Day 7
#I learned how to pu an if sattment inside a if statement.

def main():
    # Basic nested list example
    print("=== NESTED LISTS ===")
    nested_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Accessing elements in nested lists
    print("\nAccessing elements:")
    print(f"First row: {nested_list[0]}")
    print(f"Element at row 1, column 2: {nested_list[1][2]}")
    
    # Iterating through nested lists
    print("\nIterating through nested list:")
    for row in nested_list:
        for item in row:
            print(item, end=" ")
        print()  # New line after each row
    
    # Nested dictionary example
    print("\n\n=== NESTED DICTIONARIES ===")
    user_data = {
        "user1": {
            "name": "John Smith",
            "age": 28,
            "hobbies": ["reading", "swimming", "coding"],
            "contact": {
                "email": "john@example.com",
                "phone": "555-1234"
            }
        },
        "user2": {
            "name": "Emily Johnson",
            "age": 32,
            "hobbies": ["hiking", "photography"],
            "contact": {
                "email": "emily@example.com",
                "phone": "555-5678"
            }
        }
    }
    
    # Accessing nested dictionary data
    print("\nAccessing nested dictionary data:")
    print(f"User1's name: {user_data['user1']['name']}")
    print(f"User2's hobbies: {user_data['user2']['hobbies']}")
    print(f"User1's email: {user_data['user1']['contact']['email']}")
    
    # Common error demonstration (with error handling)
    print("\n\n=== COMMON ERRORS AND HANDLING ===")
    
    # KeyError handling
    try:
        print(user_data["user3"]["name"])
    except KeyError as e:
        print(f"KeyError caught: {e}")
        
    # IndexError handling
    try:
        print(nested_list[5][0])
    except IndexError as e:
        print(f"IndexError caught: {e}")
    
    # TypeError handling
    try:
        print(nested_list["first"][0])
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    # Challenge: Find the average age of all users
    print("\n\n=== CHALLENGE SOLUTION ===")
    total_age = 0
    user_count = 0
    
    for user_id, user_info in user_data.items():
        total_age += user_info["age"]
        user_count += 1
    
    average_age = total_age / user_count if user_count > 0 else 0
    print(f"Average age of all users: {average_age}")
    
    # Challenge: Count total hobbies across all users
    all_hobbies = []
    for user_id, user_info in user_data.items():
        all_hobbies.extend(user_info["hobbies"])
    
    unique_hobbies = set(all_hobbies)
    print(f"Total unique hobbies: {len(unique_hobbies)}")
    print(f"All unique hobbies: {', '.join(unique_hobbies)}")

if __name__ == "__main__":
    main()
