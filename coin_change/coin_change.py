#!/usr/bin/env python

# Filename: coin_change.py
# Created on: July  1, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

from collections import OrderedDict

from .config import COINS, INFINITY


def min_coins(amount, coins=COINS) -> int:
    """
    @brief
        Calcula a quantidade mínima de moedas necessárias para obter o total desejado com
        as moedas disponíveis utilizando programação dinâmica.
        Esse problema é um dos estudados no curso de Algoritmos I (DCC206-DIG) do DCC/UFMG

        Função utilizada apenas para verificar se a quantidade de moedas obtida pela função
        coin_change está correta

    @param amount
        O valor total que se deseja obter com as moedas disponíveis

    @param coins
        Lista de moedas disponíveis. O algoritmo assume que não há limite de moedas de cada
        valor disponível

    @return
        A quantidade mínima de moedas necessárias para obter o total desejado
        -1 se não for possível obter o total com as moedas disponíveis
    """

    # Casos bases
    if amount < 0:
        raise ValueError("O valor total deve ser maior ou igual a zero")

    if amount == 0:
        return 0

    # Ordenar a lista de moedas em ordem decrescente. Isso é necessário para garantir que
    # a solução ótima seja encontrada
    coins.sort(reverse=True)

    # Tabela de memoização
    memo = [0 for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        memo[i] = INFINITY

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                sub_res = memo[i - coin]
                if sub_res != INFINITY and sub_res + 1 < memo[i]:
                    memo[i] = sub_res + 1

    return memo[amount] if memo[amount] != INFINITY else -1


def coin_change(amount, coins=COINS):
    """
    @brief
        Calcula a quantidade mínima de moedas de cada valor necessárias para obter o total
        desejado com as moedas disponíveis

    @param amount
        O valor total que se deseja obter com as moedas disponíveis

    @param coins
        Lista de moedas disponíveis. O algoritmo assume que não há limite de moedas de cada
        valor disponível

    @return
        json com a quantidade mínima de moedas de cada valor necessárias para obter o total
    """

    # Casos bases
    if amount < 0:
        raise ValueError("O valor total deve ser maior ou igual a zero")

    if amount == 0:
        return {coin: 0 for coin in coins}, 0

    # Ordenar a lista de moedas em ordem decrescente. Isso é necessário para garantir que
    # a solução ótima seja encontrada
    coins.sort(reverse=True)

    solution = {coin: 0 for coin in coins}
    total_coins = 0

    for coin in coins:
        while amount >= coin:
            solution[coin] += 1
            total_coins += 1
            amount -= coin

    if amount != 0:
        raise ValueError("Nao eh possivel obter o total com as moedas disponiveis")

    solution_sorted = OrderedDict(
        sorted(solution.items(), key=lambda x: x[0], reverse=True)
    )

    return solution_sorted, total_coins
