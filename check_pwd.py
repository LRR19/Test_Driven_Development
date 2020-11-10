def check_pwd(pwd):

    symbols = '~`!@#$%^&*()_+-='

    if len(pwd) < 8 or len(pwd) > 20:
        return False

    if not any(i.islower() for i in pwd):
        return False

    if not any(i.isupper() for i in pwd):
        return False

    if not any(i.isdigit() for i in pwd):
        return False

    if not any(i in symbols for i in pwd):
        return False

    return pwd
