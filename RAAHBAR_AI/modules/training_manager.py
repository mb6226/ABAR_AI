class TrainingManager:
    def __init__(self):
        self.training_jobs = []

    def start_training(self, model_name):
        print(f"[TrainingManager] Starting training for {model_name}")
        self.training_jobs.append(model_name)

    def get_training_status(self, model_name):
        status = "completed" if model_name in self.training_jobs else "not started"
        print(f"[TrainingManager] Status for {model_name}: {status}")
        return status
