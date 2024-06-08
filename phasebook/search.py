from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(u_input, id, name, age, occupation):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    result = []
    if u_input is not None:
        u_input = u_input.lower()

    if u_input != id.lower() and u_input != name.lower() and u_input != occupation:
        print("No user found!")

    # Append the found query and returns the results
    for user in USERS:
        if user.id.lower() == id:
            result.append(user)
        elif user.name.lower() == name:
            result.append(user)
        elif user.occupation.lower() == occupation:
            result.append(user)
        elif user.age == age:
            result.append(user)

        return result

    # Add all users that matches the query
    for user in USERS:
        if (name and name in user.name) or \
                (age is not None and (user.age >= age - 1 and user.age <= age + 1)) or \
                (occupation and occupation in user.occupation):
                result.append(user)

    # If there is no query, it returns all users
    if not id and not name and age is None and not occupation:
        return USERS
