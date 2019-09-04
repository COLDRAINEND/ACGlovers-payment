from tkinter import *
from memory_pic import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import tkinter.messagebox
import webbrowser
import base64
import os

root=Tk()
root.title('可怜萝莉在线可爱，给钱就完事了嗷')
root.geometry('800x540')
root.minsize(800,540)
root.maxsize(800,545)


def get_pic(pic_code, pic_name):
    """ BASE64 解码 get image files"""
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

get_pic(diantu_png, 'diantu.png')
get_pic(receivable_png, 'receivable.png')
get_pic(weixin_gif, 'weixin.gif')


def receivable():
    """ 收款时的子窗口 """
    top1=Toplevel()
    top1.title("赶紧给钱")
    image = Image.open('receivable.png') 
    img = ImageTk.PhotoImage(image)
    canvas = Canvas(top1, width = image.width ,height = image.height, bg = 'white')
    canvas.create_image(0,0,image = img,anchor="nw")
    canvas.pack()   
    top1.mainloop()


def open_url(event):
    """ 打开网页 """
    webbrowser.open("https://blog.csdn.net/coldrain_end", new=0)

def show_text():
    """ 查看弹窗 """
    tkinter.messagebox.showwarning('赶紧去扫微信的','欧尼酱～ 呆死ki～～ ..想要微信付款的～～ φ(≧ω≦*)♪')


# -- 封面图片 --------------------------------------------------
img_png = PhotoImage(file = 'diantu.png')
label_img = Label(root, image = img_png)
label_img.pack()
    
# -- 文本 ------------------------------------------------------
ft = tkFont.Font(family="Fixdsys",size=16,weight="bold") 
label_text = Label(root, text = '欧尼酱.....可以...告诉我...你的...支付宝吗..？',font=ft)
label_text.pack()
    
# -- 布局 ------------------------------------------------------
fm1 = Frame()
fm1.pack(side=LEFT, fill=BOTH, expand=YES)

Label(fm1,text='支付宝账号：').place(x=10, y=10)
Entry(fm1).place(x=100, y=10, width=250)

Label(fm1,text='支付宝密码：').place(x=10, y=40)
Entry(fm1).place(x=100, y=40, width=250)

Label(fm1,text='支付密码：').place(x=10, y=70)
Entry(fm1).place(x=100, y=70)

ft0 = tkFont.Font(size=11) 
Button(fm1, text='好的，给你！',height=4,width=18,bg='#ECF5EE',command=show_text).place(x=390, y=10)

img_png2 = PhotoImage(file = 'weixin.gif')
Button(fm1, image=img_png2, relief="groove", bd=2, command=receivable).place(x=590, y=10)

text_url = Label(fm1,text='https://blog.csdn.net/coldrain_end',fg='#739A8F')
text_url.grid(pady=164)
text_url.bind("<Button-1>", open_url)           # 绑定label 触发函数


root.mainloop()
os.remove('diantu.png')
os.remove('receivable.png')
os.remove('weixin.gif')
