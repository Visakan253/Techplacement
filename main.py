import getpass
import json

class AccountManager:
    def __init__(self):
        # Load existing accounts from a file if it exists
        self.accounts = self.load_accounts()

    def save_accounts(self):
        with open('accounts.json', 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def load_accounts(self):
        try:
            with open('accounts.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def create_account(self, account_name, username, email, password):
        if account_name in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_name] = {'username': username, 'email': email, 'password': password}
            self.save_accounts()
            print(f"Credentials for {account_name} saved securely.")

    def delete_account(self, account_name):
        if account_name in self.accounts:
            del self.accounts[account_name]
            self.save_accounts()
            print(f"Credentials for {account_name} deleted.")
        else:
            print("Account does not exist.")

    def update_account(self, account_name, new_username=None, new_email=None, new_password=None):
        if account_name in self.accounts:
            if new_username:
                self.accounts[account_name]['username'] = new_username
            if new_email:
                self.accounts[account_name]['email'] = new_email
            if new_password:
                if self.confirm_password(new_password):
                    self.accounts[account_name]['password'] = new_password
                    self.save_accounts()
                    print(f"Password updated for {account_name}.")
                else:
                    print("Passwords do not match. Password update canceled.")
            else:
                print(f"Account details updated for {account_name}.")
        else:
            print("Account does not exist.")

    def confirm_password(self, password):
        confirm_password = getpass.getpass("Confirm the new password: ").strip()
        return password == confirm_password

    def get_account(self, account_name):
        return self.accounts.get(account_name, None)


def main():
    account_manager = AccountManager()

    while True:
        print("\n--- Secure Password Manager ---")
        print("1. Store a new account")
        print("2. Retrieve an account")
        print("3. Delete an account")
        print("4. Update account details")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            account_name = input("Enter the account name (e.g., Gmail, Facebook): ").strip()
            username = input("Enter the username: ").strip()
            email = input("Enter the email address: ").strip()
            password = getpass.getpass("Enter the password: ").strip()
            account_manager.create_account(account_name, username, email, password)

        elif choice == "2":
            account_name = input("Enter the account name to retrieve: ").strip()
            account = account_manager.get_account(account_name)
            if account:
                print(f"\nAccount Name: {account_name}")
                print(f"Username: {account['username']}")
                print(f"Email: {account['email']}")
                print(f"Password: {account['password']}")
            else:
                print("Account does not exist.")

        elif choice == "3":
            account_name = input("Enter the account name to delete: ").strip()
            account_manager.delete_account(account_name)

        elif choice == "4":
            account_name = input("Enter the account name to update: ").strip()
            new_username = input("Enter the new username (or press Enter to skip): ").strip()
            new_email = input("Enter the new email address (or press Enter to skip): ").strip()
            new_password = getpass.getpass("Enter the new password (or press Enter to skip): ").strip()
            account_manager.update_account(account_name, new_username or None, new_email or None, new_password or None)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()    
