#숫자 판독 앱

import tkinter as tk
import tkinter.filedialog as fd
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        print("파일 경로: ", fpath)


#앱 창 만들기
root = tk.Tk()
root.geometry("400x400")

#버튼, 레이블 생성하기
btn = tk.Button(root, text = '파일 열기', command = openFile)
imageLable = tk.Label()

#버튼, 레이블 화면에 출력하기
btn.pack()
imageLable.pack()

#칭 실행하기
tk.mainloop()
