import pandas as pd

class Univariate:

    @staticmethod
    def qualquan(d_set):
        quan = []
        qual = []
        for col in d_set.columns:
            if d_set[col].dtype == "object":
                qual.append(col)
            else:
                quan.append(col)
        return qual, quan

    
    @staticmethod
    def freqTable(colName, dSet):
        freqTable = pd.DataFrame(columns=["UniqueValues", "Frequency", "RelativeFrequency", "CumulativeFrequency"])
        
        vc = dSet[colName].value_counts()

        freqTable["UniqueValues"] = vc.index
        freqTable["Frequency"] = vc.values
        
        # Relative Frequency should be divided by total count of that column
        freqTable["RelativeFrequency"] = freqTable["Frequency"] / vc.sum()
        
        freqTable["CumulativeFrequency"] = freqTable["RelativeFrequency"].cumsum()
        
        return freqTable


    @staticmethod
    def _Univariate(quan, dataset):
        descriptive = pd.DataFrame(
            index=["Mean", "Median", "Mode", "Q1:25%", "Q2:50%", "Q3:75%", "Q4:100%",
                   "IQR", "1.5 Rule", "Lesser", "Greater", "Min", "Max","Kurtosis","skew"],
            columns=quan
        )
        
        for col in quan:
            descriptive.loc["Mean", col] = dataset[col].mean()
            descriptive.loc["Median", col] = dataset[col].median()     # FIXED
            descriptive.loc["Mode", col] = dataset[col].mode()[0]

            desc = dataset[col].describe()

            descriptive.loc["Q1:25%", col] = desc["25%"]
            descriptive.loc["Q2:50%", col] = desc["50%"]
            descriptive.loc["Q3:75%", col] = desc["75%"]
            descriptive.loc["Q4:100%", col] = desc["max"]

            IQR = desc["75%"] - desc["25%"]
            descriptive.loc["IQR", col] = IQR

            rule = 1.5 * IQR
            descriptive.loc["1.5 Rule", col] = rule

            descriptive.loc["Lesser", col] = desc["25%"] - rule
            descriptive.loc["Greater", col] = desc["75%"] + rule

            descriptive.loc["Min", col] = dataset[col].min()
            descriptive.loc["Max", col] = dataset[col].max()

            descriptive.loc["Kurtosis", col] = dataset[col].kurtosis()
            descriptive.loc["skew", col] = dataset[col].skew()
        
        return descriptive
    
    @staticmethod
    def OutliersColumns(_quan, descriptive):
        lesser=[]
        greater=[]
        for column in _quan:
            if( descriptive.loc["Min",column] <  descriptive.loc["Lesser",column]):
                lesser.append(column)
            if( descriptive.loc["Max",column] >  descriptive.loc["Greater",column]):
                greater.append(column)
        return lesser, greater
        
    @staticmethod
    def ReplacingOutliers(lesser, greater, dataset, descriptive):
        # For "lesser" columns
        for col in lesser:
            dataset.loc[dataset[col] < descriptive.loc["Lesser", col], col] = descriptive.loc["Lesser", col]
        
        # For "greater" columns
        for col in greater:
            dataset.loc[dataset[col] > descriptive.loc["Greater", col], col] = descriptive.loc["Greater", col]
    
        return dataset
