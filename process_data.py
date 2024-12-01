
def add_one_to_values(values):
    """Simple function to add 1 to each value in the list."""
    return [value + 1 for value in values]

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    processed_data = add_one_to_values(data)
    print(processed_data) 
  
