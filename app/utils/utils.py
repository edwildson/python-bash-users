import re


def check_if_filename_is_allowed(filename: str) -> bool:
    """
    This function checks if the filename is allowed.

    :param filename: Name of the file.
    :return: True if the filename is allowed, False otherwise.
    """
    return all(c.isalnum() or c in '-_' for c in filename)


def handle_users_array_to_dict(
    users: list,
    offset: int,
    limit: int,
    username: str = '',
) -> list:
    """
    This function handles the users array to a list of dictionaries.

    :param users: List of users.
    :return: List of dictionaries.
    """
    users_dict = []
    for user in users:
        user_dict = match_user_string(user, username)
        if user_dict:
            users_dict.append(user_dict)
    return users_dict[offset:offset + limit] if offset + limit < len(users_dict) else users_dict[offset:]  # noqa


def match_user_string(user_string: str, username: str = '') -> dict:
    """
    This function matches a user string.

    :param user_string: User string.
    :return: User dictionary.
    """
    pattern = r'(?P<username>[._\w\+\-]+@[a-zA-Z0-9\.\-]+)\s(?P<folder>\w+)\s(?P<numberMessages>\d+)\ssize\s(?P<size>\d+)'  # noqa

    match = re.search(pattern, user_string)

    if match and (
        not username or username in match.group("username")
    ):
        return {
            "username": match.group("username"),
            "folder": match.group("folder"),
            "numberMessages": int(match.group("numberMessages")),
            "size": int(match.group("size"))
        }
    return {}
