from datetime import datetime, date
from typing import Optional, List

class History():
  def __init__(self):
    self.actions = []

  def add_action(self, action: str) -> None:
    self.actions.append(f"{action} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

  def get_history(self) -> list[str]:
    return self.actions

class Account():
  def __init__(self, balance: float = 0.0, agency: str = '0001', account_number: str = '', history: Optional[History] = None): 
    self.agency = agency
    self.account_number = account_number
    self.__balance = balance
    self.history = history or History()

  def get_balance(self) -> float:
    return self.__balance

  def deposit(self, amount: float) -> bool:
    if amount <= 0:
        print("Amount must be positive.")
        return False
    self.__balance += amount
    self.history.add_action(f"Deposit: R${amount:.2f}")
    return True

  def withdraw(self, amount: float) -> bool:
    if amount > self.__balance:
      return False
    self.__balance -= amount
    self.history.add_action(f"Withdraw: R${amount:.2f}")
    return True

  def get_transaction_history(self) -> list[str]:
    return self.history.get_history()

class CurrencyAccount(Account):
  def __init__(self, balance=0.0, agency='0001', account_number='', history: Optional[History] = None): 
    super().__init__(balance, agency, account_number, history)
    self.withdraw_count = 0
    self.daily_withdraw_limit = 3
    self.withdraw_limit_amount = 500.0
    self.last_withdraw_day = date.today() 

  
  def withdraw(self, amount: float) -> bool:
    
    today = date.today()
    if self.last_withdraw_day != today:
      self.withdraw_count = 0
      self.last_withdraw_day = today
      
    if self.withdraw_count >= self.daily_withdraw_limit:
      print("Daily withdraw limit reached.") 
      return False
      
    if amount > self.withdraw_limit_amount:
      print(f"Withdraw amount exceeds the limit of R${self.withdraw_limit_amount:.2f}.")
      return False
      
    if amount <= 0:
      print("Withdraw amount must be positive.")
      return False
      
    success = super().withdraw(amount) 
    
    if success:  
      self.withdraw_count += 1
      return True
    else:
      print("Insufficient funds")
      return False

class Client():
  def __init__(self, cpf: str, password: str, address: str, accounts: Optional[List[Account]] = None):
    self.__cpf = cpf
    self.__password = password
    self.__address = address
    self.__accounts = accounts or [] 
    self.is_logged_in = False
    self.name = "" # Será definido por Person

  def check_password(self, password: str) -> bool:
    return self.__password == password
  
  def login(self) -> None:
    self.is_logged_in = True

  def logout(self) -> None:
    self.is_logged_in = False

  def get_cpf(self) -> str:
    return self.__cpf

  def get_accounts(self) -> List[Account]:
    return self.__accounts
  
  def add_account(self, account: Account) -> None:
    self.__accounts.append(account)

class Person(Client):
  def __init__(self, name: str, cpf: str, birth_date: str, address: str, password: str, accounts: Optional[List[Account]] = None):
    super().__init__(cpf=cpf, password=password, address=address, accounts=accounts)
    self.name = name
    self.birth_date = birth_date

class BankSystem():
  
  def __init__(self, clients: Optional[List[Client]] = None):
    self.clients = clients or []
    self.current_client: Optional[Client] = None
    self.global_account_counter = 0

  def find_client_by_cpf(self, cpf: str) -> Optional[Client]:
    return next((client for client in self.clients if client.get_cpf() == cpf), None)

  def create_person(self, name: str, cpf: str, birth_date: str, address: str, password: str) -> Optional[Person]:
    
    if self.find_client_by_cpf(cpf):
      print("Error: A client with this CPF already exists.")
      return None
      
    new_person = Person(
      name=name, 
      cpf=cpf, 
      birth_date=birth_date, 
      address=address, 
      password=password, 
      accounts=[]
    )
    
    self.clients.append(new_person)
    print(f"Client {name} created successfully.")
    return new_person

  def create_account(self) -> Optional[Account]:
    if not self.current_client:
      print("Error: No client logged in.")
      return None
      
    self.global_account_counter += 1
    account_number = str(self.global_account_counter).zfill(4)
    
    new_account = CurrencyAccount(
      account_number=account_number,
      agency="0001"
    )
    
    self.current_client.add_account(new_account) 
    print(f"Account {account_number} created for {self.current_client.name}.")
    return new_account

  def authenticate_client(self, cpf: str, password: str) -> bool:
    client = self.find_client_by_cpf(cpf)
    
    if client and client.check_password(password): 
      self.current_client = client
      self.current_client.login()
      print(f"Welcome, {self.current_client.name}!")
      return True
      
    print("Invalid CPF or password.")
    return False

  def logout(self) -> None:
    if self.current_client:
      print(f"Goodbye, {self.current_client.name}.")
      self.current_client.logout()
      self.current_client = None
    else:
      print("No client is currently logged in.")

def select_account(client: Client) -> Optional[Account]:
  accounts = client.get_accounts()
  
  if not accounts:
    print("You have no accounts.")
    return None
    
  print("\nYour Accounts:")
  for i, acc in enumerate(accounts):
    print(f"  [{i}] Agency: {acc.agency} | Account: {acc.account_number} | Balance: R${acc.get_balance():.2f}")
    
  try:
    choice = int(input("Select account index: "))
    if 0 <= choice < len(accounts):
      return accounts[choice]
    else:
      print("Invalid index.")
      return None
  except ValueError:
    print("Invalid input.")
    return None

def __main__():
  main_input_logged_out = """
    Input a command:
    [q] Quit
    [c] Create User
    [lin] Login
  """
  
  main_input_logged_in = """
    Command:
    [d] Deposit
    [w] Withdraw
    [b] Balance
    [ca] Create Checking Account
    [lout] Logout
    [q] Quit
  """

  bank_system = BankSystem()
  
  while True:
    
    if bank_system.current_client is None:
        print(main_input_logged_out)
        command = input("Enter command: ").strip().lower()
    else:
        print(f"\nLogged in as: {bank_system.current_client.name}")
        print(main_input_logged_in)
        command = input("Enter command: ").strip().lower()

    
    if command == "q":
      print("Exiting the program...")
      break
      
    elif command == "c":
      name = input("Enter your name: ")
      cpf = input("Enter your CPF: ").strip().replace(".", "").replace("-", "")
      birth_date = input("Enter your birth date (YYYY-MM-DD): ")
      address = input("Enter your address: ")
      password = input("Enter your password: ")
      bank_system.create_person(name, cpf, birth_date, address, password)
      
    elif command == "lin":
      if bank_system.current_client:
          print("Already logged in.")
          continue
      cpf = input("Enter your CPF: ").strip().replace(".", "").replace("-", "")
      password = input("Enter your password: ")
      bank_system.authenticate_client(cpf, password)
      
    elif command == "lout":
      bank_system.logout()
      
    elif command == "ca":
      bank_system.create_account()

    elif command == "d":
      if bank_system.current_client is None:
        print("No client logged in. Please use [lin]")
        continue
        
      account = select_account(bank_system.current_client)
      if account:
        try:
          deposit_amount = float(input("Enter deposit amount: "))
          if account.deposit(deposit_amount):
            print(f"Deposit successful. New balance: R${account.get_balance():.2f}")
        except ValueError:
            print("Invalid amount.")

    elif command == "w":
      if bank_system.current_client is None:
        print("No client logged in. Please use [lin]")
        continue
        
      account = select_account(bank_system.current_client)
      if account:
        try:
          withdraw_amount = float(input("Enter withdraw amount: "))
          if account.withdraw(withdraw_amount):
            print(f"Withdraw successful. New balance: R${account.get_balance():.2f}")
        except ValueError:
            print("Invalid amount.")

    elif command == "b":
      if bank_system.current_client is None:
        print("No client logged in. Please use [lin]")
        continue
      
      account = select_account(bank_system.current_client)
      if account:
        print("\n=== Transaction History ===")
        print(f"-- Agency: {account.agency} Account: {account.account_number} --")
        history = account.get_transaction_history()
        if not history:
            print("No transactions yet.")
        else:
            for action in history:
                print(action)
        print(f"Current Balance: R${account.get_balance():.2f}")
        print("===========================\n")
    else:
      if bank_system.current_client is not None:
          print("Invalid command.")

if __name__ == "__main__":
    __main__()