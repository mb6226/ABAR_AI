class ChatManager:
    def __init__(self, memory_manager):
        self.memory_manager = memory_manager
        self.chat_history = []

    def send_message(self, user, message):
        print(f"[ChatManager] {user}: {message}")
        self.chat_history.append((user, message))
        self.memory_manager.store(f"last_message_{user}", message)

    def get_last_message(self, user):
        return self.memory_manager.retrieve(f"last_message_{user}")

    def get_history(self):
        return self.chat_history
