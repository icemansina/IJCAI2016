import numpy as np
class ConfusionMatrix:
    """
       Simple confusion matrix class
       row is the true class, column is the predicted class
    """
    def __init__(self, n_classes):
        self.n_classes = n_classes
        self.mat = np.zeros((n_classes,n_classes),dtype='int')

    def __str__(self):
        return np.array_str(self.mat)

    def batchAdd(self,y_true,y_pred):
        assert len(y_true) == len(y_pred)
        assert max(y_true) < self.n_classes
        assert max(y_pred) < self.n_classes
        for i in range(len(y_true)):
                self.mat[y_true[i],y_pred[i]] += 1

    def zero(self):
        self.mat.fill(0)

    def getErrors(self):
        """
        Calculate differetn error types
        :return: vetors of true postives (tp) false negatives (fn), false positives (fp) and true negatives (tn)
                 pos 0 is first class, pos 1 is second class etc.
        """
        tp = np.asarray(np.diag(self.mat).flatten(),dtype='float')
        fn = np.asarray(np.sum(self.mat, axis=1).flatten(),dtype='float') - tp
        fp = np.asarray(np.sum(self.mat, axis=0).flatten(),dtype='float') - tp
        tn = np.asarray(np.sum(self.mat)*np.ones(self.n_classes).flatten(),dtype='float') - tp - fn - fp
        return tp,tn,fp,fn

    def accuracy(self):
        """
        Calculates global accuracy
        :return: accuracyn
        :example: >>> conf = ConfusionMatrix(3)
                  >>> conf.batchAdd([0,0,1],[0,0,2])
                  >>> print conf.accuracy()
        """
        tp, _, _, _ = self.getErrors()
        n_samples = np.sum(self.mat)
        return np.sum(tp) / n_samples


    def sensitivity(self):
        tp, tn, fp, fn = self.getErrors()
        res = tp / (tp + fn)
        res = res[~np.isnan(res)]
        return res

    def specificity(self):
        tp, tn, fp, fn = self.getErrors()
        res = tn / (tn + fp)
        res = res[~np.isnan(res)]
        return res

    def positivePredictiveValue(self):
        tp, tn, fp, fn = self.getErrors()
        res = tp / (tp + fp)
        res = res[~np.isnan(res)]
        return res

    def negativePredictiveValue(self):
        tp, tn, fp, fn = self.getErrors()
        res = tn / (tn + fn)
        res = res[~np.isnan(res)]
        return res

    def falsePositiveRate(self):
        tp, tn, fp, fn = self.getErrors()
        res = fp / (fp + tn)
        res = res[~np.isnan(res)]
        return res

    def falseDiscoveryRate(self):
        tp, tn, fp, fn = self.getErrors()
        res = fp / (tp + fp)
        res = res[~np.isnan(res)]
        return res

    def F1(self):
        tp, tn, fp, fn = self.getErrors()
        res = (2*tp) / (2*tp + fp + fn)
        res = res[~np.isnan(res)]
        return res

    def matthewsCorrelation(self):
        tp, tn, fp, fn = self.getErrors()
        numerator = tp*tn - fp*fn
        denominator = np.sqrt((tp + fp)*(tp + fn)*(tn + fp)*(tn + fn))
        res = numerator / denominator
        res = res[~np.isnan(res)]
        return res
    def getMat(self):
        return self.mat




