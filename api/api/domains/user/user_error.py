class UserNotFoundError(Exception):

    message = "This user does not exitst."

    def __str__(self) -> str:
        return UserNotFoundError.message
