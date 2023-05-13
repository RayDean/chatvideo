from paddlespeech.cli.tts.infer import TTSExecutor
from comm.mylog import logger


class PaddleSpeechTTS(object):

    def __init__(self,
                 lang='mix',
                 am='fastspeech2_mix',
                 ) -> None:
        """
        构建Paddle语音合成类
        :param lang:
        :param am:
        """
        self.tts = TTSExecutor()
        self.am = am
        self.lang = lang
        logger.info('building PaddleSpeechTTS, am: {}, lang: {}'.format(am,lang))

    def run_tts(self,text,out_path):
        """
        将text文本转变为语音，并将语音文件保存到out_path中
        :param text:
        :param out_path:
        :return:
        """
        self.tts(text=text,lang=self.lang,am=self.am,output=out_path)
    