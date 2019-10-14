# urlStack.py - stack data strcutre designed to store visited urls.
# Once stack becomes full, top of stack section is sliced off and moved to
# bottom and stack continues.

class UrlStack:
    
    def __init__(self):
        self._maxSize = 100
        self._stack = [None] * self._maxSize
        self._topOfStack = 0
        
    def getSize(self):
        return self._topOfStack
            
    def push(self, url):
        # If reach the top of the stack
        if self._topOfStack == self._maxSize:
            # Copy top nine urls to bottom of stack
            self._stack[0:10] = self._stack[self._maxSize - 10:self._maxSize]
            # Move topOfStack to point above those nine
            self._topOfStack = 10
            # Add next url
            self._stack[self._topOfStack] = url
        else:
            self._stack[self._topOfStack] = url
        self._topOfStack += 1
        
    def pop(self):
        if _topOfStack == 0:
            print("Stack underflow")
        else:
            self._topOfStack -= 1
        return self._stack[self._topOfStack]
        
    def peek(self):
        return self._stack[self._topOfStack - 1]
