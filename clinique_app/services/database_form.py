from .. import models


def upformForward(**kwargs):
    try:
        data = models.Appointment(kwargs)
        data.save()
        return True
    except Exception:
        return False


def priceformForward(**kwargs):
    try:
        data = models.GetPrice(kwargs)
        data.save()
        return True
    except Exception:
        return False