# This is a method that returns a boolean value based on the input yes for True and no for False.
def boolean(input_value):
    """
    Convert input to a boolean value.
    
    Args:
        input_value (str): Input string, expected to be 'yes' or 'no'.
        
    Returns:
        bool: True if input is 'yes', False if input is 'no'.
        
    Raises:
        ValueError: If input is not 'yes' or 'no'.
    """
    if input_value.lower() == 'yes':
        return True
    elif input_value.lower() == 'no':
        return False
    else:
        raise ValueError("Input must be 'yes' or 'no'.")