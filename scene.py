

class Scene:

    def __init__(self,director):
        self.director = director

    def on_update(self):
        raise NotImplementedError

    def on_event(self,event):
        raise NotImplementedError

    def on_draw(self):
        raise NotImplementedError

    def on_reset(self):
        pass

    def calculateMiddle(self,widthAndHeight,screenDimensions):
        wLoc = int(screenDimensions[0]/2 - widthAndHeight[0]/2)
        hLoc = int(screenDimensions[1]/2 - widthAndHeight[1]/2)
        return (wLoc,hLoc)

    def on_startup(self):
        pass
