#!/usr/bin/env python3
from brain_games.brains import start
from brain_games.games import calc_game


def main():
    start(calc_game)


if __name__ == '__main__':
    main()
