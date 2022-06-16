def book_cook_dict(file_name):
    with open(file_name, "rt",encoding="utf-8") as file:
        global cook_book
        cook_book = {}
        for line in file:
            dish_name = file.readline().strip()
            quant = file.readline().strip()
            cook_book[dish_name] = []
            L_ingredient = []
            for i in range(int(quant)): 
                Str_ingredient = (file.readline().strip()).split("|")
                recipe = {'ingredient_name': Str_ingredient[0] , 'quantity': Str_ingredient[1], 'measure': Str_ingredient[2]}
                L_ingredient.append(recipe)
            cook_book[dish_name] = L_ingredient
        for k,v in cook_book.items():
            print(k)
            for item in v:
                print(item)
            print()


book_cook_dict("catalog.txt")
print("====================================================================")  

def get_shop_list_by_dishes(dishes, person_count=1):
    new_dict = {}
    for i in range(len(dishes)):
        x = dishes[i]   #Блюдо из списка заказа
        y = cook_book[x] #Список словарей с ингридиентами заказанного блюда
        total = {}
        for elem in y:
            new_dict[elem['ingredient_name']] = {'quantity': int(elem['quantity'])*person_count,'measure': elem['measure']}#Новый словарь с ключем - имя ингридиента
                                                                                                         #и значением - количество и единица измерения
            total.update(new_dict)
    print("Необходимые ингридиенты для приготовления заказанных блюд: ")
    for k,v in total.items():
        print(f'{k} : {v}')
        
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
