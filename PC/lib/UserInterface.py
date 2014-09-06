import Tkinter
import Algorithm

class UI :
    def __init__(self, cube = None, camera = None, hand = None) :
        self.cube = cube
        self.camera = camera
        self.hand = hand
    def execute(self, command) :
        cubeOpt = {} if (self.cube is None) else {
                'F':self.cube.F,
                'B':self.cube.B,
                'R':self.cube.R,
                'L':self.cube.L,
                'U':self.cube.U,
                'D':self.cube.D,
                'x':self.cube.x,
                'y':self.cube.y,
                'z':self.cube.z
            }
        handOpt = {} if (self.hand is None) else {
                'F':self.hand.F,
                'B':self.hand.B,
                'R':self.hand.R,
                'L':self.hand.L,
                'U':self.hand.U,
                'D':self.hand.D,
                'x':self.hand.x,
                'y':self.hand.y,
                'z':self.hand.z
            }
        num = {'+':1, '2':2, '-':3}
        for i in range(0,len(command),2) :
            f = command[i]
            n = command[i+1]
            if handOpt.has_key(f):
                handOpt[f](num[n])
            if cubeOpt.has_key(f):
                cubeOpt[f](num[n])
    def __bindFrameView(self, frame):
        if not ( self.cube is None ):
            self.cube.bindViewFrame(frame)
    def __bindFrameOperation(self, frame):
        Tkinter.Button(frame, text = "F+", command = lambda:self.execute('F+') ).grid(row = 0, column = 0)
        Tkinter.Button(frame, text = "B+", command = lambda:self.execute('B+') ).grid(row = 0, column = 1)
        Tkinter.Button(frame, text = "R+", command = lambda:self.execute('R+') ).grid(row = 0, column = 2)
        Tkinter.Button(frame, text = "L+", command = lambda:self.execute('L+') ).grid(row = 0, column = 3)
        Tkinter.Button(frame, text = "U+", command = lambda:self.execute('U+') ).grid(row = 0, column = 4)
        Tkinter.Button(frame, text = "D+", command = lambda:self.execute('D+') ).grid(row = 0, column = 5)
        Tkinter.Button(frame, text = 'x+', command = lambda:self.execute('x+') ).grid(row = 0, column = 6)
        Tkinter.Button(frame, text = 'y+', command = lambda:self.execute('y+') ).grid(row = 0, column = 7)
        Tkinter.Button(frame, text = 'z+', command = lambda:self.execute('z+') ).grid(row = 0, column = 8)
        Tkinter.Button(frame, text = "F-", command = lambda:self.execute('F-') ).grid(row = 1, column = 0)
        Tkinter.Button(frame, text = "B-", command = lambda:self.execute('B-') ).grid(row = 1, column = 1)        
        Tkinter.Button(frame, text = "R-", command = lambda:self.execute('R-') ).grid(row = 1, column = 2)
        Tkinter.Button(frame, text = "L-", command = lambda:self.execute('L-') ).grid(row = 1, column = 3)
        Tkinter.Button(frame, text = "U-", command = lambda:self.execute('U-') ).grid(row = 1, column = 4)
        Tkinter.Button(frame, text = "D-", command = lambda:self.execute('D-') ).grid(row = 1, column = 5)
        Tkinter.Button(frame, text = 'x-', command = lambda:self.execute('x-') ).grid(row = 1, column = 6)
        Tkinter.Button(frame, text = 'y-', command = lambda:self.execute('y-') ).grid(row = 1, column = 7)
        Tkinter.Button(frame, text = 'z-', command = lambda:self.execute('z-') ).grid(row = 1, column = 8)
        Tkinter.Button(frame, text = "F2", command = lambda:self.execute('F2') ).grid(row = 2, column = 0)
        Tkinter.Button(frame, text = "B2", command = lambda:self.execute('B2') ).grid(row = 2, column = 1)        
        Tkinter.Button(frame, text = "R2", command = lambda:self.execute('R2') ).grid(row = 2, column = 2)
        Tkinter.Button(frame, text = "L2", command = lambda:self.execute('L2') ).grid(row = 2, column = 3)
        Tkinter.Button(frame, text = "U2", command = lambda:self.execute('U2') ).grid(row = 2, column = 4)
        Tkinter.Button(frame, text = "D2", command = lambda:self.execute('D2') ).grid(row = 2, column = 5)
        Tkinter.Button(frame, text = 'x2', command = lambda:self.execute('x2') ).grid(row = 2, column = 6)
        Tkinter.Button(frame, text = 'y2', command = lambda:self.execute('y2') ).grid(row = 2, column = 7)
        Tkinter.Button(frame, text = 'z2', command = lambda:self.execute('z2') ).grid(row = 2, column = 8)
        if not( self.hand is None):
            frameExtend = Tkinter.LabelFrame(frame, text = 'Hand Only');
            self.hand.bindOperationFrame(frameExtend);
            frameExtend.grid(row = 3, column = 0, columnspan = 9)

    def __bindFrameEdition(self, frame) :
        FUL = Tkinter.Entry(frame, width = 10)
        FUM = Tkinter.Entry(frame, width = 10)
        FUR = Tkinter.Entry(frame, width = 10)
        FLM = Tkinter.Entry(frame, width = 10)
        FRM = Tkinter.Entry(frame, width = 10)
        FDL = Tkinter.Entry(frame, width = 10)
        FDM = Tkinter.Entry(frame, width = 10)
        FDR = Tkinter.Entry(frame, width = 10)
        FUL.grid(row = 0, column = 0)
        FUM.grid(row = 0, column = 1)
        FUR.grid(row = 0, column = 2)
        FLM.grid(row = 1, column = 0)
        FRM.grid(row = 1, column = 2)
        FDL.grid(row = 2, column = 0)
        FDM.grid(row = 2, column = 1)
        FDR.grid(row = 2, column = 2)
        def callback() :
            if not ( self.cube is None ):
                self.cube.setPart('FUL', FUL.get() )
                self.cube.setPart('FUM', FUM.get() )
                self.cube.setPart('FUR', FUR.get() )
                self.cube.setPart('FLM', FLM.get() )
                self.cube.setPart('FRM', FRM.get() )
                self.cube.setPart('FDL', FDL.get() )
                self.cube.setPart('FDM', FDM.get() )
                self.cube.setPart('FDR', FDR.get() )
        def save():
            print self.cube.part
        Tkinter.Button(frame, text = 'change', command = callback).grid(row = 1, column = 1)
        Tkinter.Button(frame, text = 'save', command = save).grid(row = 3, column = 0, columnspan = 3)
    def __bindFrameSolution(self, frame) :
        pattern = Tkinter.StringVar()
        labelPattern = Tkinter.Entry(frame, textvariable = pattern)
        labelPattern.grid(row = 0, column = 1)
        Tkinter.Label(frame, text = 'pattern:').grid(row = 0, column =  0)
        
        solu = Tkinter.StringVar()
        labelSolu = Tkinter.Entry(frame, textvariable = solu)
        labelSolu.grid(row = 1, column = 1)
        Tkinter.Label(frame, text = 'solution:').grid(row = 1, column = 0)
        def sol() :
            if not ( self.cube is None):
                pattern.set(' '.join(self.cube.getPattern()))
                solu.set(Algorithm.CFOP(self.cube.getPattern()))
        Tkinter.Button(frame, text = 'Solve', command = sol).grid(row = 0, column = 2, rowspan = 2)
    def __bindFrameExcution(self, frame):
        cmdEty = Tkinter.Entry(frame)
        cmdEty.grid(row = 0, column = 0)
        Tkinter.Button(frame, text = 'execute', command = lambda:self.execute(cmdEty.get())).grid(row = 0, column = 1)
    def __bindFrameCamera(self, frame):
        if not ( self.camera is None ):
            self.camera.bindViewFrame(frame)

    def run(self):
        self.window = Tkinter.Tk()

        self.frameView = Tkinter.LabelFrame(self.window, text = 'View')
        self.frameOperation = Tkinter.LabelFrame(self.window, text = 'Operation')
        self.frameEdition = Tkinter.LabelFrame(self.window, text = 'Edition')
        self.frameSolution = Tkinter.LabelFrame(self.window, text = 'Solution')
        self.frameExcution = Tkinter.LabelFrame(self.window, text = 'Excution')
        self.frameCamera = Tkinter.LabelFrame(self.window, text = 'Camera')

        self.__bindFrameView(self.frameView)
        self.__bindFrameOperation(self.frameOperation)
        self.__bindFrameEdition(self.frameEdition)
        self.__bindFrameSolution(self.frameSolution)
        self.__bindFrameExcution(self.frameExcution)
        self.__bindFrameCamera(self.frameCamera)

        self.frameView.grid(row = 0, column = 0, rowspan = 4, stick = 'NESW')
        self.frameOperation.grid(row = 0, column = 1, stick = 'NESW')
        self.frameEdition.grid(row = 1, column = 1, stick = 'NESW')
        self.frameSolution.grid(row = 2,column = 1, stick = 'NESW')
        self.frameExcution.grid(row = 3, column =  1, stick = 'NESW')
        self.frameCamera.grid(row = 0, column = 2, rowspan = 4, stick = 'NESW')

        self.window.mainloop()

