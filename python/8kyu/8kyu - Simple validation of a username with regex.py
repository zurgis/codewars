# Write a simple regex to validate a username. Allowed characters are:

# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

# Best Practices
import re
def validate_usr(username):
    return re.match('^[a-z0-9_]{4,16}$', username) != None

# My asnwer
def validate_usr(username):
    import re
    '''
    pattern = r'([a-z_0-9]*)'
    if len(username) > 3 and len(username) < 17:
        return True if re.fullmatch(pattern, username) else False
    return False
    '''
    return (re.fullmatch(r'([a-z_0-9]*)', username) and (len(username) > 3 and len(username) < 17)) or False