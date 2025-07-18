"""
RAAHBAR AI - Central Orchestrator for ABAR_AI
Author: <Your Name>
Date: 2025-07-18
"""


from modules.task_manager import TaskManager
from modules.health_monitor import HealthMonitor
from modules.decision_engine import DecisionEngine

from modules.memory_manager import MemoryManager
from modules.training_manager import TrainingManager
from modules.chat_manager import ChatManager


class RaahbarAI:
    def __init__(self):
        self.task_manager = TaskManager()
        self.health_monitor = HealthMonitor()
        self.decision_engine = DecisionEngine()
        self.memory_manager = MemoryManager()
        self.training_manager = TrainingManager()
        self.chat_manager = ChatManager(self.memory_manager)

    def run(self):
        print("[RAAHBAR AI] Starting Orchestrator...")
        self.health_monitor.start_monitoring()
        self.task_manager.schedule_tasks()
        self.decision_engine.run_decision_loop()
        # Example memory usage
        self.memory_manager.store("startup_time", "2025-07-18")
        self.memory_manager.retrieve("startup_time")
        # Example training usage
        self.training_manager.start_training("example_model")
        self.training_manager.get_training_status("example_model")
        # Example chat usage
        self.chat_manager.send_message("user1", "سلام راهبر!")
        self.chat_manager.send_message("admin", "وضعیت سیستم؟")
        last = self.chat_manager.get_last_message("admin")
        print(f"[ChatManager] آخرین پیام admin: {last}")
        print("[RAAHBAR AI] Orchestration running.")

if __name__ == "__main__":
    raahbar = RaahbarAI()
    raahbar.run()
