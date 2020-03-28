#숫자 예측하기
#preddictDigits.py

import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

#이미지 파일을 수치 리스트로 변환하기
def imageToData(filename):
    #이미지를 8x8의 그레이스케일로 변환
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.ANTIALIAS)

    #수치리스트로 변환
    numImage = numpy.asarray(grayImage, dtype=float)
    numImage = numpy.floor(16-16*(numImage/256))
    numImage = numImage.flatten()

    return numImage
#숫자 예측하기
def predictDigits(data):
    #학습용 데이터 불러오기
    digits = sklearn.datasets.load_digits()
    #머신러닝 실행
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    #예측결과 표시하기
    n = clf.predict([data])
    print("예측값: ", n)

#이미지 파일 수치 리스트로 변환하기
data = imageToData("4.png")
print(data)
#숫자 예측하기
predictDigits(data)
