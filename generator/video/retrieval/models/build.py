from comm.mylog import logger
from generator.video.retrieval.models.clip_model import ClipTextEmbed, MClipTextEmbed


def build_video_query_model(model_name, device):
    """
    构建视频查询模型
    :param model_name:
    :param device:
    :return:
    """
    if model_name == "ViT-B/32":
        model = ClipTextEmbed(model_name = model_name, device = device)
    elif model_name == "M-CLIP/XLM-Roberta-Large-Vit-L-14":
        model = MClipTextEmbed(model_name = model_name, device = device)
        
    return model
