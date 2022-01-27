from rouge import Rouge as R
import six

from .base import IMetrics


class Rouge1(IMetrics):
    def __init__(self):
        super().__init__()
        self.model = R(metrics=["rouge-1"])

    @property
    def name(self):
        return "rouge-1"

    def calc(self, hyps, ref, *args, **kwargs) -> float:
        if isinstance(hyps, six.string_types):
            hyps = [hyps]
        scores = [self.model.get_scores(hyps=" ".join(hyp), refs=" ".join(ref))[0][self.name]["f"] for hyp in hyps]
        return sum(scores) / len(scores)


class Rouge2(Rouge1, IMetrics):
    def __init__(self):
        super().__init__()
        self.model = R(metrics=["rouge-2"])

    @property
    def name(self):
        return "rouge-2"



class RougeL(Rouge1, IMetrics):
    def __init__(self):
        super().__init__()
        self.model = R(metrics=["rouge-l"])

    @property
    def name(self):
        return "rouge-l"


