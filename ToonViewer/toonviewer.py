import os
import sys
from tqdm import tqdm
from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType("toonViewer.ui")[0]
class Myview(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path=str()
        self.lst=[]
        self.btn_path.clicked.connect(self.pathsetting)
        self.btn_folder.clicked.connect(self.getfolder)
        self.btn_file.clicked.connect(self.getfile)

    def getfolder(self):
        if self.path=='':
            return
        name=[[] for _ in range(len(self.lst))]
        idx=0
        i=1
        for filename in self.lst:
            if filename.split('[')[-1][0]==str(i):
                i+=1
            else:
                idx+=1
                i=2
            name[idx].append(filename)
        while [] in name:
            name.remove([])
        print(name)
        self.getCurrentItems(name)



    def getfile(self):
        lst=[]
        for i in self.treeWidget.selectedItems():
            lst.append(i.text(0))
        lst.sort(key=len)


    def getCurrentItems(self, name):
        if not os.path.isdir(self.path + "/view/"):
            os.mkdir(self.path+"/view/")

        i=1
        for n in tqdm(name, desc="파일 변환 중..."):
            i+=1
            f = open('%s/%s.html' %(self.path+"/view/", n[0].split('/')[-1].split('.')[0]), 'w')
            a=''
            for k in n:
                path = self.path+'/%s' % k
                a+='<img src=\"%s\" style=\"max-width:100%%\"><br>\n'% path
            f.write('<center>\n%s</center>' % a)
            f.close()
        f = open('%s/%s.html' % (self.path, 'VIEWER'), 'w')
        f.write('<body>\n<h1>\n        <a href="view/">CLICK HERE</a>\n    </h1>\n</body>')
        print("완료!")

    def pathsetting(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file != '':
            self.treeWidget.clear()
            self.path=file
            self.lst=[]
            self.load(self.path, self.treeWidget)

    def load(self, startpath, tree):
        self.lst.extend(os.listdir(startpath))
        self.lst.sort(key=len)
        name=[]

        for filename in self.lst:
            if filename.split('.')[-1].lower() in  ['jpg', 'png', 'jpeg']:
                name.append(filename)

        self.lst=name
        for element in self.lst:
            path_info = startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                self.load(path_info, parent_itm)

if __name__ == '__main__':
    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    myview = Myview()
    myview.show()
    sys.exit(app.exec_())
