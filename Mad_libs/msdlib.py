def mad_libs():
    
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    food = input("Enter a food item: ")

    
    story = f"""
    One day, {name} went to {place} for an adventure. 
    Suddenly, a {adjective} {animal} appeared and started to {verb} wildly! 
    {name} was so surprised that they dropped their {food} on the ground.
    It was the most unexpected day ever!
    """

  
    print("\nHere's your Mad Libs story! \n")
    print(story)


mad_libs()
