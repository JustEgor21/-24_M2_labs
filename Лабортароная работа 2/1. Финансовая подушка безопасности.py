money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count_months = 0  # Количество месяцев
remains_budget = money_capital + salary - spend  # Остаток от бюджета в 1-ом месяце после трат

while remains_budget >= 0:  # Цикл while выполняется, пока остаток от бюджета >= 0
    spend += spend * increase
    remains_budget += salary - spend
    count_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", count_months)
