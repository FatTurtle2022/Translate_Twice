import tkinter as tk
import baidu_translate as fanyi
import pyperclip
from tkinter import messagebox

window = tk.Tk()
window.title('肥胖龟多次翻译')
window.geometry('400x175')

def text():
    print("此功能制作中")

output_var = '此功能制作中'

input_text = tk.Label(window,text='翻译内容:',width=10,height=2,bg='white', font=('Arial,12'))
input_text.place(x=0,y=0)

input_Entry = tk.Entry(window,show=None)
input_Entry.place(x=87,y=0,width=310,height=35)

language_var_natural = '英语'

now_language = tk.StringVar()
now_language.set('目前语言：英语')

language_nature_list_var = ['简体中文','英语','粤语','文言文','日语','韩语','法语','西班牙语','泰语','阿拉伯语','俄语','葡萄牙语','德语','意大利语','希腊语','荷兰语','波兰语','保加利亚语','爱沙尼亚语','丹麦语','芬兰语','捷克语','罗马尼亚语','斯洛文尼亚语','瑞典语','匈牙利语','繁体中文','越南语']

language_abb_list_var = ['ZH','EN','YUE','WYW','JP','KOR','FRA','SPA','TH','ARA','RU','PT','DE','IT','EL','NL','PL','BUL','EST','DAN','FIN','CS','ROM','SLO','SWE','HU','CHT','VIE']

def language_def():
    global language_var_natural

    language_window = tk.Toplevel(window)
    language_window.title('选择语言')
    language_window.geometry('200x500')

    now_language_text = tk.Label(language_window, textvariable=now_language, bg='white', font=('Arial,12'), width=25, height=2)
    now_language_text.place(x=0,y=0)

    language_list = tk.StringVar()
    language_list.set(('简体中文','英语','粤语','文言文','日语','韩语','法语','西班牙语','泰语','阿拉伯语','俄语','葡萄牙语','德语','意大利语','希腊语','荷兰语','波兰语','保加利亚语','爱沙尼亚语','丹麦语','芬兰语','捷克语','罗马尼亚语','斯洛文尼亚语','瑞典语','匈牙利语','繁体中文','越南语'))
    language_listbox = tk.Listbox(language_window,listvariable=language_list,height=22)
    language_listbox.place(x=0,y=45)

    def apply_def():
        global language_var_natural
        language_var_natural = language_listbox.get(language_listbox.curselection())
        now_language.set('目前语言：'+(language_var_natural))

    apply_Button = tk.Button(language_window,text='应用', width=13, height=2, command=apply_def)
    apply_Button.place(x=0, y=452)

    def confirm_def():
        language_window.destroy()

    confirm_Button = tk.Button(language_window,text='确定', width=13, height=2, command=confirm_def)
    confirm_Button.place(x=100, y=452)

language_Button = tk.Button(window,text='选择语言', width=27, height=2, command=language_def)
language_Button.place(x=0, y=40)

input_var = str(input_Entry.get())
language_var = str('EN')

now_language_var = 'en'
now_language_number = 6
result = '无输入内容'

def translate_def():
    global input_var
    global language_var
    global language_var_natural
    global now_language_var
    global result
    input_var = str(input_Entry.get())
    now_language_var = language_nature_list_var.index(language_var_natural)
    now_language = language_abb_list_var[int(now_language_var)]
    result = fanyi.translate_text((input_var), to=(fanyi.Lang[now_language]))
    output_Entry.delete(0,'end')
    output_Entry.insert(0,str(result))
    print(result)
    ori_language = fanyi.detect_language(input_var)
    print(ori_language)
    result_twice = fanyi.translate_text((result), to=ori_language)
    print(result_twice)
    output_twice_Entry.delete(0,'end')
    output_twice_Entry.insert(0,str(result_twice))

translate_Button = tk.Button(window,text='翻译', width=27, height=2, command=translate_def)
translate_Button.place(x=200, y=40)

#output_text = tk.Label(window,text=output_var,width=50,height=2,bg='white', font=('Arial,12'))
#output_text.place(x=0,y=120)

output_Entry = tk.Entry(window,show=None)
output_Entry.place(x=0,y=90,width=350,height=35)

def copy_def():
    pyperclip.copy(result)
    yes_copy = messagebox.showinfo(title="已复制", message="已复制")

copy = tk.Button(window,text='复制',command=copy_def,width=6,height=2)
copy.place(x=350, y=90)

output_twice_Entry = tk.Entry(window,show=None)
output_twice_Entry.place(x=0,y=130,width=400,height=35)

window.mainloop()