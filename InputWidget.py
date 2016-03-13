from PyQt4.QtGui import * 
from PyQt4.QtCore import QPoint, Qt
import math
import struct
import numpy as np

pitches = [32.7,34.6,36.7,38.9,41.2,43.7,46.2,49.0,51.9,55.0,58.3,61.7,
        65.4,69.3,73.4,77.8,82.4,87.3,92.5,98.0,103.8,110.0,116.5,123.5,
        130.8,138.6,146.8,155.6,164.8,174.6,185.0,196.0,207.7,220.0,233.1,246.9,
        261.6,277.2,293.7,311.1,329.6,349.2,370.0,392.0,415.3,440.0,466.2,493.9,
        523.3,554.4,587.3,622.3,659.3,698.5,740.0,784.0,830.6,880.0,932.3,987.8,
        1046.5,1108.7,1174.7,1244.5,1318.5,1396.9,1480.0,1568.0,1661.2,1760.0,1864.7,1975.5,
        2093.0,2217.5,2349.3,2489.0,2637.0,2793.8,2960.0,3136.0,3322.4,3520.0,3729.3,3951.1]

pitches = [math.log(p) for p in pitches]

def closestPitch(p):
    return min(pitches, key=lambda x:abs(x-p))

snap = True


def Blend(img1,img2,op):
    res = QImage(img1)
    r = img1.rect()
    p = QPainter()
    p.begin(res)
    p.drawImage(r,img1)
    p.setOpacity(op)
    p.drawImage(r,img2)
    p.end()
    
    return res
def toGreyScale(img):
    h = img.height()
    w = img.width()
    arr = np.zeros((h,w))
    d = img.depth()/8
    linebytes = w*d
    for i in range(h):
        pxls = img.scanLine(i).asstring(linebytes)
        for j in range(w):
            arr[i][j] = ord(pxls[j*d])
    return arr
        
class InputWidget(QLabel):
    def __init__(self,parent=None):
        QLabel.__init__(self,parent)
        
        self.mainImg = QImage(self.width(),self.height(),QImage.Format_ARGB32)
        self.mainImg.fill(QColor.fromRgb(0,0,0))

        self.topImg = QImage(self.width(),self.height(),QImage.Format_ARGB32)
        self.topImg.fill(QColor.fromRgb(0,0,0,0))
        
        self.brush = QBrush(QColor.fromRgb(255,255,255))
        
        self.pen  = QPen(self.brush,5.0,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin)

        self.offset = QPoint(2,2)
        self.drawing = False
        
        self.srcP = QPoint()

        self.setPixmap(QPixmap.fromImage(self.mainImg))
        self.adjustSize()
        self.setScaledContents(True)
        self.pSnap = True

    def mousePressEvent(self,event):
        self.drawing = True
        self.srcP = event.pos()
        event.accept()

    def mouseReleaseEvent(self,event):
        self.drawing = False

        self.mainImg = Blend(self.mainImg,self.topImg,self.op)
        self.topImg.fill(Qt.transparent)
        
        self.update()
        event.accept()

    def mouseMoveEvent(self,event):
        pt = event.pos()
        if self.pSnap:
            h = self.mainImg.height()
            ratio = h /(pitches[-1]-pitches[0])
            pt.setY(ratio * (closestPitch(pitches[0] + pt.y()/ratio)-pitches[0]))
        #print(pt)
        if(self.drawing):
            #print(pt)
            p = QPainter(self.topImg)
            p.setPen(self.pen)
            p.drawLine(self.srcP+self.offset,pt+self.offset)
            self.srcP = pt
            self.update()
        event.accept()
    def drawGrid(self,p):
        h = self.mainImg.height()
        ratio = h /(pitches[-1]-pitches[0])
        p.setOpacity(1.0)
        for f in pitches: #fundamental pitches
            p.drawLine(0,h-ratio*(f-pitches[0]),self.mainImg.width(),h-ratio*(f-pitches[0]))
        
        pen = QPen(Qt.red)
        pen.setWidth(5)
        p.setPen(pen)
        mC = np.log(261.6)
        p.drawLine(0,h-ratio*(mC-pitches[0]),self.mainImg.width(),h-ratio*(mC-pitches[0]))
        
        pen.setColor(QColor.fromRgb(255,0,0,128))
        pen.setWidth(2)
        p.setPen(pen)
        
        for c in range(0,len(pitches),12):
            p.drawLine(0,h-ratio*(pitches[c]-pitches[0]),self.mainImg.width(),h-ratio*(pitches[c]-pitches[0]))



    def paintEvent(self,event):
        QLabel.paintEvent(self,event)
        p = QPainter(self)
        r = event.rect()
        p.drawImage(self.mainImg.rect(),self.mainImg)
        p.setOpacity(self.op)
        self.drawGrid(p)
        p.drawImage(self.mainImg.rect(),self.topImg)

    def setOp(self,op):
        self.op = op/255.0
        #c = self.brush.color()
        #c.setAlpha(op)
        #self.pen.setColor(c)

    def setSz(self,sz):
        self.pen.setWidth(sz)
        self.offset = QPoint(0,0)

    def setZm(self,zm):
        self.zm = zm
        self.zoom(self.zm)
    def setPSnap(self,pSnap):
        self.pSnap = pSnap

    def resizeEvent(self,event):
        QLabel.resizeEvent(self,event)
        s = event.size()
        #print("REISZE",s)
        w = s.width()
        h = s.height()
        self.mainImg = self.mainImg.scaled(w,h)
        self.topImg = self.topImg.scaled(w,h)

    def zoom(self,s):
        w = s.width()
        h = s.height()
        self.mainImg = self.mainImg.scaled(w,h)
        self.topImg = self.topImg.scaled(w,h)
    def getData(self):
        ratio = self.mainImg.height() /(pitches[-1]-pitches[0])
        return toGreyScale(self.mainImg), ratio


