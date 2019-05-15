from layouts.Window import Window

if __name__ == "__main__":
    try:
        root = Window()
        root.run()
    except:
        print("Create main window failed!!!")

