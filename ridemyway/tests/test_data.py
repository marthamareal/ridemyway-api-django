valid_user_data = {
    "username": "mareal",
    "email": "marthamareal@gmail.com",
    "id_number": "CF2288909892883G",
    "phone_number": "+256-787-789-772",
    "password": "password123"
}

valid_user_data2 = {
    "username": "martha",
    "email": "martha@gmail.com",
    "id_number": "CF228890989283G4",
    "phone_number": "+256-787-789-000",
    "password": "password123"
}

invalid_user_data = {
    "username": "mar",  # short username
    "email": "marthamamail.com",  # invalid email address
    "id_number": "CF2288909892883G#,",  # Invalid id number
    "phone_number": "idjdddj",  # Invalid phone number
    "password": "pas"  # short password
}

missing_field_user_data = {
    "email": "marthamareal@gmail.com"
}

valid_update_user_data = {
    "username": "mareal2",
    "email": "marthamareal2@gmail.com",
    "phone_number": "+256-000-000-000",
    "image_url": "https://www.youtube.com/watch?v=CX11yw6YL1w&index=4&list=RDMM"
}

vehicle_data = {
    "number_plate": "UBE 490S",
    "category": "CR",
    "color": "Black",
    "make": "BMW",
    "model": "2018"
}

empty_vehicle_data = {}

vehicle_data_no_number_plate = {
    "number_plate": "",
    "category": "CR",
    "color": "Black",
    "make": "BMW",
    "model": "2018"
}

vehicle_data_invalid_plate = {
    "number_plate": "UBE490S",
    "category": "CR",
    "color": "Black",
    "make": "BMW",
    "model": "2018"
}


invalid_vehicle_category_choice = {
    "number_plate": "UBD 490S",
    "category": "BS",
    "color": "Black",
    "make": "BMW",
    "model": "2018"
}
