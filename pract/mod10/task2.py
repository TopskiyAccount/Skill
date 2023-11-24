import re
import doctest

def isValidDate(date):
    """
    Проверяет, является ли дата date допустимой.

    Args:
    - date (str): Дата для проверки.

    Returns:
    - bool: True, если дата соответствует критериям, иначе False.

    >>> isValidDate("20 января 1806")
    True
    
    >>> isValidDate("1924, July 25")
    True
    
    >>> isValidDate("26/09/1635")
    True
    
    >>> isValidDate("3.1.1506")
    True
    
    >>> isValidDate("25.08-1002")
    False
    
    >>> isValidDate("декабря 19, 1838")
    False
        
    >>> isValidDate("8.20.1973")
    False
        
    >>> isValidDate("Jun 7, -1563")
    False
        
    >>> isValidDate("31 февраля 2023")
    False
        
    >>> isValidDate("31 июня 2015")
    False
    """

    pattern = (
        r"^((?:[1-9]|[1-2]\d|30|31)/(?:[1-9]|0[1-9]|10|11|12)/\d{4})$|"  
        r"^((?:[1-9]|[1-2]\d|30|31)\.(?:[1-9]|0[1-9]|10|11|12)\.\d{4})$|"
        r"^(\d{1,4}\,\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря|January|February|March|April|May|June|July|August|September|October|November|December)\s(?:[1-9]|[1-2]\d|30|31))$|"
        r"^((?:[1-9]|[1-2]\d|30|31)\s(?:января|марта|мая|июля|августа|октября|декабря|January|March|May|July|August|October||December)\s\d{1,4})$|"
        r"^((?:[1-9]|[1-2]\d|30)\s(?:|апреля|июня|сентября|ноября|April|June|September|November|)\s\d{1,4})$|"
        r"^((?:[1-9]|[1]\d|2[0-8]|)\s(?:февраля|February)\s\d{1,4})$"
    )

    return re.match(pattern, date) is not None

doctest.testmod(verbose=True)
