import random

MAX_SLOTS = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🍒": 2,
    "🍊": 4,
    "🍋": 6,
    "🍉": 8,
}

symbol_values = {
    "🍒": 5,
    "🍊": 4,
    "🍋": 3,
    "🍉": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in lines:
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(rows):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def savingbag():
    while True:
        cosmicjar = input("how many yuan would you like to add to your saving bag today? ¥")
        if cosmicjar.isdigit():
            cosmicjar = int(cosmicjar)
            if cosmicjar > 0:
                break
            else:
                print("REQUIREMENT: Your Yuan in the savings bag must be filled like a lucky red envelope—always! 🧧💰✨")
        else:
            print("please enter a numerical value for your savings bag")

    return cosmicjar

def get_number_of_lines():
    while True:
        slots = input("how many lucky slot would you like to bet (1-" + str(MAX_SLOTS) + ")? ")
        if slots.isdigit():
            slots = int(slots)
            if 1 <= slots <= MAX_SLOTS:
                break
            else:
                print("REQUIREMENT: enter a valid number of slots! 🧧💰✨")
        else:
            print("please enter a numerical value for your savings bag")

    return slots

def get_bet():
    while True:
        cosmicjar = input("how many yuan would you like to bet on each slots today? ¥")
        if cosmicjar.isdigit():
            cosmicjar = int(cosmicjar)
            if MIN_BET <= cosmicjar <= MAX_BET:
                break
            else:
                print(f"REQUIREMENT: Your Yuan in the savings bag must be between ¥{MIN_BET} - ¥{MAX_BET}! 🧧💰✨")
        else:
            print("please enter a numerical value for your savings bag")

    return cosmicjar    

def gamblejapan_spin(balance, symbol_count, symbol_values, ROWS, COLS):
    slots = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * slots

        if total_bet > balance:
            print(f"You don't have enough money to make that bet! Your current balance is: ¥{balance} 🧧💰✨")
        else:
            break

    print(f"You've got ¥{balance} tucked away in your savings pouch, and you're sprinkling ¥{bet} on {slots} lucky slots! That's a total bet of ¥{total_bet} for a dash of sparkle and a whole lot of fun! 🪙💰🎰✨")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, range(ROWS), bet, symbol_values)
    print(f"You won ¥{winnings}! 🧧🪙💰✨")
    print("Your winning lines were:", end=" ")
    for line in winning_lines:
        print(line, end=" ")
    print("! 🧧🪙💰✨")
    return winnings - total_bet

def main():
    balance = savingbag()
    while True:
        print(f"Your current balance is: ¥{balance} 🧧💰✨")
        gamble = input("Press enter to play, or type 'q' to quit: ")
        if gamble == "q":
            break
        balance += gamblejapan_spin(balance, symbol_count, symbol_values, ROWS, COLS)

    print(f"Thanks for playing! Your final balance is: ¥{balance} 🧧💰✨")


main()