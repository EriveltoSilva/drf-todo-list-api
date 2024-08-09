import re
import shortuuid


def generate_otp(length=12):
    """ generate a random string identifier with [length] caracters"""
    uuid_key = shortuuid.uuid()
    return uuid_key[:length]


def is_email_valid(email: str) -> bool:
    """
    Função para validar um endereço de email.
    Args:
      email: O endereço de email a ser validado.
    Returns:
      True se o email for válido, False caso contrário.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,7}$'     # Expressão regular para um email válido
    return re.match(regex, email)
