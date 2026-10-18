
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
bidders = {}
name = input("What is your name? ")
bid = int(input("What is your bid? "))
bidders[name] = bid
more_bidders = input("Are there any other bidders? Type 'yes or 'no'.")
if more_bidders == 'no':
    max_bid = 0
    for key in bidders:
        if bidders[key] > max_bid:
            max_bid = bidders[key]
    for key in bidders:
        if bidders[key] == max_bid:
            print(f"The winner is {key} with a bid of ${bidders[key]}")
elif more_bidders == 'yes':
    while more_bidders == 'yes':
            print("\n" * 20)
            name = input("What is your name? ")
            bid = int(input("What is your bid? "))
            bidders[name] = bid
            more_bidders = input("Are there any other bidders? Type 'yes or 'no'.")
            if more_bidders == 'no':
                max_bid = 0
                for key in bidders:
                    if bidders[key] > max_bid:
                        max_bid = bidders[key]
                for key in bidders:
                    if bidders[key] == max_bid:
                        print(f"The winner is {key} with a bid of ${bidders[key]}")

# TODO-4: Compare bids in dictionary


