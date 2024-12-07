# TODO Напишите функцию для поиска индекса товара
def product_search(list_products, desired_product):
    if desired_product in list_products:  # если искомый продукт есть в списке продуктов, то:
        return list_products.index(desired_product)  # возвращаем индекс искомых продуктов по списку

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = product_search(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
