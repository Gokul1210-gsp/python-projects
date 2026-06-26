import calendar

def glass(text):
    lines = text.splitlines()
    w = max(len(l) for l in lines)
    print("┌" + "-" * (w+2) + "┐")
    for l in lines:
        print("| " + l.ljust(w) + " |")
    print("└" + "-" * (w + 2) + "┘")

cal = int(input("Year of Calendar: "))

for m in range(1,13):
    glass(calendar.month(cal,m))

