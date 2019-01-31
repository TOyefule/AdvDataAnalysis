import sys

print('Name is :', sys.argv[1])
print('Pay Rate :', sys.argv[2])
print('Hours :', sys.argv[3])
name = sys.argv[1]
payrate = int(sys.argv[2])
hours = int(sys.argv[3])
if hours <= 40:
	pay = payrate * hours
else:
	othours = hours - 40
	pay = 40 * payrate + othours * 1.5 * payrate
print("Pay is ", pay)


