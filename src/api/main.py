
from scrapers import *

available_scrapers = []

for func in dir(__import__("scrapers")):

    if "get_bookings" in dir(getattr(__import__("scrapers"),func)):
        available_scrapers.append(getattr(__import__("scrapers"),func))
