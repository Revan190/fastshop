class BaseCrudPrefixes:
    def __init__(self):
        self.create: str = '/create'
        self.read: str = '/read'
        self.update: str = '/update'
        self.delete: str = '/delete'
        self.root: str = '/'
        self.detail: str = '/{pk}'