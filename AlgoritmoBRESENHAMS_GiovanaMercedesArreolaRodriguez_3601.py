import matplotlib.pyplot as plt

def bresenhams(x1, y1, x2, y2, color):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    p = 2*dy - dx

    x = x1
    y = y1

    for i in range(x, x2):
        plt.plot(round(x), round(y), color, color="red")
        x += x
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + (2*dy) - (2*dx)
            y += y 
 
        print("Valor en X:", x)
        print("Valor en Y:", y)
    plt.title("Algoritmo Bresenhams")
    plt.ylabel("Eje y")
    plt.xlabel("Eje x")
    plt.grid()
    plt.show()
    

def main():
    x1 = int(input("Ingresa el valor para x1: "))
    y1 = int(input("Ingresa el valor para y1: "))
    x2 = int(input("Ingresa el valor para x2: "))
    y2 = int(input("Ingresa el valor para y2: "))    
    color = "b."


    bresenhams(x1, y1, x2, y2, color)

if __name__ == "__main__":
    main()    
    