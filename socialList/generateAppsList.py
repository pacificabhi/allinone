apps_old_list_path = "social_list.json"
apps_new_list_path = "apps_list.json"


import json

def get_title_in_key_format(title):
    title = title.lower()
    title = title.split(" ")
    return "_".join(title)

def write_to_new_file(final_dict):

    with open(apps_new_list_path, "w") as new_file:
        json.dump(final_dict, new_file, indent=4)
    

def generate(old_file):
    old_apps_file_dict = json.loads(old_file.read())
    old_apps_list = old_apps_file_dict["apps"]
    new_apps_dict = {}
    for app in old_apps_list:
        app_key = get_title_in_key_format(app["app_name"])
        #print(app_key)
        new_apps_dict[app_key] = app

    old_categories_list = old_apps_file_dict["categories"]
    new_categories_dict = {}

    for category in old_categories_list:
        category_key = get_title_in_key_format(category["category"])
        new_categories_dict[category_key] = category

    final_dict = {"apps": new_apps_dict, "categories": new_categories_dict}
    write_to_new_file(final_dict);




with open(apps_old_list_path) as old_apps_file:
    generate(old_apps_file)
