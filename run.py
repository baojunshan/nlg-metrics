import argparse
import json
import tabulate

from nlg_metrics.metrics import Metrics


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="待评估文件，格式为json[{'ref': str, 'hyps': [str, ..]}, ...]")
parser.add_argument("--output", type=str, default=None, help="保存文件")
parser.add_argument("--metrics", type=eval, default=None, help=f"评估方法，目前有{Metrics.AVAILABLE_METRICS.keys()}")
parser.add_argument("--ppl_model_path", type=str, default=None, help="如果计算ppl，需要输入模型路径")
parser.add_argument("--verbose", type=bool, default=True, help="显示进度条")
cfg = parser.parse_args()

metrics = Metrics(metrics=cfg.metrics, path=cfg.ppl_model_path)
with open(cfg.input, "r") as f:
    inputs = json.load(f)
results = metrics.calc(inputs=inputs, verbose=cfg.verbose)

if cfg.output is not None:
    with open(cfg.output, "w") as f:
        json.dump(results, f)

contents, header = list(), list(metrics.metrics)
for metric in metrics.metrics:
    score = [res[metric] for res in results]
    contents.append(sum(score) / len(score))
header.append("data size")
contents.append(len(results))
print(tabulate.tabulate([contents], header, tablefmt='fancy_grid'))