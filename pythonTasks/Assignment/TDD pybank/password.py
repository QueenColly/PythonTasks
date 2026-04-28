def validate_email(email):
    
    if len(email) < 8:
        return "Email is too short"

    if email[0] == '@' or email[-1] == '@' :
        return "Email is wrong"

    if '@' not in email:
        return "Email is wrong"

    return "Email is valid"
    
    

