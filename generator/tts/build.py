from generator.tts.tts_generator import TTSGenerator
from generator.tts.paddlespeech_model import PaddleSpeechTTS
from comm.mylog import logger


def build_tts_generator(cfg):
    """
    根据配置cfg来产生语音产生器
    :param cfg:
    :return:
    """
    # 使用的文本转语音模型
    tts_model = cfg.video_editor.tts_gen.model
    logger.info('tts_model: {}'.format(tts_model))
    tts_generator = None
    # 目前仅支持PaddleSpeechTTS
    if tts_model == "PaddleSpeechTTS":
        model = PaddleSpeechTTS(
                                lang=cfg.video_editor.tts_gen.lang,
                                am=cfg.video_editor.tts_gen.am,
                                )
        tts_generator = TTSGenerator(cfg,model)
    else:
        raise ValueError('tts_model: {} not support'.format(tts_model))
    return tts_generator

    