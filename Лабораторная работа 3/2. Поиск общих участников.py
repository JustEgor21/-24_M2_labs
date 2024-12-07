# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, separator=','):
    for_group_1 = group_1.split(separator)
    for_group_2 = group_2.split(separator)

    list_name_intersection = list(set(for_group_1).intersection(for_group_2))
    list_name_intersection.sort()

    return list_name_intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,))
