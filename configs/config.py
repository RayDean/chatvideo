from yacs.config import CfgNode as CN
# 由于目前使用两个editor：Text2Video-其配置来源于：configs/text2video, URL2VideoEditor-其配置来源于configs/url2video
# 单这两个editor的yml配置都是由四个基本要素组成：visual_gen-生成视频，tts_gen-由文字生成语音，subtitle-字幕的配置，text_gen-生成文字
# 所以下面的config可以包括这两个editor的内容
_C = CN()
_C.video_editor = CN()
_C.video_editor.type = "Text2Video"

# 视频信息的生成模式
_C.video_editor.visual_gen = CN()
_C.video_editor.visual_gen.type = "image_by_retrieval" 
# 其他类型: image_by_diffusion  video_by_retrieval image_by_retrieval_then_diffusion video_by_diffusion
_C.video_editor.visual_gen.image_by_retrieval = CN()
# query model
_C.video_editor.visual_gen.image_by_retrieval.model = "ViT-L/14" 
_C.video_editor.visual_gen.image_by_retrieval.model_path = ""
_C.video_editor.visual_gen.image_by_retrieval.device = "cpu" # index file path

# index
_C.video_editor.visual_gen.image_by_retrieval.index_path = "" # index file path

# meta
_C.video_editor.visual_gen.image_by_retrieval.meta_path = "" # meta file path

# video query model
_C.video_editor.visual_gen.video_by_retrieval = CN()
_C.video_editor.visual_gen.video_by_retrieval.model = "ViT-B/32"
_C.video_editor.visual_gen.video_by_retrieval.model_path = ""
_C.video_editor.visual_gen.video_by_retrieval.device = "cpu"

# video index 
_C.video_editor.visual_gen.video_by_retrieval.index_path = ""
_C.video_editor.visual_gen.video_by_retrieval.meta_path = ""

# image gen by diffusion
_C.video_editor.visual_gen.image_by_diffusion = CN()
_C.video_editor.visual_gen.image_by_diffusion.model_id = "stabilityai/stable-diffusion-2-1"

# image_by_retrieval_then_diffusion
_C.video_editor.visual_gen.image_by_retrieval_then_diffusion = CN()

_C.video_editor.visual_gen.image_by_retrieval_then_diffusion.model_id = "stabilityai/stable-diffusion-2-1"

# text gen
_C.video_editor.text_gen = CN()
_C.video_editor.text_gen.type = "toy"
_C.video_editor.text_gen.organization = ""
_C.video_editor.text_gen.api_key = ""

# tts 
_C.video_editor.tts_gen = CN()
_C.video_editor.tts_gen.model = "PaddleSpeechTTS"
# set am
_C.video_editor.tts_gen.am = 'fastspeech2_mix'
_C.video_editor.tts_gen.lang = 'mix'

# subtitle
_C.video_editor.subtitle = CN()
_C.video_editor.subtitle.font=""

# bgm 
_C.video_editor.bgm_gen = CN()
_C.video_editor.bgm_gen.type = "toy"


def get_cfg_defaults():
  """
  通过yacs来获取配置，某些配置有自己的默认值
  :return:
  """
  return _C.clone()