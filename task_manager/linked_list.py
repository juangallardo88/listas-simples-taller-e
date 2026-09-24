class Node:
    def __init__(self, task_id, task_name, completed=False):
        self.task_id = task_id
        self.task_name = task_name
        self.completed = completed
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None
        self._task_counter = 1

    def is_empty(self):
        return self.head is None

    def add_task(self, task_name):
        clean_task_name = str(task_name).strip()
        if clean_task_name == "":
            raise ValueError("Task name cannot be empty.")

        new_node = Node(self._task_counter, clean_task_name)
        self._task_counter += 1

        if self.is_empty():
            self.head = new_node
            return new_node

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        return new_node

    def display_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append({
                "task_id": current.task_id,
                "task_name": current.task_name,
                "completed": current.completed,
            })
            current = current.next

        return tasks

    def complete_task(self, task_name):
        current = self.head

        while current is not None:
            if current.task_name.lower() == task_name.lower():
                current.completed = True
                return True
            current = current.next

        return False

    def delete_task(self, task_name):
        if self.is_empty():
            return False

        current = self.head

        if current.task_name.lower() == task_name.lower():
            self.head = current.next
            return True

        while current.next is not None:
            if current.next.task_name.lower() == task_name.lower():
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search_task(self, task_name):
        current = self.head

        while current is not None:
            if current.task_name.lower() == task_name.lower():
                return {
                    "task_id": current.task_id,
                    "task_name": current.task_name,
                    "completed": current.completed,
                }
            current = current.next

        return None
