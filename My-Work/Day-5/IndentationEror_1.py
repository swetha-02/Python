try:
def compare(a):
if a>7:
print("a is greater than 7")
except IndentationError:
    print("IndentationError: Indentation block is missing")
finally:
    print("Cleaned up the resources")
