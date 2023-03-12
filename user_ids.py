#when we use two '**' in python we can pass multiple keyword arguments to a function
# and python will automatically package them into a dictionary
  
def save_user(**user):
    # we use print (user["keyword"]) to searach keyword you want
    print(user['id'])
    print(user["age"])

save_user(id=103, name="kelly", age=24)