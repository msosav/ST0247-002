def lcsAux(A: str,B: str,i: int,j: int)-> int:
    if(i == len(A) or j == len(B)):
        return 0
    elif A[i] == B[j]:
        return 1 + lcsAux(A,B,i+1,j+1)
    else:
        return max(lcsAux(A,B,i+1,j), lcsAux(A,B,i,j+1))

def lcs(A: str, B: str)-> int:
    return lcsAux(A,B,0,0)

def main():
    print(lcs("sergio","miguel"))
main()