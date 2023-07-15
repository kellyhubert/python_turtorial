
# if number_friends <= 0:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     friends = {}
#     for _ in range(number_friends):
#         name = input()
#         friends[name] = 0

#     print(friends)

# number_friends= int(input("Enter the number of friends joining (including you):\n"))

# if number_friends <= 0:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     friends = {}
#     for _ in range(number_friends):
#         name = input()
#         friends[name] = 0

#     bill = float(input("Enter the total bill value:\n"))
#     split_bill = round(bill / number_friends, 2)

#     for friend in friends:
#         friends[friend] = split_bill

#     print(friends)
# import random
# number_friends = int(input("Enter the number of friends joining (including you):\n"))
# if number_friends <= 0:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     friends = {}
#     for _ in range(number_friends):
#         name = input()
#         friends[name] = 0

#     bill = float(input("Enter the total bill value:\n"))

#     who_lucky= input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

#     if who_lucky.lower() == "yes":
#         lucky_person = random.choice(list(friends.keys()))
#         print(f"{lucky_person} is the lucky one!")
#     else:
#         print("No one is going to be lucky")

import random

number_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(number_friends):
        name = input()
        friends[name] = 0

    bill = float(input("Enter the total bill value:\n"))
    split_bill = round(bill / number_friends, 2)

    who_lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    if who_lucky.lower() == "yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
        friends[lucky_person] = 0
        remaining_people = number_friends - 1
        adjusted_split_bill = round(bill / remaining_people, 2)
        for friend in friends:
            if friend != lucky_person:
                friends[friend] = adjusted_split_bill
    else:
        print("No one is going to be lucky")
        for friend in friends:
            friends[friend] = split_bill

    print(friends)
    split_amount = round(bill / num_people, 2)

    use_lucky_feature = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    if use_lucky_feature.lower() == "yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
        friends[lucky_person] = 0
        remaining_people = num_people - 1
        adjusted_split_amount = round(bill / remaining_people, 2)
        for friend in friends:
            if friend != lucky_person:
                friends[friend] = adjusted_split_amount
    else:
        print("No one is going to be lucky")
        for friend in friends:
            friends[friend] = split_amount

    print(friends)