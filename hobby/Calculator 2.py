# 계산기 만들기

from tkinter import *

def click(key):
    if key == '=':
        try:
            result = eval(entry1.get())
            entry1.delete(0, END)
            entry1.insert(END, str(result))
        except:
            entry1.insert(END, '다시 시도!')
    elif key == 'clear':
        entry1.delete(0, END)
    else:
        entry1.insert(END, key)

calculator = Tk()
calculator.title('한승훈의 미천한 계산기')


#첫번쨰 행(clear, +)
btn_clear = Button(calculator, text='clear', command=lambda x = 'clear' : click(x))
btn_nil = Button(calculator, text=' ')
btn_nil2 = Button(calculator, text=' ')
btn_plus = Button(calculator, text='+', command=lambda x = '+' : click(x))

btn_clear.grid(row=1, column=0)
btn_nil.grid(row=1, column=1)
btn_nil2.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)

#두번째 행(7,8,9,-)
btn_seven = Button(calculator, text='7', command=lambda x = '7' : click(x))
btn_eight = Button(calculator, text='8', command=lambda x = '8' : click(x))
btn_nine = Button(calculator, text='9', command=lambda x = '9' : click(x))
btn_minus = Button(calculator, text='-', command=lambda x = '-' : click(x))

btn_seven.grid(row=2, column= 0)
btn_eight.grid(row=2, column= 1)
btn_nine.grid(row=2, column= 2)
btn_minus.grid(row=2, column= 3)

#세번째 행(4,5,6,*)
btn_four = Button(calculator, text='4', command=lambda x = '4' : click(x))
btn_five = Button(calculator, text='5', command=lambda x = '5' : click(x))
btn_six = Button(calculator, text='6', command=lambda x = '6' : click(x))
btn_mul = Button(calculator, text='*', command=lambda x = '*' : click(x))

btn_four.grid(row=3, column= 0)
btn_five.grid(row=3, column= 1)
btn_six.grid(row=3, column= 2)
btn_mul.grid(row=3, column= 3)

#네번째 행(1,2,3,/)
btn_one = Button(calculator, text='1', command=lambda x = '1' : click(x))
btn_two = Button(calculator, text='2', command=lambda x = '2' : click(x))
btn_three = Button(calculator, text='3', command=lambda x = '3' : click(x))
btn_div = Button(calculator, text='/', command=lambda x = '/' : click(x))

btn_one.grid(row=4, column= 0)
btn_two.grid(row=4, column= 1)
btn_three.grid(row=4, column= 2)
btn_div.grid(row=4, column= 3)

#마지막 행(0,=)
btn_nil3 = Button(calculator, text=' ')
btn_zero = Button(calculator, text='0', command=lambda x = '0' : click(x))
btn_point = Button(calculator, text='.', command=lambda x = '.' : click(x))
btn_enter = Button(calculator, text='=', command=lambda x = '=' : click(x))

btn_nil3.grid(row=5, column= 0)
btn_zero.grid(row=5, column= 1)
btn_point.grid(row=5, column= 2)
btn_enter.grid(row=5, column= 3)

#입력
entry1= Entry(calculator)
entry1.grid(row=0, column=0, columnspan=5)


calculator.mainloop()