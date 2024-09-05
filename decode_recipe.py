# decode_recipe.py

# Define the encoding dictionary
ENCODING = {
    'h': 'b', 'g': 'u', 'i': 't', 'k': 'e', 'f': 'r',
    # Add all other mappings here
}

def decode_string(encoded_string):
    """Decode a single encoded string using the ENCODING dictionary."""
    decoded_string = ''.join(ENCODING.get(char, char) for char in encoded_string)
    return decoded_string

def decode_ingredient(encoded_line):
    """Decode a line from the recipe into an Ingredient object."""
    print(f"Decoding line: {encoded_line}")
    # Split the line into amount and description
    amount, encoded_desc = encoded_line.split('#')
    amount = decode_amount(amount)  # Implement decode_amount function
    description = decode_string(encoded_desc)
    return Ingredient(amount, description)

def decode_amount(encoded_amount):
    """Decode the amount part of the ingredient (e.g., '8 vgl' to '1 cup')."""
    # Implement this function based on your requirements
    return '1 cup'

def decode_recipe(file_path):
    """Read and decode the entire recipe from a file."""
    print(f"Decoding recipe from file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    decoded_lines = []
    for line in lines:
        decoded_lines.append(decode_ingredient(line.strip()))
    
    with open('decoded_recipe.txt', 'w') as file:
        for ingredient in decoded_lines:
            file.write(f"{ingredient.amount} {ingredient.description}\n")

class Ingredient:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

# For testing purposes
if __name__ == "__main__":
    print("Script is running")
    decode_recipe('secret_recipe.txt')
