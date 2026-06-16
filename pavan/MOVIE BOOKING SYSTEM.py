movies = [

    {"name": "Pushpa 2", "price": 200, "seats": 5, "rating": "9.5"},
    {"name": "Kalki", "price": 250, "seats": 4, "rating": "9.8"},
    {"name": "RRR", "price": 180, "seats": 6, "rating": "9.7"},
    {"name": "KGF 2", "price": 220, "seats": 5, "rating": "9.4"},
    {"name": "Salaar", "price": 240, "seats": 5, "rating": "9.6"},
    {"name": "Leo", "price": 210, "seats": 4, "rating": "9.1"},
    {"name": "Jailer", "price": 190, "seats": 6, "rating": "9.0"},
    {"name": "Avatar 2", "price": 300, "seats": 3, "rating": "9.9"},
    {"name": "Bahubali", "price": 230, "seats": 5, "rating": "9.8"},
    {"name": "Interstellar", "price": 350, "seats": 2, "rating": "10"},
    {"name": "Spider Man", "price": 260, "seats": 4, "rating": "9.3"},
    {"name": "Batman", "price": 240, "seats": 5, "rating": "9.2"},
    {"name": "Jawan", "price": 210, "seats": 5, "rating": "9.1"},
    {"name": "Animal", "price": 220, "seats": 6, "rating": "9.0"},
    {"name": "Master", "price": 200, "seats": 5, "rating": "8.9"}
]

bookings = []

money = 0
ticket_id = 5000

print("================================")
print("     MEGA CINEMA WORLD")
print("================================")

user_name = input("Enter Your Name: ")

print("Welcome", user_name)

while True:

    print("\n================================")
    print("1. Show Movies")
    print("2. Book Normal Ticket")
    print("3. Book VIP Ticket")
    print("4. Book GOLD Ticket")
    print("5. Food Corner")
    print("6. Booking History")
    print("7. Search Ticket")
    print("8. Cancel Ticket")
    print("9. Total Collection")
    print("10. Exit")
    print("================================")

    choice = input("Enter Choice: ")

    match choice:

        case "1":

            print("\nNOW SHOWING MOVIES\n")

            for movie in movies:

                print("Movie  :", movie["name"])
                print("Price  :", movie["price"])
                print("Seats  :", movie["seats"])
                print("Rating :", movie["rating"])
                print("--------------------------")

        case "2" | "3" | "4":

            movie_name = input("Enter Movie Name: ")

            found = False

            for movie in movies:

                if movie["name"] == movie_name:

                    found = True

                    if movie["seats"] > 0:

                        movie["seats"] = movie["seats"] - 1

                        seat_number = movie["seats"] + 1

                        if choice == "2":
                            ticket_type = "Normal"
                            final_price = movie["price"]

                        elif choice == "3":
                            ticket_type = "VIP"
                            final_price = movie["price"] + 150

                        else:
                            ticket_type = "GOLD"
                            final_price = movie["price"] + 300

                        money = money + final_price

                        ticket_id = ticket_id + 1

                        booking = {

                            "id": ticket_id,
                            "name": user_name,
                            "movie": movie["name"],
                            "type": ticket_type,
                            "price": final_price,
                            "seat": seat_number
                        }

                        bookings.append(booking)

                        print("\nTICKET BOOKED SUCCESSFULLY")
                        print("Ticket ID :", ticket_id)
                        print("Seat No   :", seat_number)
                        print("Type      :", ticket_type)
                        print("Price     :", final_price)

                    else:
                        print("HOUSE FULL")

            if found == False:
                print("Movie Not Found")

        case "5":

            print("\n========== FOOD MENU ==========")
            print("1. Popcorn Combo  - 120")
            print("2. Burger Combo   - 150")
            print("3. Pizza Combo    - 250")
            print("4. Cooldrink      - 90")
            print("5. Ice Cream      - 110")

            food = input("Enter Food Number: ")

            match food:

                case "1":
                    money = money + 120
                    print("Popcorn Combo Ordered")

                case "2":
                    money = money + 150
                    print("Burger Combo Ordered")

                case "3":
                    money = money + 250
                    print("Pizza Combo Ordered")

                case "4":
                    money = money + 90
                    print("Cooldrink Ordered")

                case "5":
                    money = money + 110
                    print("Ice Cream Ordered")

                case _:
                    print("Invalid Food")

        case "6":

            print("\n========== BOOKINGS ==========\n")

            if bookings == []:
                print("No Bookings Yet")

            else:

                for b in bookings:

                    print("Ticket ID :", b["id"])
                    print("Name      :", b["name"])
                    print("Movie     :", b["movie"])
                    print("Type      :", b["type"])
                    print("Seat No   :", b["seat"])
                    print("Price     :", b["price"])
                    print("----------------------------")

        case "7":

            search_id = input("Enter Ticket ID: ")

            found = False

            for b in bookings:

                if search_id == str(b["id"]):

                    found = True

                    print("\nTICKET FOUND")
                    print("Name    :", b["name"])
                    print("Movie   :", b["movie"])
                    print("Type    :", b["type"])
                    print("Seat No :", b["seat"])

            if found == False:
                print("Ticket Not Found")

        case "8":

            remove_id = input("Enter Ticket ID To Cancel: ")

            found = False

            for b in bookings:

                if remove_id == str(b["id"]):

                    found = True

                    bookings.remove(b)

                    print("Ticket Cancelled")

            if found == False:
                print("Ticket Not Found")

        case "9":

            print("\nTOTAL COLLECTION =", money)

        case "10":

            print("\nTHANK YOU", user_name)
            print("VISIT AGAIN")
            break

        case _:

            print("Invalid Choice")