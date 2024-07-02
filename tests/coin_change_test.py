#!/usr/bin/env python3

# Filename: coin_change_test.py
# Created on: July  1, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

import unittest
from random import randrange
from coin_change.coin_change import coin_change, min_coins

TEST_COINS = [10, 5, 1, 3, 50]


class CoinChangeTest(unittest.TestCase):
    def test_negative_amount(self):
        """
        @brief:
            Testa a função para quantia negativa
        """
        with self.assertRaises(ValueError):
            coin_change(-10, TEST_COINS)

    def test_min_coins_random_amount(self):
        """
        @brief
            Testa o mínimo de moedas necessárias para um valor pseudo-aleatório
        """
        random_value = randrange(0, 1000)
        self.assertEqual(
            coin_change(random_value, TEST_COINS)[1],
            min_coins(random_value, TEST_COINS),
            "O mínimo de moedas necessárias para o troco não está correto",
        )


if __name__ == "__main__":
    unittest.main()
