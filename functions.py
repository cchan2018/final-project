"""A collection of function for doing my project."""


import random


list_of_character = []

random_num_list = []


def generate_random_list_of_numbers(message):
    """Generate a random list of numbers, used to encode the message later.
    
    Parameters
    ----------
    message : string
        The message to be encoded.
           
    Returns
    -------
    random_num_list: list
        List of randomly generated numbers.
    """

    # Convert every character in the message from string to list.
    list_of_character = list(message)
    
    # Convert every character in the list to a random number from 1 to 100.
    for character in list_of_character:
        
        character = random.choice(range(1,100))
        random_num_list.append(character)
       
    return random_num_list


ord_list_of_character = []

encoded_ord_list = []

encoded_message_list = []

encoded_message = ''


def encode_message(message):
    """Encode a message by adding a ramdomly generated list of numbers to the unicode.
    
    Parameters
    ----------
    message : string
        The message to be encoded.
           
    Returns
    -------
    encoded_message: string
        Randomly encoded message.
    """
    
    # Convert the letter in the meesage to unicode.
    for letter in message:
        
        ord_list_of_character.append(ord(letter))
        
    # Add the number in 'ord_list_of_character' and 'random_num_list' together.
    for (num1, num2) in zip(ord_list_of_character, random_num_list):
        
        encoded_ord_list.append(num1 + num2)
        
    for num in encoded_ord_list:
        
        encoded_message_list.append(chr(num))
        
    # To make the variable 'decoded_message' usable inside and outside the function
    global encoded_message
    
    # join the list of characters together and convert it to string
    space = ''
    
    encoded_message = space.join(encoded_message_list)
    
    return encoded_message


ord_of_encoded_message = []

ord_of_original_message = []

decoded_message = ''

list_of_encoded_message = []


def decode_message(encoded_message):
    """Decode the message that was just encoded using the previous functions.
    
    Parameters
    ----------
    encoded_message : string
        The encoded message and is ready to be decoded.
           
    Returns
    -------
    decoded_message: string
        The decoded message, which is the origninal message.
    """
    
    # Convert encoded message to a list of characters
    list_of_encoded_message.append(list(encoded_message))
    
    for character in encoded_message:
        
        ord_of_encoded_message.append(ord(character))
        
    for (num1, num2) in zip(ord_of_encoded_message, random_num_list):
        
        num = num1-num2
        ord_of_original_message.append(num)
    
    # To make the variable 'decoded_message' usable inside and outside the function
    global decoded_message
    
    for num in ord_of_original_message:
        
        decoded_message = decoded_message + chr(num)
        
    return decoded_message


def gathering_outputs(message):
    """Print out the encoded message, decoded message, and the randomly generated list of numbers.
    Parameters
    ----------
    message : string
        The message that the user wants to encode
    """
    
    print("ramdomly generated list of numbers: ")
    
    print(generate_random_list_of_numbers(message))
    
    print("\n")
    
    print("encoded message: " + encode_message(message))
    
    print("\n")
    
    print("decoded message: " + decode_message(encode_message(message)))
          
    print("\n")
    
    print("Done! Remember that every time you want to encode a new message, you have to restart the kernel and clear output because this function does not automatically clear the old data!")
    

