def f(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


f(100 , txt=50, new=25)