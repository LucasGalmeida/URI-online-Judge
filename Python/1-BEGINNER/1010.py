CODE1, N1, P1 = input().split()
CODE1 = int(CODE1)
N1 = int(N1)
P1 = float(P1)

CODE2, N2, P2 = input().split()
CODE2 = int(CODE2)
N2 = int(N2)
P2 = float(P2)

print("VALOR A PAGAR: R$ {:.2f}".format(N1 * P1 + N2 * P2))

