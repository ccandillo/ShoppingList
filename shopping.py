from ingredients import Ingredient
from query import QueryTemplate


class ShoppingListTemplate(Ingredient):
    ingredients = []

    def add_item_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_ingredient()
        self.ingredients.append(ingredient)

    def add_item_category(self, ingredient_obj):
        category = ingredient_obj
        category.add_category()

    def delete_item():
        pass

    def modify_item():
        pass

    def update_db(self):
        food = self.ingredients[-1].food
        category = self.ingredients[-1].category
        self.conn.execute('INSERT INTO Food (ingredient, category) VALUES("%s", "%s")' % (food, category))
        self.conn.commit()


class ShoppingList(ShoppingListTemplate, QueryTemplate):
    def construct_query(self):
        self.query = 'SELECT * from Food'

    def output_results(self):
        print(self.formatted_results)

    def process_format(self):
        self.add_item_ingredient()
        self.add_item_category(self.ingredients[-1])
        self.connect()
        self.query_db()
        self.update_db()
        self.add_category()
        self.query_db()
        self.update_db()
        self.format_results()
        self.output_results()


if __name__ == '__main__':
    shoppinglist = ShoppingList()
    shoppinglist.add_item_ingredient()
    shoppinglist.add_item_category(shoppinglist.ingredients[-1])
    shoppinglist.connect()
    shoppinglist.update_db()
    shoppinglist.construct_query()
    shoppinglist.do_query()
    shoppinglist.format_results()
    shoppinglist.output_results()


