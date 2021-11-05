def f():
    email=input("enter email: ")
    if "@" in email and "." in email:
        print("valid")
    else:
        print("not valid")
f()