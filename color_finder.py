import colorgram
rgb_clrs = []
colours = colorgram.extract('OIP1.jpg', 9)
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_clrs = (r, g, b)
    rgb_clrs.append(new_clrs)

print(rgb_clrs)

[(105, 80, 120), (168, 152, 177), (166, 155, 182), (100, 82, 122), (51, 28, 66)]