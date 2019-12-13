t = list(map(float, input("Введіть через пробіл 8 координат вершин чотирикутника в такій \n послідовності : Xa Ya Xb Yb Xc Yc Xd Yd :  ").split()))

[Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd]=t

Xab=Xb-Xa
Yab=Yb-Ya

Xad=Xd-Xa
Yad=Yd-Ya

Xcb=Xb-Xc
Ycb=Yb-Yc

Xcd=Xd-Xc
Ycd=Yd-Yc

S=0.5*(abs(Xab*Yad-Yab*Xad)+abs(Xcb*Ycd-Ycb*Xcd))
print("\n")
print("Площа чотирикутника ABCD дорівнює ", round(S, 3))