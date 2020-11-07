from typing import List, Tuple, Union
# Instead of always transmitting an "original" dictionary, it is simpler to just agree on an initial set.
# Here we use the 256 possible values of a byte:
common_dictionary = list(range(256))

def encode(plain_text: str) -> List[int]:
    # Change to bytes for 256.
    plain_text = plain_text.encode('utf-8')

    # Changing the common dictionary is a bad idea. Make a copy.
    dictionary = common_dictionary.copy()

    # Transformation
    compressed_text = list()          # Regular array
    rank = 0

    # Read in each character
    for c in plain_text:
        rank = dictionary.index(c)    # Find the rank of the character in the dictionary [O(k)]
        compressed_text.append(rank)  # Update the encoded text

        # Update the dictionary [O(k)]
        dictionary.pop(rank)
        dictionary.insert(0, c)

    return compressed_text   
def decode(compressed_data: List[int]) -> str:
    compressed_text = compressed_data
    dictionary = common_dictionary.copy()
    plain_text = []

    # Read in each rank in the encoded text
    for rank in compressed_text:
        # Read the character of that rank from the dictionary
        plain_text.append(dictionary[rank])

        # Update the dictionary
        e = dictionary.pop(rank)
        dictionary.insert(0, e)

    return bytes(plain_text).decode('utf-8')  # Return original string
print(encode('Wikipedia'))
print(decode([119, 106, 108, 1, 113, 105, 105, 3, 103]))
print(encode('Nam The'))


