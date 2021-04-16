"""Process credit card."""

import os

CREDIT_CARD = os.environ['CREDIT_CARD']


def charge_card(amt, card):
    """Charge credit card."""

    print("Charged {amt} to {card}".format(amt=amt, card=card))


charge_card(100, CREDIT_CARD)
