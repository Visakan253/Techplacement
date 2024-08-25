import hashlib

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, username, password):
        if username in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[username] = self.hash_password(password)
            print(f"Account created for {username}.")

    def delete_account(self, username):
        if username in self.accounts:
            del self.accounts[username]
            print(f"Account {username} deleted.")
        else:
            print("Account does not exist.")

    def update_account(self, username, new_password):
        if username in self.accounts:
            self.accounts[username] = self.hash_password(new_password)
            print(f"Password for {username} updated.")
        else:
            print("Account does not exist.")

    def get_account(self, username):
        return self.accounts.get(username, None)
