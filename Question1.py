class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned

"""The function that sorts a list using radix sorting with two queue data structures"""
def radix_sort(post_sort, list_length):
    main_queue = ArrayQueue()                                       # The Main queue
    bin_queue = ArrayQueue()                                        # Sorting Queue
    position = len(str(max(post_sort)))                             # Determines how many times the main queue will need to be sorted
    for i in range(list_length):
        item = str(post_sort.pop(0))
        if len(item) < position:
            item = ("0"*(position-len(item))) + item
        main_queue.enqueue(item)                        # enqueues the list into the main Queue
    bin_count = 0                                                   # keeps track of how many numbers go into the bin queue
    main_count = 0                                                  # keeps track of how many numbers should be in the main queue
    index = 0                                                       # used to sort each digit
    """Loop will run for each digit that needs to be processed and sorted"""
    while position > 0:
        """this inner loop will repeatedly dequeue and either enqueue that element into the bin in order or back into
            the main queue to be processed later until the main queue is empty"""
        while not main_queue.is_empty():
            element = main_queue.dequeue()
            number = int(element[position-1])                       # derives the number at each position
            if number == index:                                     # decides if the number should be organized into the bin queue
                bin_queue.enqueue(element)
                bin_count += 1
                main_count += 1
            else:                                                   # puts the element back into the main queue
                main_queue.enqueue(element)
                main_count += 1
            if main_count == list_length:                           # keeps track of when the index needs to increase
                index += 1
                list_length = list_length-bin_count
                bin_count=0
                main_count=0

        position -= 1
        """Once the main queue is empty, the bin is put back into the queue in the newer position sorted order"""
        while not bin_queue.is_empty():
            main_queue.enqueue(bin_queue.dequeue())
            list_length += 1
        index = 0
    """appends the queue back into the list in the now sorted order"""
    while not main_queue.is_empty():
        post_sort.append(int(main_queue.dequeue()))
    return post_sort


""" Allows the user to enter a list of numbers and saves them into a list that can be sorted"""
reset = True
while reset: # Allows the user to sort multiple lists in a row
    pre_sort = [int(n) for n in input("Enter numbers: ").split(", ")]
    print("Unsorted List: "+str(pre_sort))
    print()
    print("Sorted List: "+str(radix_sort(pre_sort, len(pre_sort))))                        # Prints the now sorted list
    print()
    cont = input("Continue?: ")
    if cont[0].lower() == "n":
        reset = False
