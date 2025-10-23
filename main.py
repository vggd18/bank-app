from datetime import datetime, date

main_input = """
Input a command:
[q] Quit
[d] Deposit
[w] Withdraw
[b] Balance
[c] Create User
[ca] Create Checking Account
[lin] Login
[lout] Logout
"""
ALL_USERS = {}
CURRENT_USER = None
MAX_LIMIT = 500.0
MAX_DAILY_WITHDRAWS = 3
GLOBAL_ACCOUNT_COUNTER = 0


def deposit_function():
  target_account = None
  account_number_input = input("Select account: ")

  for acc in CURRENT_USER["checking_account"]:
    if str(acc['account_number']) == account_number_input:
      target_account = acc
      break

  if target_account is None:
    print("Account not found.")
    return

  value = input("Insert deposit amount: ")
  try:
    amount = float(value)
  except ValueError:
    print("Invalid Value.")
    return

  if amount <= 0:
    print("Deposit amount must be positive.")
    return

  target_account["value"] += amount
  target_account["actions"].append(
    f"Deposit: R${amount:.2f} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
  )

def withdraw_function():
  target_account = None
  account_number_input = input("Select account: ")

  for acc in CURRENT_USER["checking_account"]:
    if str(acc['account_number']) == account_number_input:
      target_account = acc
      break

  if target_account is None:
    print("Account not found.")
    return

  value = input("Insert withdraw amount: ")
  try:
    amount = float(value)
  except ValueError:
    print("Invalid Value.")
    return

  if target_account["withdraw_count"] >= MAX_DAILY_WITHDRAWS:
    print("Daily withdraw limit reached.")
    return
  if amount <= 0:
    print("Withdraw amount must be positive.")
    return
  if amount > MAX_LIMIT:
    print("Withdraw amount exceeds the maximum limit.")
    return
  if amount > target_account["value"]:
    print("Insufficient balance.")
    return

  target_account["value"] -= amount
  target_account["withdraw_count"] += 1
  target_account["last_withdraw_day"] = date.today()
  target_account["actions"].append(
    f"Withdraw: R${amount:.2f} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
  )

def balance_function():
  print("\n=== Transaction History ===")
  for account in CURRENT_USER["checking_account"]:
    print(f"\n-- Agency: {account['agency']} Account Number: {account['account_number']} --")
    for action in account["actions"]:
      print(action)
    print(f"Current Balance: R${account['value']:.2f}")
  print("===========================\n")

def verify_day():
  current_day = date.today()
  for account in CURRENT_USER["checking_account"]:
    if account["last_withdraw_day"] is None:
      account["last_withdraw_day"] = current_day
    elif account["last_withdraw_day"] != current_day:
      account["withdraw_count"] = 0
      account["last_withdraw_day"] = current_day

def create_user():
  cpf = input("Enter your CPF: ").strip().replace(".", "").replace("-", "")
  if cpf in ALL_USERS:
    print("User already exists.")
    return None
  name = input("Enter your name: ")
  password = input("Enter your password: ")
  address = input("Enter your address: ")
  birth_date = input("Enter your birth date (YYYY-MM-DD): ")
  ALL_USERS[cpf] = {
    "nome": name,
    "cpf": cpf,
    "senha": password,
    "endereco": address,
    "data_nascimento": birth_date,
    "checking_account": []
  }
  print("User created successfully.")

def create_currency_account():
  global GLOBAL_ACCOUNT_COUNTER

  if CURRENT_USER is None:
    print("No user logged in.")
    return

  GLOBAL_ACCOUNT_COUNTER += 1
  new_account_number = GLOBAL_ACCOUNT_COUNTER

  CURRENT_USER["checking_account"].append({
    'agency': '0001',
    'account_number': new_account_number, 
    "value": 0.0,
    "last_withdraw_day": None,
    "withdraw_count": 0,
    "actions": []
  })
  print("Checking account created successfully.")
  print(f"Agency: 0001 | Account Number: {new_account_number}")

def login():
  global CURRENT_USER
  if not ALL_USERS:
    print("No users available. Please create a user first.")
    return
  if CURRENT_USER is not None:
    print("A user is already logged in.")
    return
  cpf = input("Enter your CPF: ").strip().replace(".", "").replace("-", "")
  password = input("Enter your password: ")
  user = ALL_USERS.get(cpf)
  if user and user["senha"] == password:
    CURRENT_USER = user
    print("Login successful.")
  else:
    print("Invalid CPF or password.")

def logout():
  global CURRENT_USER
  if CURRENT_USER is None:
    print("No user is currently logged in.")
    return
  CURRENT_USER = None
  print("Logged out successfully.")


if __name__ == "__main__":
  while True:
    command = input(main_input).strip().lower()
    if CURRENT_USER is not None:
      verify_day()

    if command == "q":
      print("Exiting the program...")
      break
    elif command == "d":
      if CURRENT_USER is None:
        print("No user logged in.")
        continue
      deposit_function()
    elif command == "w":
      if CURRENT_USER is None:
        print("No user logged in.")
        continue
      withdraw_function()
    elif command == "b":
      if CURRENT_USER is None:
        print("No user logged in.")
        continue
      balance_function()
    elif command == "c":
      create_user()
    elif command == "ca":
      create_currency_account()
    elif command == "lin":
      login()
    elif command == "lout":
      logout()
    else:
      print("Invalid command. Please try again.")
