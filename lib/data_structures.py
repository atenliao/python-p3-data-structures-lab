spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    a = []
    for dic in spicy_foods:
        a.append(dic['name'])
    return a

def get_spiciest_foods(spicy_foods):
    newList=[]
    for dic in spicy_foods:
        if(dic["heat_level"]> 6):
            newList.append(dic)
    return newList

def print_spicy_foods(spicy_foods):
    for dic in spicy_foods: 
        print(f'{dic["name"]} ({dic["cuisine"]}) | Heat Level: {"🌶"*dic["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dic in spicy_foods:
        if(dic['cuisine'] == cuisine):
            return dic

def print_spiciest_foods(spicy_foods):
    for dic in spicy_foods:
        if(dic['heat_level'] > 5):
            print(f'{dic["name"]} ({dic["cuisine"]}) | Heat Level: {"🌶"* dic["heat_level"]}')

def get_average_heat_level(spicy_foods):
    count = len(spicy_foods)
    total = 0
    for dic in spicy_foods:
        total = total + dic["heat_level"]
    
    return (int(total / count))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return(spicy_foods)



# get_names(spicy_foods)
# get_spiciest_foods(spicy_foods)
# print_spicy_foods(spicy_foods)
# get_spicy_food_by_cuisine(spicy_foods, 'American')
# get_average_heat_level(spicy_foods)