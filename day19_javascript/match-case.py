animal = "cat"
match animal:
    case "dog": print("Bark")  
    case "cat": print("Meow")
    case "bird": print("Tweet")
    case _ : print("Unknown animal")