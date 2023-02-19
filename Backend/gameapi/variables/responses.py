def login_success():
    return {'success': 'Login successful'}

def login_error():
    return {'error': 'Invalid credentials'}

def login_failed():
    return {'error': 'Login failed'}

def logout_success():
    return {'success': 'Logout sucessful'}

def not_allowed():
    return {'error': 'Method not allowed'}

def user_not_found():
    return {'error': 'User not found'}

def user_deleted():
    return {'success': 'User deleted'}