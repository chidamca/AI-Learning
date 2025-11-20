class Univariate():
    def qualquan(d_set):
        quan=[]
        qual=[]
        for colum in d_set.columns:
            if d_set[colum].dtypes == "object":
                qual.append(colum)
            else:
                quan.append(colum)
        return qual,quan
