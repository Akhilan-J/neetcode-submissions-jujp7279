class Singleton:
    something = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls.something is None:
            cls.something = object.__new__(cls)
        
        return cls.something 
    def getValue(self) -> str:
        return self.val
    def setValue(self, value: str):
        self.val = value