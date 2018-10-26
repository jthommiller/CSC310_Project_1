class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data.pop()               # remove last item from list

"""This funciton will take an equation in post-fix notation and solves it"""
def postFix(exp):
    Stack = ArrayStack()
    """This loop iterates through the string and determines if each character is a number or an operaiton"""
    for i in exp:
        if i.isdigit():            # Checks if each character is a digit or not
            Stack.push(int(i))     # If the character is a digit, pushed into the stack
        else:
            exp1=Stack.pop()       # Pops the stack
            exp2=Stack.pop()       # Pops the stack
            if i == '+':           # Performs elementary operations
                value=exp2+exp1
            elif i == '-':
                value=exp2-exp1
            elif i == '/':
                value =exp2/exp1
            else:
                value=exp2*exp1
            Stack.push(value)       # Pushes the answer into the stack
    return Stack.pop()              # Returns the answer to the expression

reset=True
cont = ""
while reset:
    print()
    expression = input("Enter An Expression: ")         #gets user input in post-fix notation
    print(expression+" = "+str(postFix(expression)))    #prints the answer
    print()
    cont = input("Continue?: ")                          #allows the user to continue by typing yes or no
    if cont[0].lower() == 'n':
            reset = False