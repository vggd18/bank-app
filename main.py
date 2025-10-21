from datetime import datetime, date

main_input = """
Input a command:
[q] Quit
[d] Deposit
[w] Withdraw
[b] Balance
"""

USER_BALANCE = {
  "value": 0.0,
  "last_withdraw_day": None,
  "withdraw_count": 0,
  "actions": []
}
MAX_LIMIT = 500.0
MAX_DAILY_WITHDRAWS = 3


def deposit_function(value):
  try:
    amount = float(value)
  except ValueError:
    print("Valor inválido.")
    return

  if amount <= 0:
    print("Deposit amount must be positive.")
    return

  USER_BALANCE["value"] += amount
  USER_BALANCE["actions"].append(
    f"Deposit: R${amount:.2f} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
  )

def withdraw_function(value):
  try:
    amount = float(value)
  except ValueError:
    print("Valor inválido.")
    return

  if USER_BALANCE["withdraw_count"] >= MAX_DAILY_WITHDRAWS:
    print("Daily withdraw limit reached.")
    return
  if amount <= 0:
    print("Withdraw amount must be positive.")
    return
  if amount > MAX_LIMIT:
    print("Withdraw amount exceeds the maximum limit.")
    return
  if amount > USER_BALANCE["value"]:
    print("Insufficient balance.")
    return

  USER_BALANCE["value"] -= amount
  USER_BALANCE["withdraw_count"] += 1
  USER_BALANCE["last_withdraw_day"] = date.today()
  USER_BALANCE["actions"].append(
    f"Withdraw: R${amount:.2f} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
  )


def balance_function():
  for action in USER_BALANCE["actions"]:
    print(action)
  print(f"Current Balance: R${USER_BALANCE['value']:.2f}")


def verify_day():
  current_day = date.today()
  if USER_BALANCE["last_withdraw_day"] is None:
    USER_BALANCE["last_withdraw_day"] = current_day
  elif USER_BALANCE["last_withdraw_day"] != current_day:
    USER_BALANCE["withdraw_count"] = 0
    USER_BALANCE["last_withdraw_day"] = current_day


if __name__ == "__main__":
  while True:
    command = input(main_input).strip().lower()
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
    else:
      print("Invalid command. Please try again.")
