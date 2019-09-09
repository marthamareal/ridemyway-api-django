""" Regular expressions for validating input fields"""

patterns = {
    'email_pattern': '^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$',
    'username_pattern': '^[A-Za-z0-9]{5,}$',
    'id_number_pattern': '^[A-Za-z0-9]{8,49}$',
    'phone_number_pattern': '^\+[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{3}',
    'password_pattern': '[0-9A-Za-z|@,.#-]{8,}',
    'number_plate_pattern': '[A-Z]{3} [0-9]{3}[A-Z]'
}
