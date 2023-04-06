#597개 동작시간이 너무 오래걸려서, csv 파일에 예측값 저장
import csv 

predict = ["23423","dsfsf","egwrgw","erwee"]
with open("test_list.csv",'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(predict)