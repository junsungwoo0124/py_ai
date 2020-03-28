#숫자 판독 앱

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy

#이미지 파일을 수치 리스트로 변환

def imageToData(filename):
    #이미지를 8x8의 그레이스 케일로 변환
    greyImage = PIL.Image.open(filename).convert('L')
    greyImage = greyImage.resize((8,8), PIL.Image.ANTIALIAS)
    #해당 이미지를 표시한다
    dispImage = PIL.ImageTk.PhotoImage(greyImage.resize((300,300)))
    imageLable.configure(image = dispImage)
    imageLable.image = dispImage
    #수치 리스트 변환
    numImage = numpy.asarray(greyImage, dtype=float)
    numImage = numpy.floor(16-16*(numImage/256))
    numImage = numImage.flatten()
    return numImage

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        print("파일 경로: ", fpath)
        data = imageToData(fpath)
        print(data)
        predictDigits(data)

def predictDigits(data):
    # 학습용 데이터를 읽어온다
    digits = sklearn.datasets.load_digits()
    # 머신러닝하기
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    # 예측결과 표시
    n = clf.predict([data])
    textLabel.configure(text = "이 그림은 %d입니다"%n)

#앱 창 만들기
root = tk.Tk()
root.geometry("400x400")

#버튼, 레이블 생성하기
btn = tk.Button(root, text = '파일 열기', command = openFile)
imageLable = tk.Label()
textLabel = tk.Label()

#버튼, 레이블 화면에 출력하기
btn.pack()
imageLable.pack()
textLabel.pack()

#칭 실행하기
tk.mainloop()