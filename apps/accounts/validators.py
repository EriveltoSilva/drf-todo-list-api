from . import utils


def is_email_valid(email):
    return utils.is_email_valid(email)


def is_password_equal(password, confirmation_password):
    return password == confirmation_password
