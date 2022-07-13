PLACES = {
 "Chico": 50,
 "Groucho": 70,
 "Harpo": 50,
 "Zeppo": 40
}

def calculate_tax(amount, place, hour):
    total = amount
    for h in range(0, 25):
        if h == hour:
            place_tax = (PLACES[place] * (hour * 100 / 24)) / 100
            total += (total * place_tax) / 100
            return total


