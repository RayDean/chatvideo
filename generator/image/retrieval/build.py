from generator.image.retrieval.models.build import build_image_query_model
from generator.image.retrieval.server.embed import QueryTextEmbedServer
from generator.image.retrieval.server.knn import FiassKnnServer


def build_QueryTextEmbedServer(cfg):
    """
    依据cfg构建查询文本对应词向量的类
    :param cfg:
    :return:
    """
    # image_by_retrieval所使用的模型
    model_name = cfg.video_editor.visual_gen.image_by_retrieval.model
    # image_by_retrieval所运行模型的设备：CPU 或 GPU
    device = cfg.video_editor.visual_gen.image_by_retrieval.device
    # 依据模型名称和所运行的设备获取对应的模型
    model = build_image_query_model(model_name = model_name, device = device)
    return QueryTextEmbedServer(model)


def build_FiassKnnServer(cfg):
    """
    根据配置cfg
    :param cfg:
    :return:
    """
    index_path = cfg.video_editor.visual_gen.image_by_retrieval.index_path
    return FiassKnnServer(index_path)
