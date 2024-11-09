list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]  # первая половина команды
second_team = list_players[middle_index:]  # вторая половина команды

print(first_team)
print(second_team)
