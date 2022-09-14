import random
import os
import keyboard
import time

good_result = 0
bad_result = 0

lower_range = int(input("give me first number: "))
greater_range = int(input("give me the last number: "))

player_name = input("type your name: ")


f = open("players.txt", "a")
f.write(f"\n{player_name}")
f.close()

while True:
    os.system('cls')
    for i in range(1):
        x = random.randint(lower_range, greater_range)
        y = random.randint(lower_range, greater_range)
    print("bad_results:", bad_result, "good_results:", good_result)
    result = input(f"your operation is: {x} * {y} = ")
    x *= y
    if int(result) == x:
        good_result += 1
    else:
        bad_result += 1
        print("good result was: ", x)
        choice = input("press enter to continue or 'q' to quit\n")
        if choice == 'q':
            break

with open('logs.txt', 'a') as f:
    f.write(f"\nplayer: {(player_name)} bad_results: {bad_result} good_results: {good_result}\n")
