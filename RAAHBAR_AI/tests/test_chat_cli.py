"""
Test script for 3-user chat session with RAAHBAR AI
"""
from modules.memory_manager import MemoryManager
from modules.chat_manager import ChatManager

USERS = ["user1", "user2", "copilot"]
MESSAGES = [
    ("user1", "سلام!"),
    ("user2", "درود بر همه!"),
    ("copilot", "آیا سیستم آنلاین است؟")
]

def test_three_user_chat():
    memory = MemoryManager()
    chat = ChatManager(memory)
    for user, msg in MESSAGES:
        chat.send_message(user, msg)
        # Simulate RAAHBAR AI response
        response = f"[RAAHBAR] پیام شما '{msg}' دریافت شد."
        chat.send_message("raahbar", response)
    history = chat.get_history()
    assert len(history) == 6  # 3 user + 3 raahbar
    assert history[0][0] == "user1"
    assert history[1][0] == "raahbar"
    assert history[2][0] == "user2"
    assert history[3][0] == "raahbar"
    assert history[4][0] == "copilot"
    assert history[5][0] == "raahbar"
    print("3-user chat test passed. History:")
    for u, m in history:
        print(f"{u}: {m}")

if __name__ == "__main__":
    test_three_user_chat()
