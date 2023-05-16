import faiss


class FiassKnnServer(object):

    def __init__(self,
                 index_path,
                 ):
        """
        构建FiassKNN类
        :param index_path:
        """
        # loading faiss index
        # self.top_k = 10
        self.nprobe = 1024 
        self.index_path = index_path
        
        self.index = faiss.read_index(index_path)
        if isinstance(self.index,faiss.swigfaiss.IndexPreTransform):
            faiss.ParameterSpace().set_index_parameter(self.index, "nprobe", self.nprobe)
        else:
            self.index.nprobe = self.nprobe
        
    def search(self,query_emebed,top_k=50):
        """
        搜索query_embed对应的top_k个最相似的向量
        :param query_emebed: np.ndarray
        :param top_k:
        :return:
        """
        query_emebed = query_emebed.astype('float32')
        distances, indices = self.index.search(query_emebed, top_k)
        return distances, indices

    def batch_search(self,query_list):
        pass


if __name__ == '__main__':
    pass