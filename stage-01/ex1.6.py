"""
Step-by-Step Debugging (Python Execution Order)

1. First Error (Before execution - Syntax Phase):
   - Exact Message: SyntaxError: expected ':' (on the line 'if average >= 10')
   - Reason: Python parses and checks the grammar of the entire file before running it.
     Because the colon (:) is missing, the program aborts immediately before even asking
     for the inputs, hiding all subsequent runtime errors.

2. Second Error (During execution - Type Error):
   - Exact Message: TypeError: unsupported operand type(s) for /: 'str' and 'int'
   - Reason: After fixing the colon, the program runs, asks for the grades, and crashes
     on line 3. Since input() always returns a string (str), Python cannot divide the
     string 'grade2' by the integer 2.

3. Third Error (During execution - Logic Error):
   - Wrong Behavior: No Python error message is raised, but the average is calculated
     incorrectly (e.g., for grades 8 and 8, it outputs 12.0 and approves the student).
   - Reason: After converting the inputs to float(), the expression 'grade1 + grade2 / 2'
     divides only the second grade by 2 due to operator precedence. Parentheses are
     missing around '(grade1 + grade2) / 2'.
"""

# corrected code:
grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))
average = (grade1 + grade2) / 2
if average >= 10:
    print("Approved")
else:
    print("Failed")
