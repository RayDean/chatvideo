
class QueryTextEmbedServer(object):

    def __init__(self,model):
        """
        初始化QueryTextEmbedServer类
        :param model:
        """
        self.model = model

    def get_query_embed(self,query):
        """
        获取文本query的词向量
        :param query:
        :return:
        """
        query_features = self.model.get_text_embed(query)
        return query_features
