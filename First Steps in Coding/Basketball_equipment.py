yearly_fee = int(input())

sneakers = yearly_fee - (yearly_fee * (40 / 100))
outfit = sneakers - (sneakers * (20/100))
ball = outfit / 4
accessories = ball / 5

total = yearly_fee + sneakers + outfit + ball + accessories

print(total)
