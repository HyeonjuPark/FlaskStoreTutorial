import datetime
class Employee:
    def __init__(self, name, role, wage):
        self.name = name
        self.role = role
        self.wage = wage
        self.started_at = datetime.datetime.now().strftime('%Y.%m.%d')

    def __repr__(self):
        return '<Employee name=%s role=%s wage=%s started_at=%s>' \
            % (self.name, self.role, self.wage, self.started_at)