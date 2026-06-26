def generate_band_name():
    print("Welcome to the Band Name Generator")

    city_name = input("What's your city you grew up in! ").strip()
    pet_name = input("What's your pet name? ").strip()

    band_name = f"{city_name.title()} {pet_name.title()}"

    print(f"Your band name is {band_name}")

    if not city_name or not pet_name:
        print("Please enter your valid city and pet name!")
        return

generate_band_name()
