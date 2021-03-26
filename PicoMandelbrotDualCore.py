# Mandelbrot Pico in MicroPython with Zoom - by Hari Wiguna, 2021
# Math courtesy of:
# https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/mandelbrot-set

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import framebuf
import time
import _thread
import gc

#-- Parameters --
WIDTH, HEIGHT = 128, 64
width2 = int(WIDTH/2)
height2 = int(HEIGHT/2)

realStart, realEnd = -2-1, 2
imStart, imEnd = -1,1
MAX_ITER = 25 # orig 80, 30 crashes

results = [False] * HEIGHT #One column of the display. Initialize thread result to all off
resultsReady=False

def mandelbrot(c):
    global MAX_ITER
    z,n = 0,0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def mandelbrotThreadY(y):
    global MAX_ITER
    global WIDTH, HEIGHT, realStart, realEnd, imStart, imEnd
    global results, resultsReady
    #print("Thread Begin y=",y)
    yy = imStart + (y / HEIGHT) * (imEnd - imStart)
    for x in range(WIDTH):
        results[x]=False
    for x in range(WIDTH):
        xx = realStart + (x / WIDTH) * (realEnd - realStart)
        c = complex(xx, yy) # Convert pixel coordinate to complex number
        m = mandelbrot(c)   # Compute the number of iterations
        color = 1 - int(m/MAX_ITER)
        results[x] = color>0
    resultsReady = True
    #print("Thread Done x", y)
    _thread.exit() # when done, commit suicide so we could be re-incarnated for next X.

def DrawMandelbrotY():
    global oled, brotFB, cursorFB, isHiRez, nextRefresh, MAX_ITER
    global results, resultsReady
    #print("DRAWINGY:", realStart, realEnd, imStart, imEnd)
    stopWatch = time.ticks_ms()
    RE_START = realStart
    RE_END = realEnd
    IM_START = imStart
    IM_END = imEnd

    #brotFB.fill(0)
    
    for y in range(0, HEIGHT, 2):
        if gc.mem_free() < 10000:
            gc.collect()
        print("mem free=",gc.mem_free())
        print("y=",y)
        resultsReady=False # Will be set by thread to True when it's done computing row.
        _thread.start_new_thread(mandelbrotThreadY,(y,))
        
        y1 = y+1
        #print("Main begin y1=",y1)
        yy = IM_START + (y1 / HEIGHT) * (IM_END - IM_START)
        for x in range(WIDTH): # We're drawing two rows at a time. One by the thread, the other by main.
            xx = RE_START + (x / WIDTH) * (RE_END - RE_START)
            c = complex(xx, yy) # Convert pixel coordinate to complex number
            m = mandelbrot(c)   # Compute the number of iterations
            color = 1 - int(m/MAX_ITER)
            brotFB.pixel(x,y1, 1 if color>0 else 0) # Plot the point
        #print("Main End x1=",x1)
                   
        stopwatchStart = time.ticks_ms()
        #print("Waiting...")
        while not resultsReady:
            pass
        #print("waited ", time.ticks_ms()-stopwatchStart, "ms")
        
        # Plot the X column computed by the thread
        for x in range(WIDTH):
            brotFB.pixel(x,y, 1 if results[x] else 0)

        if y % 4 == 0: # No need to refresh everytime we go through X loop.
            oled.blit(brotFB,0,0)
            oled.show()

    oled.blit(brotFB,0,0)
    oled.show()


def mandelbrotThreadX(x):
    global MAX_ITER
    global WIDTH, HEIGHT, realStart, realEnd, imStart, imEnd
    global results, resultsReady
    #print("Thread Begin x=",x)
    xx = realStart + (x / WIDTH) * (realEnd - realStart)
    for y in range(HEIGHT):
        results[y]=False
    for y in range(HEIGHT):
        yy = imStart + (y / HEIGHT) * (imEnd - imStart)
        c = complex(xx, yy) # Convert pixel coordinate to complex number
        m = mandelbrot(c)   # Compute the number of iterations
        color = 1 - int(m/MAX_ITER)
        results[y] = color>0
    resultsReady = True
    #print("Thread Done x", x)
    _thread.exit() # when done, commit suicide so we could be re-incarnated for next X.

