
def validate_email(email):
    
    # Rule 1: must be exactly 8 characters
    if len(email) != 8:
        return False

    # Rule 2: must contain '@'
    if '@' not in email:
        return False

    # Rule 3: must not start or end with '@'
    if email[0] == '@' or email[-1] == '@':
        return False

    return True
