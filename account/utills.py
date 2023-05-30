# import firebase_admin
# from firebase_admin import auth
#
#
# def send_sms_code(phone_number):
#     # Создание пользовательской эмитации (mock user)
#     user = auth.create_user(phone_number=phone_number)
#
#     # Отправка SMS сообщения
#     verification_code = auth.generate_phone_number_verification_code(user.uid)
#
#     return verification_code


import firebase_admin
from firebase_admin import auth


def send_sms_code(phone_number):
    # Создание пользовательской эмитации (mock user)
    user = auth.create_user(phone_number=phone_number)

    # Отправка SMS сообщения
    verification_code = auth.generate_phone_number_verification_code(user.uid)
    if verification_code is None:
        return None
    else:
        return verification_code


print(send_sms_code("+996771478853"))