def DrawMandelbrotX():
    global oled, brotFB, cursorFB, isHiRez, nextRefresh, MAX_ITER
    global results, resultsReady
    print("DRAWING:", realStart, realEnd, imStart, imEnd)
    stopWatch = time.ticks_ms()
    RE_START = realStart
    RE_END = realEnd
    IM_START = imStart
    IM_END = imEnd

    brotFB.fill(0)
    
    for x in range(0, WIDTH,2): # We're drawing two columns at a time. One by the thread, the other by main.
        resultsReady=False # Will be set by thread to True when it's done computing column.
        _thread.start_new_thread(mandelbrotThreadX,(x,))
        
        x1 = x+1
        #print("Main begin x1=",x1)
        xx = RE_START + (x1 / WIDTH) * (RE_END - RE_START)
        for y in range(0, HEIGHT, 1):
            yy = IM_START + (y / HEIGHT) * (IM_END - IM_START)
            c = complex(xx, yy) # Convert pixel coordinate to complex number
            m = mandelbrot(c)   # Compute the number of iterations
            color = 1 - int(m/MAX_ITER)
            brotFB.pixel(x1,y, 1 if color>0 else 0) # Plot the point
        #print("Main End x1=",x1)
                   
        #stopwatchStart = time.ticks_ms()
        while not resultsReady:
            pass
        #print("waited ", time.ticks_ms()-stopwatchStart, "ms")
        
        # Plot the X column computed by the thread
        for y in range(HEIGHT):
            brotFB.pixel(x,y, 1 if results[y] else 0)

        if x % 6 == 0: # No need to refresh everytime we go through X loop.
            oled.blit(brotFB,0,0)
            oled.show()

    oled.blit(brotFB,0,0)
    oled.show()

def SetupDisplay():
    global oled
    i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    
def SetupFB():
    global brotBitmap, brotFB, cursorFB

    #-- Mandelbrot canvas --
    brotBitmap=bytearray(int(WIDTH*HEIGHT/8))
    brotFB=framebuf.FrameBuffer(brotBitmap, WIDTH,HEIGHT, framebuf.MVLSB)
    
    #-- Cursor --
    cursorBitmap=bytearray(int(WIDTH*HEIGHT/8))
    cursorFB = framebuf.FrameBuffer(cursorBitmap, WIDTH,HEIGHT, framebuf.MVLSB)
    cursorFB.line(0,0, WIDTH, HEIGHT, 1)  

def SetupUI():
    global mPot0, mPot1, mZoomPot
    global buttonZoomIn, buttonZoomOut, buttonCenter, buttonRez
    
    #-- Setup UI --
    mPot0 = ADC(26)
    mPot1 = ADC(27)
    mZoomPot = ADC(28)
    
    buttonZoomIn = Pin(13, Pin.IN, Pin.PULL_UP)
    buttonZoomOut = Pin(14, Pin.IN, Pin.PULL_UP)
    buttonCenter = Pin(15, Pin.IN, Pin.PULL_UP)
    buttonRez = Pin(12, Pin.IN, Pin.PULL_UP)

def Setup():
    global oled, brotFB, cursorFB, threadState
    SetupDisplay()
    SetupFB()
    SetupUI()

def get_pixel(buffer, x,y):
    yy = y % 8
    return 1 if (buffer[x+WIDTH*int(y/8)] & (1<<yy)) > 0 else 0
    
def _map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def getCursorX(pot):
    return int(_map(pot.read_u16(), 0, 65520, 0, WIDTH))

def getCursorY(pot):
    return int(_map(pot.read_u16(),0, 65520, 0, HEIGHT))

def getZoomLevel(pot):
    return int(_map(pot.read_u16(), 0, 65520, 0, HEIGHT))

def MoveCursor():
    global nextSensorRead
    global oled, brotFB, cursorFB
    if time.ticks_ms() >= nextSensorRead:          
        x0 = getCursorX(mPot0)
        y0 = getCursorY(mPot1)
        z = getZoomLevel(mZoomPot)
        newHeight = int(z/2)
        newWidth = int((z*WIDTH/HEIGHT)/2)
        left, right = x0-newWidth, x0+newWidth
        top, bottom = y0-newHeight, y0+newHeight
        
        cursorFB.blit(brotFB,0,0)
        cursorFB.line(left,top, right,top, 0) # Top Line
        cursorFB.line(left,top, left, bottom, 0) # Left Line
        cursorFB.line(right,top, right, bottom, 0) # Right Line
        cursorFB.line(left,bottom, right, bottom, 0) # Bottom Line
        oled.blit(cursorFB,0,0)
        oled.show()
        
        nextSensorRead = time.ticks_ms() + 100

