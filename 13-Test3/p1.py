def f(n):
    output = ""
    for i in range(n):
        if i%5 != 0 or i==0:
            output += "/"
        else:
            output += "-/"
    return output

def main():
    print(f(5) == "/////")
    print(f(7) == "/////-//")
    print(f(10) == "/////-/////")
    print(f(11) == "/////-/////-/")
    print(f(15) == "/////-/////-/////")
    print(f(16) == "/////-/////-/////-/")

if __name__ == "__main__":
    main()
