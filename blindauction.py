#from art import logo
#print(logo)
# TODO-1: Ask the user for input
print("Welcome to blind Auction: ")


def find_highest_bid(bidding_record):
    highest_bid=0
    winner=""
    # TODO-4: Compare bids in dictionary
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"Thw winner is {winner} with highest bid of ${highest_bid}")

bids={}
should_continue=True
while should_continue:
      # TODO-2: Save data into dictionary {name: price}
      name=input("what's your name: ")
      price=int(input("Enter your bid:$ "))
      bids[name]=price
      # TODO-3: Whether if new bids need to be added
      should_continue=input("Are there any other bidders? type yes or no. ")
      if should_continue =="no":
          should_continue=False
          find_highest_bid(bids)
      elif should_continue=="yes":
          print("\n"*150)








