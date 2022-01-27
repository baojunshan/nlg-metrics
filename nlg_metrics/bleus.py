import nltk
import six

from .base import IMetrics


class Bleu(IMetrics):
    def __init__(self, ngram=3):
        super(Bleu, self).__init__()
        self.ngram = ngram
        self.weights = [1 / ngram] * ngram
        self.model = nltk.translate.bleu_score.sentence_bleu
        self.smoothing_func = nltk.translate.bleu_score.SmoothingFunction().method1

    @property
    def name(self):
        return "bleu"

    def calc(self, hyps, ref, *args, **kwargs) -> float:
        if isinstance(hyps, six.string_types):
            hyps = [hyps]
        scores = [self.model([" ".join(ref)], " ".join(hyp), weights=self.weights, smoothing_function=self.smoothing_func) for hyp in hyps]
        return sum(scores) / len(scores)


class SelfBleu(IMetrics):
    def __init__(self, ngram=3):
        super(SelfBleu, self).__init__()
        self.ngram = ngram
        self.bleu = Bleu(ngram=ngram).calc

    @property
    def name(self):
        return "self-bleu"

    def calc(self, hyps: list, *args, **kwargs):
        n = len(hyps)
        if n < 2:
            return 1
        scores = [self.bleu(hyps[i], hyps[j]) for i in range(n) for j in range(i + 1, n)]
        return sum(scores) / len(scores)

