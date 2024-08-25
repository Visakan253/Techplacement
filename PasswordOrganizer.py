class PasswordOrganizer:
    def __init__(self):
        self.passwords = {}

    def add_password(self, account, password):
        if account in self.passwords:
            print("Password for this account already exists.")
        else:
            self.passwords[account] = password
            print(f"Password added for {account}.")

    def delete_password(self, account):
        if account in self.passwords:
            del self.passwords[account]
            print(f"Password for {account} deleted.")
        else:
            print("Password for this account does not exist.")

    def update_password(self, account, new_password):
        if account in self.passwords:
            self.passwords[account] = new_password
            print(f"Password for {account} updated.")
        else:
            print("Password for this account does not exist.")

    def get_password(self, account):
        return self.passwords.get(account, None)
