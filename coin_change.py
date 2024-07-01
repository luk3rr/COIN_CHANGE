#!/usr/bin/env python

# Filename: coin_change.py
# Created on: July  1, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

import json
import sys

COINS = [100, 50, 20, 10, 5, 2]


def coin_change(total):
    """
    @brief
        Calcula a quantidade mínima de moedas de cada valor necessárias para obter o total
        desejado com as moedas disponíveis

    @param total
        O valor total que se deseja obter com as moedas disponíveis

    @return
        json com a quantidade mínima de moedas de cada valor necessárias para obter o total
    """
    solution = {coin: 0 for coin in COINS}

    for coin in COINS:
        while total >= coin:
            solution[coin] += 1
            total -= coin

    if total != 0:
        raise ValueError("Não é possível obter o total com as moedas disponíveis")

    return solution


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 coin_change.py <total>")
        sys.exit(1)

    value = int(sys.argv[1])

    try:
        solution = coin_change(value)
    except ValueError as e:
        print(e)
        sys.exit(1)

    solution_sorted = dict(sorted(solution.items(), key=lambda x: x[0], reverse=True))
    print(json.dumps(solution_sorted, indent=4))


if __name__ == "__main__":
    main()
