def main():
    fruit = input("Item: ").strip().lower()
    calories = [
        {"name":"apple", "calories":"130"},
        {"name":"avocado", "calories":"50"},
        {"name":"banana", "calories":"110"},
        {"name":"cantaloupe", "calories":"50"},
        {"name":"grapefruit", "calories":"60"},
        {"name":"grapes", "calories":"90"},
        {"name":"honeydrew melon", "calories":"50"},
        {"name":"kiwifruit", "calories":"90"},
        {"name":"pear", "calories":"100"},
        {"name":"sweet cherries", "calories":"100"},
        ]
    for item in calories:
        if item["name"] == fruit:
            print(f"Calories: {item['calories']}")
            break

main()
