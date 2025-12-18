print(" *** Number Fun !!! ***")
a,b = input("Enter a b : ").split()
print("a=",a,"\ttype =",type(a))
print("b=",b,"\ttype =",type(b))
print("a+b =>",a,"+",b,"=>",a+b)
# convert a to int
a = int(a)
# convert b to int
b = int(b)
# แสดงผล a/b ทศนิยม 2 ตำแหน่ง
print("a/b =", "{:.2f}".format(a/b))
# แสดงผล b/a ทศนิยม 3 ตำแหน่ง
print("b/a =", "{:.3f}".format(b/a))
# แสดงผลการหารแบบเหลือเศษของ a และ b
print("a/b =", "{:.0f}".format(a//b), "r", a%b)
# แสดงผลการหารแบบเหลือเศษของ b และ a
print("b/a =", "{:.0f}".format(b//a), "r", b%a)