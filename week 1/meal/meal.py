def main():
    #breakfast between 7:00 and 8:00
    #lunch between 12:00 and 13:00
    #dinner between 18:00 and 19:00

    time = input("What time is it? ")

    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    # converts time, a str in 24-hour format, to the corresponding number of hours as a float
    # EXAMPLE: Given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours)
    # CHALLENGE: add support for 12-hour times, allowing the user to input times in these formats too: #:## a.m. and ##:## a.m. / #:## p.m. and ##:## p.m.

    if time.endswith("p.m."):
        time = time.removesuffix("p.m.")
        hours, minutes = time.split(":")
        hours, minutes = float(hours), float(minutes)

        if hours != 12:
            hours = hours + 12

    elif time.endswith("a.m."):
        time = time.removesuffix("a.m.")
        hours, minutes = time.split(":")
        hours, minutes = float(hours), float(minutes)

        if hours == 12:
            hours = hours - 12

    else:
        hours, minutes = time.split(":")
        hours, minutes = float(hours), float(minutes)

    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
