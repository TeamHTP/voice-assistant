class Skill(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def do(self, params):
        raise NotImplementedError