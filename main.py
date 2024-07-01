#!/usr/bin/env python3

# Filename: main.py
# Created on: July  1, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

import sys
import json
from coin_change import coin_change

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

    solution_sorted = dict(
        sorted(solution[0].items(), key=lambda x: x[0], reverse=True)
    )
    print(json.dumps(solution_sorted, indent=4))


if __name__ == "__main__":
    main()
