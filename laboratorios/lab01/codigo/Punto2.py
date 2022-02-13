
class Bipartite_Graph:
    def setCreation(list):
        blue = []
        red = []
        if (list[-1] == 2):
            return "Bicolorable"
        for i in range(len(list[0])):
            if not (list[0][i][0] in red) :
                blue.append(list[0][i][0])
                if (list[0][i][1] in blue):
                    return "Not Bicorolable"
                else:
                    red.append(list[0][i][1])
            if not (list[0][i][0] in blue):
                red.append(list[0][i][0])
                if (list[0][i][1] in red):
                    return "Not Bicorolable"
                else:
                    blue.append(list[0][i][1])
        return "Bicolorable"

    def input():
        while True:
            g = Bipartite_Graph
            list = []
            print("Digite el numero de nodos")
            numNodos = int(input())
            if numNodos == 0:
                return
            print("Digite el numero de arcos")
            numArcos = int(input())
            for j in range(numArcos):
                print("Digite arco")
                arcos = input()
                num1 = int(arcos[ :arcos.find(" ")])
                num2 = int(arcos[arcos.find(" ") + 1: ])
                list.append((num1, num2))
            print()
            print(g.setCreation((list,numNodos)))
            print("--------------------------")
    
    

def main():
    g = Bipartite_Graph
    g.input()
    

main()