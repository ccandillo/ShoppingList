class IngredientTemplate:
    quantity = ''

    def add_ingredient(self):
        self.food = input('Enter Ingredient: ')

    def add_category(self):
        self.category = input('Enter Category: ')

    def delete_ingredient():
        raise NotImplementedError()

    def delete_catetory():
        raise NotImplementedError()

    def modify_category():
        raise NotImplementedError()


class Ingredient(IngredientTemplate):
    pass


