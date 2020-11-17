from .. import models


def upformForward(**kwargs):

    data = models.Appointment(kwargs)
    data.save()
    return True



def priceformForward(**kwargs):

    print('DATA IN FUNC')
    data = models.GetPrice(kwargs)
    print('DATA IN MODEL')
    data.save()
    print('DATA IS SAVED')
    return True
