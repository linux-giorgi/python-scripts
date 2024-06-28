#python slot machine
import os
import random
import time
os.system("clear");
def spin_row():
    symbols=['🍒','🍉','🍋','🔔','⭐']
    return[random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("\033[34m*************\033[0m")
    print("\033[34m | \033[0m".join(row))
    print("\033[34m*************\033[0m")
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet *5
        elif row[0] == '🔔':
            return bet *10
        elif row[0] == '⭐':
            return bet  *20
    return 0
def main():
    balance=100
    print("\033[34m***********************\033[0m")
    print("\033[92m\033[5mWelcome To Python Slots\033[25m\033[0m")
    print("\033[36mSymbols:🍒 🍉 🍋 🔔 ⭐ \033[0m")
    print("\033[34m***********************\033[0m")
    while balance>0:
        print(f"\033[96mCurrent balance: ${balance}\033[0m")
        bet = input("\033[92mplease your bet amount: \033[0m")    
        if not bet.isdigit():
            print("\033[91mplease enter a valid number\033[0m")
            continue
        bet = int(bet)
        if bet > balance:
            print("\033[32mInsufficient funds\033[0m")
            continue
        if bet <= 0:
            print("\033[32mbet must be greater than 0\033[0m")
            continue
        balance -= bet
        row = spin_row()
        print("\033[93mspining...\n\033[0m")
        time.sleep(0.3)
        print_row(row)
        payout=get_payout(row, bet)
        if payout>0:
            print(f"\033[36myou won ${payout}\033[0m")
        else:
            print("\033[35mSorry you lost this round\033[0m")
        balance+=payout
    print("\033[91m*******************************\033[0m")
    print(f"\033[91mgame over! balance is:{balance}\033[0m")
    print("\033[91m*******************************\033[0m")
if __name__ == '__main__':
    main()
