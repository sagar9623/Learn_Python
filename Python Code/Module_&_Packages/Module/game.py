# game.py
# import the draw module

import draw

def play_game():
    return "Victory"

def main():
    result = play_game()
    draw.draw_game(result)

if __name__ == '__main__':
    main()