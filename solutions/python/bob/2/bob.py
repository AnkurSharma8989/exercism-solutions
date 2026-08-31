"""
    Determine Bob's response based on the type of statement given.
"""
def response(hey_bob):
    """
    Determine how Bob responds to a given statement.

    :param hey_bob: The statement or question given to Bob.
    :return: Bob's appropriate response.
    """
    if (hey_bob.strip()).endswith("?") and (hey_bob.strip())[:-1].isupper():
        return "Calm down, I know what I'm doing!"
    if (hey_bob.strip()).endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    return "Whatever."