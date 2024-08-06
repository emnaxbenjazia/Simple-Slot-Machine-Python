import random  


MAX_LINES = 3 # constant variable, all caps by convention
MAX_BET = 100 # constant variable, all caps by convention
MIN_BET = 1 # constant variable, all caps by convention

ROWS = 3
COLS = 3

symbol_count = { # how many times each symbol appears in one column
     "A": 2,
     "B": 4,
     "C": 6,
     "D": 8 
}

symbol_value = { # value of each symbol
     "A": 5,
     "B": 4,
     "C": 3,
     "D": 2 
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # line will take values 0, 1, 2 and lines will be 1, 2, 3 (lines is how many lines the player is betting on from top to bottom)
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else: # this else is for the for loop, if the loop completes without breaking, the else block will be executed
            winnings += values[symbol]*bet
            winning_lines.append(line+1) # we add 1 because the line variable starts at 0   
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) # adds the symbol to the list symbol_count times

    columns = []
    for _ in range(cols):
        column= []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns): # enumerate returns the index and the value of the list  (0, seq[0]), (1, seq[1]), (2, seq[2]), 
            if i != len(columns) - 1 :
                print(col[row], "|", end=" ")
            else:
                print(col[row], end=" ") # end=" " prevents the print function from adding a new line character because by default end="\n"
        print() # prints a new line \n character after each row donc kol row fi star wahdou

def deposit():
    while True:
        amount = input("How much would you like to deposit? $") #we'll get a string
        if amount.isdigit(): # tests if string is a digit (positive or zero)
                amount = int(amount) #converts string to integer
                if amount > 0:
                    break
                else:
                    print("your deposit must be greater than 0. Please try again.")
        else:
            print("Invalid amount. Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on (1 - " + str(MAX_LINES)+") ?  ") # we cant concatenate a number and a string with + bevause it will try to perform an add operation so we convert the number to a string
        if lines.isdigit(): # tests if string is a digit (positive or zero)
                lines = int(lines) #converts string to integer
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines.")
        else:
            print("Invalid input. Please enter a number.")
    return lines
     
def get_bet():
    while True:
        bet = input(f"How much would you like to bet ({MIN_BET} -  {MAX_BET}) ? $") #we'll get a string. variables in curly brakets will be converted to strings
        if bet.isdigit(): # tests if string is a digit (positive or zero)
                bet = int(bet) #converts string to integer
                if MIN_BET <= bet <= MAX_BET:
                    break
                else:
                    print("Enter a valid bet amount.")
        else:
            print("Invalid input. Please enter a number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money to make that bet, your balance is ${balance}. Please try again.")
        else:
            break
    print(f"balance: ${balance}")
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"Winning lines:", *winning_lines) # the * will unpack the list and print the elements separated by a space
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play, q to quit: ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"Your final balance is ${balance}")
    

main()