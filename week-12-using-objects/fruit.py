def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    # Print the fruit list in reverse order.
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Append "orange" fruit list.
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    # Find where "apple" is located in fruit_list and insert 
    # "cherry" before "apple" in the list and print the list.
    i_apple = fruit_list.index("apple")
    fruit_list.insert(i_apple, "cherry")
    print(f"insert cherry: {fruit_list}")

    # Remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    # Pop the last element from fruit_list and print the 
    # popped element and the list.
    last = fruit_list.pop()
    print(f"pop {last}: {fruit_list}")

    # Sort and print fruit_list.
    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    # Clear and print fruit_list.
    fruit_list.clear()
    print(f"cleared {fruit_list}")


# If this file is executed like this:
# > python check_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
