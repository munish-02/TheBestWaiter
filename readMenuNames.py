import json

def readMenuNames():
	with open("Menu.json") as file:
		json_data = json.load(file)

	# Access the food menu items
	food_menu = json_data["foodMenu"]
	names = [item["name"] for item in food_menu]
	return names

def readMenuNamesWithPrices():
	with open("Menu.json") as file:
		json_data = json.load(file)

	# Access the food menu items
	food_menu = json_data["foodMenu"]
	nameAndPriceList = []
	for item in food_menu:
		name = item["name"]
		price = item["price"]
		nameAndPriceList.append((name, price))
	return nameAndPriceList

def readMenuNamesWithPricesAndDescription():
	with open("Menu.json") as file:
		json_data = json.load(file)

	# Access the food menu items
	food_menu = json_data["foodMenu"]
	nameAndPriceListWithDisc = []
	for item in food_menu:
		name = item["name"]
		price = item["price"]
		description=iten["description"]
		nameAndPriceListWithDisc.append((name, price,description))
	return nameAndPriceListWithDisc


foodNames=readMenuNames()
print(foodNames)

nameAndPriceList=readMenuNamesWithPrices()
print(nameAndPriceList)