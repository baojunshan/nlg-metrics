import six
import nltk

from .base import IMetrics


class Meteor(IMetrics):
    def __init__(self):
        super(Meteor, self).__init__()
        self.model = nltk.translate.meteor_score.single_meteor_score

    @property
    def name(self):
        return "meteor"

    def calc(self, hyps, ref, *args, **kwargs):
        if isinstance(hyps, six.string_types):
            hyps = [hyps]
        ref = list(ref) if isinstance(ref, six.string_types) else ref
        scores = list()
        for hyp in hyps:
            hyp = list(hyp) if isinstance(hyp, six.string_types) else hyp
            scores.append(self.model(reference=ref, hypothesis=hyp,  preprocess=str.lower, alpha=0.9, beta=3.0, gamma=0.5))
        return sum(scores) / len(scores)