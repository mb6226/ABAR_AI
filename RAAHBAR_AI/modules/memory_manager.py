class MemoryManager:
    def __init__(self):
        self.knowledge_base = {}

    def store(self, key, value):
        print(f"[MemoryManager] Storing {key} -> {value}")
        self.knowledge_base[key] = value

    def retrieve(self, key):
        value = self.knowledge_base.get(key, None)
        print(f"[MemoryManager] Retrieving {key} -> {value}")
        return value
