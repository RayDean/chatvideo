import torch
import logging


class QueryTextEmbedServer(object):

    def __init__(self,model):
        """
        查询提示词向量的服务器
        :param model:
        """
        self.model = model

    def get_query_embed(self,query):
        """
        获取query提示词的词向量
        支持批次查询
        :param query:
        :return:
        """
        query_features = self.model.get_text_embed(query)
        return query_features
