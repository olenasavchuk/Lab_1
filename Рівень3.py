print("Нуль в якості знаку операції завершить програму")
while True:
    s = input("Знак (+,-,/,*): ")
    if s == '0': break
    if s in ('+','-','/','*'):
        a = int(input("a="))
        b = int(input("b="))
        if s == '+':
            print("%.i" % (a+b))
        elif s == '-':
            print("%.i" % (a-b))
        elif s == '*':
            print("%.i" % (a*b))
        elif s == '/':
            if b != 0:
                print("%.i" % (a/b))
            else:
                print("Ділення на нуль!")
    else:
        print("Невірний знак операції!")
