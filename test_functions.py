"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""


from my_module.functions import encode_message, decode_message, generate_random_list_of_numbers, message_to_encode


message = input("What do you want to encode?  ")

encoded_message = encode_message(message)



def test_generate_random_list_of_numbers(message):
    """Test for the 'generate_random_list_of_numbers function."""
    
    
    assert len(generate_random_list_of_numbers(message)) == len(message)
    
    assert type(generate_random_list_of_numbers(message)) == list
    
    assert generate_random_list_of_numbers(message)[1] == int

def test_encode_message(message):
    """Test for the 'encode_message' function."""
    
    assert len(encode_message(message)) == len (message)
    
    assert type(encode_message(message)) == str
    
    assert (encode_message(message)) != message
    
    
def test_decode_message(encoded_message):
    """Test for the 'decode_message' function."""
    
    assert len(decode_message(encoded_message)) == len(message)
    
    assert decode_message(encoded_message) == message
    



                 
    