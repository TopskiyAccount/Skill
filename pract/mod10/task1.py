import re
import doctest

def is_valid_password(password):
    """
    Проверяет, является ли входная строка корректным паролем.

    Пароль должен:
    - Содержать только латинские символы, цифры и специальные символы ^$%@#&*
    - Состоять из не менее чем восьми символов
    - Содержать по крайней мере два латинских символа в нижнем регистре
    - Содержать по крайней мере одну цифру
    - Содержать по крайней мере три различных специальных символа
    - Не содержать символы ,.!?

    Примеры:
    >>> is_valid_password("rtG&3FG#Tr^e")
    True
    >>> is_valid_password("a^A1@*@1Aa")
    True
    >>> is_valid_password("oF^a1D@y5%e6")
    True
    >>> is_valid_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
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

    pattern = r"^(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[^a-zA-Z\d])(?!.*[ ,.!?]).{8,}$"

    return bool(re.match(pattern, password))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
