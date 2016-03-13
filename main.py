#/usr/bin/python2.7
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import numpy as np
import sys
import pyaudio
from matplotlib import pyplot as plt

from mainUI import Ui_MainWindow


p = pyaudio.PyAudio()

class ComposerMain(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.setWindowTitle("Composer")
        self.opSlider.valueChanged.connect(self.changeOp)
        self.szSlider.valueChanged.connect(self.changeSz)
        self.horzZmSlider.valueChanged.connect(self.changeZm)
        self.vertZmSlider.valueChanged.connect(self.changeZm)

        self.playBtn.clicked.connect(self.play)
        
        self.changeOp(self.opSlider.value())
        self.changeSz(self.szSlider.value())

    def changeOp(self,op):
        self.inputWidget.setOp(op)
    def updateCursor(self,sz):
        img = QImage(sz+1,sz+1,QImage.Format_ARGB32)
        img.fill(qRgba(0,0,0,0))
        
        p = QPainter()
        pen = QPen(QColor.fromRgbF(1.0,0.2,0.2,0.5))
        p.begin(img)
        p.setPen(pen)
        p.drawEllipse(0,0,sz,sz)
        p.drawPoint(sz/2,sz/2)
        p.end()
        
        c = QCursor(QPixmap.fromImage(img),hotX=sz/2,hotY=sz/2)
        QApplication.setOverrideCursor(c)
    def changeSz(self,sz):
        self.inputWidget.setSz(sz)
        self.updateCursor(sz)

    def resizeEvent(self,event):
        QMainWindow.resizeEvent(self,event)
        self.changeZm()

    def changeZm(self):
        hzm = self.horzZmSlider.value()/100.0
        vzm = self.vertZmSlider.value()/100.0
        s = self.scrollArea.size()
        
        s.setWidth(s.width() * hzm)
        s.setHeight(s.height() * vzm)

        self.scrollAreaWidgetContents.resize(s)
        self.inputWidget.resize(s)
        self.inputWidget.setZm(s)
        self.update()

    def play(self,event):
        rate = 44100 #how long each pixel would last.
        pps = self.ppsSpin.value()
        spp = 44100/pps
        arr,ratio = self.inputWidget.getData()
        h = arr.shape[0]
        w = arr.shape[1]
        #print("RATIO", ratio)
        stream = p.open(format=p.get_format_from_width(1),channels=1,rate=44100,output=True) #44100 Hz
        sound = np.asarray([],dtype=np.uint8)
        #maxes = []
        for j in range(w): #change here to w later.
            #mymax = 0
            #argmax = 0
            print(j)
            sig_jw = reversed(arr[:,j])
            sig = np.zeros(44100,dtype=np.uint8) #signal
            for i,s in enumerate(sig_jw):
                hz = int(np.exp(3.487 + i/ratio))
                sig[hz] = s
                sig[22050+hz] = -s
                #if s>mymax:
                #    argmax = hz 
                #    mymax = s
            #maxes += [argmax]

            #print(np.where(sig!=0))
            s = np.fft.ifft(sig,n=44100,norm="ortho")
            s = s.astype(np.uint8)
            sound = np.concatenate((sound,s[:spp]))
            stream.write(s[:spp])
            #stream.stop_stream()
            #stream.close()
            #plt.plot(arr[:,j])
            #plt.plot(sig)
            #plt.plot(s)
            #plt.show()
        stream.write(sound)
        #plt.plot(maxes)
        #plt.show()

        print(w)
        stream.stop_stream()
        stream.close()





def main():
    global app;
    app = QApplication(sys.argv)
    w = ComposerMain()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
