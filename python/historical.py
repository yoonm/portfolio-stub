birth_dates = {"George Washington": 1729,
    "John Adams": 1734,
    "Andrew Jackson": 1802,
    "John F. Kennedy": 1920}

eighteenth_count = 0
nineteenth_count = 0
twentieth_count = 0

for person, year in birth_dates.items():
    if year >= 1800 and year < 1900:
        nineteenth_count += 1
    elif year >= 1900:
        twentieth_count += 1
    else:
        eighteenth_count += 1

print("There are " + str(eighteenth_count) + " 18th century birth(s), " +
    str(nineteenth_count) + " 19th century birth(s), " + "and " +
    str(twentieth_count) + " 20th century birth(s) in my collection.")
