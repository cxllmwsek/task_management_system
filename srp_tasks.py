# แก้ไข Class Task ให้รับ priority เพิ่ม
class Task:
    def __init__(self, task_id, description, due_date=None, completed=False, priority="low"):
        self.id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.priority = priority # เพิ่มส่วนนี้

    def mark_completed(self):
        self.completed = True
        print(f"Task {self.id} '{self.description}' marked as completed.")

    def __str__(self):
        status = "✓" if self.completed else " "
        due = f" (Due: {self.due_date})" if self.due_date else ""
        # เพิ่ม Priority ในการแสดงผล
        return f"[{status}] {self.id}. {self.description} [Priority: {self.priority}]{due}"

# แก้ไขฟังก์ชัน add_task ใน Class TaskManager ให้รับ priority เพิ่ม
    def add_task(self, description, due_date=None, priority="low"):
        task = Task(self.next_id, description, due_date, priority=priority)
        self.tasks.append(task)
        self.next_id += 1
        self.storage.save_tasks(self.tasks)
        print(f"Task '{description}' added with {priority} priority.")
        return task