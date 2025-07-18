"""
Simple Multi-User CLI Chat for RAAHBAR AI
Roles: user1, user2, copilot, raahbar
"""
from modules.memory_manager import MemoryManager
from modules.chat_manager import ChatManager

USERS = ["user1", "user2", "copilot", "raahbar"]

class SimpleChatCLI:
    def __init__(self):
        self.memory = MemoryManager()
        self.chat = ChatManager(self.memory)

    def start(self):
        print("\n--- Multi-User Chat (type 'exit' to quit) ---")
        while True:
            user = input(f"Choose user {USERS}: ").strip()
            if user not in USERS:
                print("Invalid user. Try again.")
                continue
            msg = input(f"{user}> ").strip()
            if msg.lower() == "exit":
                break
            self.chat.send_message(user, msg)
            # Simulate RAAHBAR AI response
            if user != "raahbar":
                response = f"[RAAHBAR] پیام شما '{msg}' دریافت شد."
                self.chat.send_message("raahbar", response)
            print("\nChat History:")
            for u, m in self.chat.get_history():
                print(f"{u}: {m}")
            print("-")

if __name__ == "__main__":
    SimpleChatCLI().start()
