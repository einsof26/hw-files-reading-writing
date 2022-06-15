def book_cook_dict(file_name):
    with open(file_name, "rt",encoding="utf-8") as file:
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
