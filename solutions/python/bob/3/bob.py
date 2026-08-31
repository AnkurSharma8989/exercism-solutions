"""
    Determine Bob's response based on the type of statement given.
"""
def response(hey_bob):
    """
    Determine how Bob responds to a given statement.

    :param hey_bob: The statement or question given to Bob.
    :return: Bob's appropriate response.
    """
    satement_nospace = hey_bob.strip()
    if satement_nospace.endswith("?") and satement_nospace.isupper():
        return "Calm down, I know what I'm doing!"
    if satement_nospace.endswith("?"):
        return "Sure."
    if satement_nospace.isupper():
        return "Whoa, chill out!"
    if satement_nospace.strip() == "":
        return "Fine. Be that way!"
    return "Whatever."