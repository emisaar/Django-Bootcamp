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

def not_found():
    return {'error': 'Resource was not found.'}

def resource_deleted():
    return {'success': 'User deleted'}