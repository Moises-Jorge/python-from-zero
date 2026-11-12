rating = float(input('enter your rating: '))
if rating < 10:
    print('Failed')
elif rating < 14:
    print('Approved')
elif rating < 17:
    print('Good')
elif rating <= 20:
    print('Excellent')
else:
    print('Number out of range')