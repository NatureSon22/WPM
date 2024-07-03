import curses
from curses import wrapper
import time

list_levels = [
    "A lesson without pain is meaningless.",
    "Those who cannot acknowledge themselves will eventually fail.",
    "The night is darkest just before dawn. But keep your eyes open. If you avert your eyes from the dark, you’ll be blind to the rays of a new day. So keep your eyes set on the dark, and the light will come."
]

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "This is a simple game for you to test your typing speed. A block of text will appear and you have to type it as quickly as possible.")
    stdscr.addstr(1, 0, "Press any key to start...")
    stdscr.getkey()
    stdscr.refresh()

def set_challenge(stdscr, level):
    stdscr.clear()
    stdscr.addstr(0, 0, list_levels[level])
    stdscr.refresh()

def user_input(stdscr, challenge_text):
    stdscr.move(1, 0)
    x = 0
    start_time = time.time()
    user_text = []
    correct_chars = 0
    
    while True:
        key = stdscr.getkey()
        
        if key == "\n":
            break
        elif key == "\b":
            if x > 0:
                x -= 1
                stdscr.delch(1, x)
                user_text.pop()
        else:
            user_text.append(key)
            stdscr.addch(1, x, key)
            x += 1
        
        stdscr.refresh()

    end_time = time.time()
    time_taken = end_time - start_time
    correct_chars = sum(1 for i, char in enumerate(user_text) if i < len(challenge_text) and char == challenge_text[i])
    wpm = (correct_chars / 5) / (time_taken / 60)
    return wpm

def close_program(stdscr, wpm):
    stdscr.clear()
    stdscr.addstr(0, 0, f"Thank you for playing! Your typing speed is {wpm:.2f} WPM.")
    stdscr.addstr(1, 0, "Press any key to exit.")
    stdscr.getkey()
    curses.endwin()
    exit()

def main(stdscr):
    start_screen(stdscr)
    user_quit = False

    while not user_quit:
        for level in range(len(list_levels)):
            set_challenge(stdscr, level)
            wpm = user_input(stdscr, list_levels[level])
        
        close_program(stdscr, wpm)
        user_quit = True

wrapper(main)