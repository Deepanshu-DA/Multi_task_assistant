import threading

class TaskManager:
    def __init__(self):
        self.active_tasks = []

    def run_task(self, func, *args, **kwargs):
        thread = threading.Thread(target=self._task_wrapper, args=(func, args, kwargs))
        thread.daemon = True
        thread.start()
        self.active_tasks.append(thread)

    def _task_wrapper(self, func, args, kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Task error: {e}")

    def wait_for_all(self):
        for task in self.active_tasks:
            task.join()

    def get_status(self):
        return [(i+1, t.is_alive()) for i, t in enumerate(self.active_tasks) if t]

    def clear_finished(self):
        self.active_tasks = [t for t in self.active_tasks if t.is_alive()]

    def stop_all(self):
        print("Note: Force stopping threads isn't safe in Python. Consider using stop flags or task-specific cancel logic.")
