import random

def three_prize():
    prizes = [
        "A roll of premium toilet paper - Soft, strong, and comforting in tough times.",
        "Novelty mug - A funny or motivational mug to lift your spirits.",
        "$5 coffee shop gift card - Enough for a quick caffeine fix."
    ]
    return random.choice(prizes)

def four_star_prize(index):
    prizes = [
        "High-quality suitcase - Durable and stylish, perfect for travel enthusiasts.",
        "Mixer-grinder - A versatile kitchen appliance for cooking convenience.",
        "Air fryer - A trendy gadget for health-conscious food lovers.",
        "Premium coffee maker - Brew barista-quality coffee at home.",
        "Smartwatch - Tracks fitness, notifications, and more.",
        "Portable vacuum cleaner - Compact and efficient for easy cleaning.",
        "Premium cookware set - Includes non-stick pans, pots, and utensils.",
        "Noise-canceling headphones - High-quality sound and comfort.",
        "Kindle e-reader - Perfect for book lovers who want to carry an entire library.",
        "Electric kettle with temperature control - Ideal for tea and coffee enthusiasts."
    ]
    random.shuffle(prizes)
    return prizes[index % len(prizes)]

def standard_prize():
    prizes = [
        "Fitness package - Includes a smartwatch, gym membership, and fitness equipment.",
        "E-bike or electric scooter - Perfect for eco-friendly and fun commuting.",
        "Luxury spa retreat - A 3-day wellness retreat with massages, yoga, and gourmet meals."
    ]
    return random.choice(prizes)

def pull(x, four_star, five_star, desired_fs):
    if x == five_star:
        print("\n\tBINGO!\nCONGRATULATIONS!!")
        if random.randint(1, 2) == 1:
            print("You Have Won:", desired_fs)
        else:
            print("You Have Won:", standard_prize())
        print()
        x = 0
        five_star = random.randint(1, 100)  # Re-randomize five_star after winning
    else:
        if x in four_star:
            print("\nHURRAY!")
            print("You Have Won:", four_star_prize(four_star.index(x)))
            print()
        else:
            print("You get:", three_prize())
        x += 1
    return x, five_star

def pull_main(x, four_star, five_star, desired_fs):
    while True:
        print("choose:")
        print("1. Buy 1 ticket")
        print("2. Buy 10 tickets - gives one guaranteed high value prize")
        print("3. Choose another Banner")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Your pull is:")
            x, five_star = pull(x, four_star, five_star, desired_fs)
        elif choice == '2':
            print("Your pulls are:")
            for _ in range(10):
                x, five_star = pull(x, four_star, five_star, desired_fs)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
    return x, five_star

def main():
    random.seed()
    x = 0
    five_star = random.randint(1, 100)  # SET ONLY ONCE and updated only after win
    while True:
        four_star = []
        for i in range(10):
            while True:
                val = random.randint(0, 10) + (i * 10)
                if val != five_star:
                    four_star.append(val)
                    break

        print("Which Banner Would You Like To Pull For?")
        print("1. A trip to Paris for two")
        print("2. Luxury cruise vacation")
        print("3. Electric luxury car")
        print("4. Quit Buying Lottery Tickets")
        banner = input("Enter your choice: ")

        if banner == '1':
            desired_fs = "A trip to Paris for two - Includes flights, a 5-star hotel stay, and Eiffel Tower tickets."
            x, five_star = pull_main(x, four_star, five_star, desired_fs)
        elif banner == '2':
            desired_fs = "Luxury cruise vacation - A 7-day all-inclusive Mediterranean cruise."
            x, five_star = pull_main(x, four_star, five_star, desired_fs)
        elif banner == '3':
            desired_fs = "Electric luxury car - A Tesla Model 3 or equivalent, eco-friendly and stylish."
            x, five_star = pull_main(x, four_star, five_star, desired_fs)
        elif banner == '4':
            print("Thank You for participating in the Lottery Game!")
            break
        else:
            print("Invalid selection. Exiting game.")
            break

if __name__ == '__main__':
    main()
