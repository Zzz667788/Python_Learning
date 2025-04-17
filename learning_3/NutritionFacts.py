def main():
    fruit_name = input("Item: ")
    print(serch_fruit(fruit_name))
def serch_fruit(name):
    fruits_nutrition_facts = {'Apple':130,
                              'Avocado': 50,
                              'Banana': 110,
                              'Cantaloupe': 50,
                              'Grapefruit': 60,
                              'Grapes': 90,
                              'Honeydew melon': 50,
                              'Kiwifruit': 90,
                              'Lemon': 15,
                              'Lime': 20,
                              'Nectarine': 60,
                              'Orange': 80,
                              'Peach': 60,
                              'Pear': 100,
                              'Pineapple': 50,
                              'Plums': 70,
                              'Strawberries': 50,
                              'Sweet Cherries': 100,
                              'Tangerine': 50,
                              'Watermelon': 80
                              }
    if name.capitalize() in fruits_nutrition_facts:
        return "Calories: " + str(fruits_nutrition_facts.get(name.capitalize(),''))
    else:
        return ''
if __name__ == '__main__':
    main()