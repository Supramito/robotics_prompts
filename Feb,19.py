
# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(f"{BLUE}Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!{RESET}")

my_name = input(f"{GREEN}What is your name?: {RESET}")
my_enemy = input(f"{RED}What is your enemy's name?: {RESET}")
my_superpower = input(f"{BLUE}What is your superpower?: {RESET}")

print(f"{GREEN}Hello, {RED}{my_name}{GREEN}! Your ability to {BLUE}{my_superpower}{GREEN} will make sure you never have to look at {RED}{my_enemy}{GREEN} again.{RESET}")
