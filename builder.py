def build():
    attrs = {
            "name": "",
            "role": "",
            "weapon_type": "",
            "effective_range": "",
            "mobility": "",
            "ease_of_value": ""
    }
    for key in attrs.keys():
        attrs[key] = input(f"{key}: ")
    return attrs

if __name__ == "__main__":
    import json
    for x in range(32):
        print("input hero")
        hero = build()
        with open(f"{hero['name']}.json", "w") as f:
            json.dump(hero, f)

