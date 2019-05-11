
def jwt_response_token_handler(token, user, request):

    return {
        "user_id": user.id,
        "username": user.username,
        "token": token
    }
