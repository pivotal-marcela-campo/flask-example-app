from .decorators import before_logging

@before_logging
class DatabaseDouble:
    def __init__(self):
        self.rows = []

    def add_todo(self, a_todo):
        print('** Add TODO:{} to List:{}'.format(a_todo, self.rows))
        self.rows.append(a_todo)

    def update_todo(self, todo_id, a_todo):
        print('** Update TODO:{} in List:{}'.format(todo_id, self.rows))
        old_todo = self.find(todo_id)
        old_todo['pending'] = a_todo['pending']

    def find(self, a_todo_id):
        print('** Find TODO:', a_todo_id)
        return self.rows[a_todo_id - 1]

    def all(self):
        print('*** All Rows:', self.rows)
        return self.rows
