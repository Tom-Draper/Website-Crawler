class UrlStack:
    
    def __init__(self):
        self._maxSize = 1000
        self._stack = [None] * self._maxSize
        self._topOfStack = 0
        
    def getSize(self):
        return self._topOfStack
            
    def push(self, url):
        # If reach the top of the stack
        if self._topOfStack == self._maxSize - 1:
            # Copy top ten urls to bottom of stack
            self.stack[0:11] = self._stack[self._maxSize - 11:self._maxSize]
            # Move topOfStack to point above those ten
            self._topOfStack == 11
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
