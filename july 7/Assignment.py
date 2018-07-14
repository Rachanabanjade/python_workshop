import math


def question_2():

    x = input("Enter First Name :")
    y = input("Enter Last Name :")

    print(x + y, '\n')


question_2()


def no_3():

    x = input("Enter name :")

    print(x*10, '\n')

    print(x,end="**\n")


no_3()


def number_1():

  velocity = "u + a * t"

  print(velocity)

  acceleration = "(v - u) / t"

  print(acceleration)

  v = 25
  u = 0
  t =10

  a = (v-u)/t
  print(a,end=" m/s\n")


number_1()


def builtin():
    x = 5
    print(chr(64))
    print(ascii(1))
    print(chr(ord('A')))
    print(abs(x))
    print(complex())
    lst = [1, 2, 3]
    print(len(lst))
    s = "Python"
    print(len(s))
    lst = [16, 32, 8, 64, 2, 4]
    print(max(lst))
    print(min(lst))
    print(pow(2, 2))


builtin()


