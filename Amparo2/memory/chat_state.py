class ChatState:
    def __init__(self, history=None):
        self.history = history or []

    def add_message(self, user_input, response):
        self.history.append({"user": user_input, "amparo": response})
