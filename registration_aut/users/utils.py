def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': {
            'id': user.id,
            'email': user.email,
            'phone_number': str(user.phone_number)
        }
    }