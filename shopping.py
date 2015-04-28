from ingredients import Ingredient
from query import QueryTemplate


class ShoppingListTemplate(Ingredient):
    ingredients = []

    def add_item(self):
        ingredient = Ingredient()
        ingredient.add_ingredient()
        self.ingredients.append(ingredient)

    def delete_item():
        pass

    def modify_item():
        pass

    def update_db(self):
        food = self.ingredients[-1].food
        self.conn.execute('INSERT INTO Food (ingredient) VALUES("%s")' % (food))
        self.conn.commit()


class ShoppingList(ShoppingListTemplate, QueryTemplate):
    def construct_query(self):
        self.query = 'SELECT * from Food'

    def output_results(self):
        print(self.formatted_results)

    def process_format(self):
        self.add_item()
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
    shoppinglist.add_item()
    shoppinglist.connect()
    shoppinglist.update_db()
    shoppinglist.construct_query()
    shoppinglist.do_query()
    shoppinglist.format_results()
    shoppinglist.output_results()


