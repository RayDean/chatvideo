from generator.image.retrieval.models.clip_model import ClipTextEmbed, MClipTextEmbed


def build_image_query_model(model_name, device):
    """
    依据模型名称和运行设备得到具体的模型
    :param model_name:
    :param device:
    :return:
    """
    if model_name == "ViT-L/14":
        model = ClipTextEmbed(model_name = model_name, device = device)
    elif model_name == "M-CLIP/XLM-Roberta-Large-Vit-L-14":
        model = MClipTextEmbed(model_name = model_name, device = device)
    else:
        raise ValueError("model_name={} is not supported.".format(model_name))
    return model
