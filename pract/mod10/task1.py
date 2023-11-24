import re
import doctest

def is_valid_password(password):
    """
    Проверяет, является ли пароль password допустимым.

    Args:
    - password (str): Пароль для проверки.

    Returns:
    - bool: True, если пароль соответствует критериям, иначе False.

    >>> is_valid_password("rtG&3FG#Tr^e")
    True
    
    >>> is_valid_password("a^A1@*@1Aa")
    True
    
    >>> is_valid_password("oF^a1D@y5%e6")
    True
    
    >>> is_valid_password("enroi#$*rkdeR#$*092uwedchf34tguv394hNoSpecialChars1")
    True
    
    >>> is_valid_password("пароль")
    False
    
    >>> is_valid_password("password")
    False
        
    >>> is_valid_password("qwerty")
    False
        
    >>> is_valid_password("lOngPa$$W0Rd")
    False
    """


    if not re.search(r'[a-z].*[a-z]', password):
        return False
    

    if not re.search(r'\d', password):
        return False
    

    if not re.search(r'(?:[^$%^@#&*]*[$%^@#&*]){3}', password):
        return False
    
   
    if re.search(r'[,.!?]', password):
        return False
    

    if not re.match(r'[a-zA-Z0-9$%^@#&*]{8,}$', password):
        return False
    
    return True


doctest.testmod(verbose=True)
