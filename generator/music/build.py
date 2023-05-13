from generator.music.toy import ToyBgmGenerator
from comm.mylog import logger


def build_bgm_generator(cfg):
    """
    根据cfg配置内容构建背景音乐产生器
    :param cfg:
    :return:
    """
    # 背景音乐的类型
    bgm_gen_type = cfg.video_editor.bgm_gen.type
    logger.info('bgm_gen_type: {}'.format(bgm_gen_type))
    bgm_generator = None
    if bgm_gen_type == "toy":
        bgm_generator = ToyBgmGenerator()
    return bgm_generator

