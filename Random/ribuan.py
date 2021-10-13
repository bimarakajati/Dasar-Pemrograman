x = int(input('Input number: ')) # dalam ribuan
def place_value(number):
    return ("{:,}".format(number))
print(place_value(x))