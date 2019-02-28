import derivative
import integral as ig

test_point = 2.0

der_right = derivative.right(test_point)
print("Right   derivative at point x = 2: " + str(der_right) + " - should be 4.0")

der_central = derivative.central(at_point=test_point)
print("Central derivative at point x = 2: " + str(der_central) + " - should be 4.0")

area_rect_low = ig.rect_low(from_x=0, to_x=2)
print("Area using rect_low: " + str(area_rect_low))

area_rect_high = ig.rect_high(from_x=0, to_x=2)
print("Area using rect_high: " + str(area_rect_high))

area_rect_avg = ig.rect_avg(from_x=0, to_x=2)
print("Area using rect_avg: " + str(area_rect_avg))