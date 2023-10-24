class ModelStore:
    def __init__(self):
        self.Models = None
        self.Scenes = None
        self.Flashes = None
        self.Cameras = None
        self.changeObservers = None

    def GetScene(self, int):
        pass

    def NotifyChange(self, ModelChanger):
        pass