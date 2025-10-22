from datetime import datetime, date

main_input = """
Input a command:
[q] Quit
[d] Deposit
[w] Withdraw
[b] Balance
[c] Create User
[lin] Login
[lout] Logout
[ca] Create Currency Account
"""
ALL_USERS = {}
CURRENT_USER = None
MAX_LIMIT = 500.0
MAX_DAILY_WITHDRAWS = 3
USER_LOGGED_IN = False


def deposit_function(user, value):
  if user is None:
    print("No user logged in.")
    return
  try:
    amount = float(value)
  except ValueError:
    print("Valor inválido.")
    return

  if amount <= 0:
    print("Deposit amount must be positive.")
    return

  user["conta"]["value"] += amount
  user["conta"]["actions"].append(
    f"Deposit: R${amount:.2f} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
  )

def withdraw_function(user, value):
  if user is None:
    print("No user logged in.")
    return
  try:
    amount = float(value)
  except ValueError:
    print("Valor inválido.")
    return

  if user["conta"]["withdraw_count"] >= MAX_DAILY_WITHDRAWS:
    print("Daily withdraw limit reached.")
    return
  if amount <= 0:
    print("Withdraw amount must be positive.")
    return
  if amount > MAX_LIMIT:
    print("Withdraw amount exceeds the maximum limit.")
    return
  if amount > user["conta"]["value"]:
    print("Insufficient balance.")
    return

  user["conta"]["value"] -= amount
  user["conta"]["withdraw_count"] += 1
  user["conta"]["last_withdraw_day"] = date.today()
  user["conta"]["actions"].append(
    f"Withdraw: R${amount:.2f} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
  )


def balance_function(user=None):
  if user is None:
    print("No user logged in.")
    return
  
  print("\n=== Transaction History ===")
  for action in user["conta"]["actions"]:
    print(action)
  print(f"Current Balance: R${user['conta']['value']:.2f}")


def verify_day(user=None):
  current_day = date.today()
  if user["conta"]["last_withdraw_day"] is None:
    user["conta"]["last_withdraw_day"] = current_day
  elif user["conta"]["last_withdraw_day"] != current_day:
    user["conta"]["withdraw_count"] = 0
    user["conta"]["last_withdraw_day"] = current_day

def create_user():
  cpf = input("Enter your CPF: ")
  if cpf in ALL_USERS:
    print("User already exists.")
    return None
  name = input("Enter your name: ")
  password = input("Enter your password: ")
  address = input("Enter your address: ")
  birth_date = input("Enter your birth date (YYYY-MM-DD): ")
  cpf = cpf.strip().replace(".", "").replace("-", "")
  ALL_USERS[cpf] = {
    "nome": name,
    "cpf": cpf,
    "senha": password,
    "endereco": address,
    "data_nascimento": birth_date,
    "conta": {
      "value": 0.0,
      "last_withdraw_day": None,
      "withdraw_count": 0,
      "actions": []
    }
  }
  USER_LOGGED_IN = True
  print("User created successfully.")

def login():
  if USER_LOGGED_IN:
    print("A user is already logged in.")
    return
  if not ALL_USERS:
    print("No users available. Please create a user first.")
    return
  cpf = input("Enter your CPF: ").strip().replace(".", "").replace("-", "")
  password = input("Enter your password: ")
  user = ALL_USERS.get(cpf)
  if user and user["senha"] == password:
    USER_LOGGED_IN = user
    print("Login successful.")
  else:
    print("Invalid CPF or password.")

def logout():
  USER_LOGGED_IN = False

if __name__ == "__main__":
  while True:
    command = input(main_input).strip().lower()
    if USER_LOGGED_IN is not None:
      verify_day()

    if command == "q":
      print("Exiting the program...")
      break
    elif command == "d":
      value = input("Insert deposit amount: ")
      deposit_function(value)
    elif command == "w":
      value = input("Insert withdraw amount: ")
      withdraw_function(value)
    elif command == "b":
      balance_function()
    elif command == "c":
      create_user()
    elif command == "lin":
      login()
    elif command == "lout":
      logout()
    else:
      print("Invalid command. Please try again.")
