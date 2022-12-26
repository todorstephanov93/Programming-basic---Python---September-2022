w = float(input())
h = float(input())

w_places = w // 1.20
h_places = (h - 1) // 0.70

all_places = (w_places * h_places) - 3

print(all_places)
