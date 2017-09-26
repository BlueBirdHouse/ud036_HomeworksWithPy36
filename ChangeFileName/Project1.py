import webbrowser
import time
import os

#首先自动打开浏览器
#time.sleep(3)
#webbrowser.open('http://www.ifeng.com/')

#然后遍历一个文件夹里面的文件
LocalDir = os.getcwd()
FigDir = LocalDir + "\Figs"
os.chdir(FigDir)
FileNames = os.listdir(FigDir)
for AFileName in FileNames:
    NewName = AFileName.replace('IMG_','')
    os.rename(AFileName,NewName)
#还原系统路径
os.chdir(LocalDir)

 