"""
Test Cases Table (Range and Boundary Validation)

| Input (Rating) | Expected Result      | Actual Result        |
|----------------|----------------------|----------------------|
| -1             | Number out of range  | Number out of range  |
| 0              | Failed               | Failed               |
| 9.99           | Failed               | Failed               |
| 10             | Approved             | Approved             |
| 13.99          | Approved             | Approved             |
| 14             | Good                 | Good                 |
| 16.99          | Good                 | Good                 |
| 17             | Excellent            | Excellent            |
| 20             | Excellent            | Excellent            |
| 20.01          | Number out of range  | Number out of range  |
"""

rating = float(input('enter your rating [0-20]: '))
if rating < 0 or rating > 20:
    print('Number out of range')
elif rating < 10:
    print('Failed')
elif rating < 14:
    print('Approved')
elif rating < 17:
    print('Good')
else:
    print('Excellent')
