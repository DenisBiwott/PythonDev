def myfunction(arg1, *argv):
    print("From arg1:", arg1)


    for arg in argv:
        print ("From *argv:", arg)
myfunction("I", "am", "Biwott")
