class UrlStack:
    
    def __init__(self):
        self._stack = [None] * 1000
        self._topOfStack = 0
        
    def getSize(self):
        return self._topOfStack
            
    def push(self, url):
        self._stack[self._topOfStack] = url
        self._topOfStack += 1
        
    def pop(self):
        self._topOfStack -= 1
        return self._stack[self._topOfStack]
        
    def peek(self):
        return self._stack[self._topOfStack - 1]
