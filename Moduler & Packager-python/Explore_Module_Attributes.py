def Explore_Module_Attributes():
    print("=" * 30)
    modul=input("Enter module name to explore:-")
    module=__import__(modul)
    Attri=dir(module)
    print(f"Available Attributes in {modul} module: {Attri}")
    print("=" * 30)
def main():
    Explore_Module_Attributes()
if __name__ == "__main__":
    main()




