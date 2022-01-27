from tqdm import tqdm

from .rouges import (
    Rouge1,
    Rouge2,
    RougeL,
)
from .bleus import (
    Bleu,
    SelfBleu,
)
from .meteors import (
    Meteor,
)
from .perplexity import (
    Perplexity,
)


class Metrics:

    AVAILABLE_METRICS = {
        "rouge-1": Rouge1,
        "rouge-2": Rouge2,
        "rouge-l": RougeL,
        "bleu": Bleu,
        "self-bleu": SelfBleu,
        "meteor": Meteor,
        "ppl": Perplexity
    }
    DEFAULT_METRICS = ["bleu", "self-bleu", "meteor", "ppl"]

    def __init__(self, metrics:list=None, path:str=None):
        self.metrics = metrics or Metrics.DEFAULT_METRICS
        self.metrics = list((set(self.metrics) & set(Metrics.AVAILABLE_METRICS.keys())))
        self.models = list()
        for metric in self.metrics:
            if metric == "ppl":
                self.models.append(Metrics.AVAILABLE_METRICS[metric](model_path=path))
            else:
                self.models.append(Metrics.AVAILABLE_METRICS[metric]())

    def calc(self, inputs, verbose=False):
        results = list()
        for data in tqdm(inputs, disable=not verbose):
            ref, hyps = data["ref"], data["hyps"]
            results.append({
                metric: model.calc(hyps=hyps, ref=ref) for metric, model in zip(self.metrics, self.models)
            })
        return results
