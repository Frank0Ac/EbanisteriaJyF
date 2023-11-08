class User:
    users = {
        'frk': {
            'password': 'frkfrkfrk',
            'email': 'frk@example.com',
            'notes': [],
            'payments': []
        },
        'jz': {
            'password': 'jzjzjz',
            'email': 'jz@example.com',
            'notes': [],
            'payments': []
        }
    }

    @classmethod
    def get(cls, username):
        user_data = cls.users.get(username)
        if user_data:
            return cls(username, user_data['password'], user_data['email'])

    @classmethod
    def create(cls, user):
        cls.users[user.username] = {
            'password': user.password,
            'email': user.email,
            'notes': [],
            'payments': []
        }

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.notes = []
        self.payments = []

    def check_password(self, password):
        return self.password == password

    def add_note(self, note):
        self.notes.append(note)

    def add_payment(self, payment):
        self.payments.append(payment)
