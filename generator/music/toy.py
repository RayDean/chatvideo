import random


class ToyBgmGenerator(object):

    def __init__(self) -> None:
        """
        背景音乐产生器
        """
        self.bgms = [
            "generator/music/12Mornings.mp3",
            "generator/music/AcousticBlues.mp3",
            "generator/music/AllGoodInTheWood.mp3",
            "generator/music/ClapAlong.mp3",
        ]
    
    def run(self,):
        """
        从所有候选的背景音乐中随机选择一个
        :return:
        """
        local_file = random.choice(self.bgms)
        resp = {
            'bgm_local_file':local_file,
        }
        return resp
