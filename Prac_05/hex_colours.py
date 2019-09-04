hex_colours = {"AliceBlue": '#f0f8ff', "Beige": '#f5f5dc', "Brown": '#a52a2a', 'Black': '#000000', 'Coral': '#ff7f50'}
hex_colour = input('Please input either AliceBlue, Beige, Brown, Black or Coral: ')
hex_colour = hex_colour.capitalize()
while hex_colour != "":
    if hex_colour in hex_colours:
        print(hex_colour, 'is', hex_colours[hex_colour])
    else:
        print("Invalid Choice")
    hex_colour = input('Please input either AliceBlue, Beige, Brown, Black or Coral')
    hex_colour = hex_colour.capitalize()