def inputConverter(variable) -> int or None:
    """
    function converting inserted string into int and returns it if possible, otherwise returns None instead
    :param variable:
    :return: Int or None
    """
    try:
        var = int(variable)
        return var
    except ValueError:
        return None