def ZoomIn():
    global mPot0, mPot1, mZoomPot
    global oled, brotFB, cursorFB
    global buttonZoomIn, buttonZoomOut, buttonCenter
    global realStart, realEnd, imStart, imEnd #???????????????????

    pressed = buttonZoomIn.value() == False
    if pressed:
        print("BEFORE ZOOM IN:", realStart, realEnd, imStart, imEnd)
        x0 = getCursorX(mPot0)
        y0 = getCursorY(mPot1)
        z = getZoomLevel(mZoomPot)
        newHeight = int(z/2)
        newWidth = int((z*WIDTH/HEIGHT)/2)
        print(z, newWidth, newHeight)
        left, right = x0-newWidth, x0+newWidth
        top, bottom = y0-newHeight, y0+newHeight
        realRange = realEnd-realStart
        imRange = imEnd-imStart
        realStart = realStart + (realRange*left/WIDTH)
        realEnd = realStart + (right-left)*realRange/WIDTH
        imStart = imStart + (imRange*top/HEIGHT)
        imEnd = imStart + (bottom-top)*imRange/HEIGHT
        print("AFTER:",realStart, realEnd, imStart, imEnd)
        time.sleep_ms(500) # Allow human to release button
    return pressed

def ZoomOut():
    global realStart, realEnd, imStart, imEnd #???????????????????
    pressed = buttonZoomOut.value() == False
    if pressed:
        print("BEFORE ZOOM OUT:",realStart, realEnd, imStart, imEnd)
        zoomDelta = 2
        realRange, imRange = realEnd-realStart, imEnd-imStart
        realDelta, imDelta = realRange/zoomDelta, imRange/zoomDelta
        left, right = realStart-realDelta, realEnd+realDelta
        top, bottom = imStart-imDelta, imEnd+imDelta
        realStart = left
        realEnd = right
        imStart = top
        imEnd = bottom
        print("AFTER:",realStart, realEnd, imStart, imEnd)
        time.sleep_ms(500) # Allow human to release button
    return pressed

def ChangeRez():
    global buttonRez, isHiRez
    pressed = buttonRez.value()== False
    if pressed:
        isHiRez = not isHiRez
        print("isHiRez=", isHiRez)
        time.sleep_ms(500) # Allow human to release button
    return pressed

def ButtonPressed():
#     MoveCursor()
    pressed = ChangeRez() or Center() or ZoomIn() or ZoomOut()
    return pressed

def Center():
    global mPot0, mPot1
    global realStart, realEnd, imStart, imEnd #???????????????????

    pressed = buttonCenter.value() == False
    if pressed:
        print("BEFORE CENTER:",realStart, realEnd, imStart, imEnd)
        realRange, imRange  = realEnd-realStart, imEnd-imStart
        print("Ranges:",realRange, imRange)
        width2, height2 = WIDTH/2, HEIGHT/2
        xDelta = getCursorX(mPot0) - width2
        yDelta = getCursorY(mPot1) - height2
        print("Cursors:",getCursorX(mPot0) , getCursorY(mPot1) )
        print("Screen Deltas:",xDelta, yDelta)
        realDelta, imDelta = (realRange*xDelta/WIDTH), (imRange*yDelta/HEIGHT)
        print("Mandel Deltas:",realDelta, imDelta)
        realStart = realStart + realDelta
        realEnd = realEnd + realDelta
        imStart = imStart + imDelta
        imEnd = imEnd + imDelta
        print("AFTER:",realStart, realEnd, imStart, imEnd)
    return pressed

def Loop():
    global mPot0, mPot1, mZoomPot
    global oled, brotFB, cursorFB
    global buttonZoomIn, buttonZoomOut, buttonCenter
    global nextSensorRead, nextRefresh, lastX0, lastY0
    global isHiRez
    
    isHiRez = False
    nextSensorRead, nextRefresh =-1,-1
    lastX0, lastY0 = -1024,-1024

    while True:
        DrawMandelbrotX()
        while not ButtonPressed():
            MoveCursor()

def main():
    Setup()
    Loop()
