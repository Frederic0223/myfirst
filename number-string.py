#數字運算
x=3+6
print(x)
x=3-6
print(x)
#you can use +_*小數除法"/" 整數除法=“//”
x=7/6
print(x)
y=7//6
print(y)
#x的y次方
z=x**y
print(z)
#取餘數
p=7%3
print(p)
x=2+3
print(x)
x=x+1 #相當於x+=1將變數這個數字+1
#同理有x-=1, x*=1將變數*1
print(x)

#string 
s="hello"+"world" #''="" 如果雙引號裏要輸出雙引號，可以寫;字串可以用+或空格串接
s="hello" "world"
d="hell\"0" #這裏面的\叫跳脫，可以保留雙引號在string裏
print(s,d)
#"\n"換行
a="hello\nworld"
#或者三個雙引號直接換行，比如
b="""hello
world"""
print(a)
print(b)
#文字重複*次數
a="hello"*3
#string每個字都有編號（索引），比如hello有01234
s="hello"
print(s[2])
#或者選取1-3的索引 包含開頭不包含結尾
print(s[1:4])
#也可以不寫結尾，從開頭算起取全部；只給結尾不給開頭也可
print(s[1:])
print(s[:4])