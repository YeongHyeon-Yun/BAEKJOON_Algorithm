# A = int(input("A :: "))
# print(type(A), A)
#
# B = int(input("B :: "))
# print(type(B), B)

A, B = map(float, input().split("and"))


def arithmetic_operation(A, B):
    print(A + B, A - B, A * B, int(A / B), A % B, sep="\n")


arithmetic_operation(A, B)
