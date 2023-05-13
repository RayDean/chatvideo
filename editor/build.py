from generator.image.build import build_image_generator
from generator.video.build import build_video_generator
from generator.tts.build import build_tts_generator
from generator.text.build import build_text_generator
from generator.music.build import build_bgm_generator
from editor.chat_editor import Text2VideoEditor
from comm.mylog import logger


def build_editor(cfg):
    """
    根据cfg中的配置内容，产生图像/视频生成器，文本生成器，音频生成器，背景音乐生成器，
    并将这些生成器并产生整体视频合成器，返回该合成器
    :param cfg:
    :return:
    """
    # 通过什么方式产生视频
    visual_gen_type = cfg.video_editor.visual_gen.type
    logger.info('visual_gen_type: {}'.format(visual_gen_type))
    # image_by_diffusion  video_by_retrieval image_by_retrieval_then_diffusion video_by_diffusion
    if visual_gen_type in ["image_by_retrieval","image_by_diffusion","image_by_retrieval_then_diffusion"]:
        # 如果是产生图像
        vision_generator = build_image_generator(cfg)
    else:
        # 其他则产生视频
        vision_generator = build_video_generator(cfg)

    # 文本产生器
    text_generator = build_text_generator(cfg)
    # 音频产生器
    audio_generator = build_tts_generator(cfg)
    # 背景音乐产生器
    bgm_generator = build_bgm_generator(cfg)
    # 将多种元素合并为视频
    editor = Text2VideoEditor(cfg,text_generator, vision_generator, audio_generator,bgm_generator)
    return editor