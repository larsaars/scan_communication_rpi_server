from datetime import datetime


def stamp():
    return datetime.now().strftime('%m%d%Y_%H%M%S')
