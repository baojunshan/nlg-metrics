## 衡量生成文本质量的方法集

## 快速开始
把待检测文件整理成如下格式：
```json
[
  {"ref": str, "hyps": [str, str, ...]},
  {...},
  ...
]
```
### 命令行方法

查看用法
```shell
python run.py -h
```
或者查看`run.sh`的例子

```shell
python run.py --input=input_path --output=output_path --metrics="['rouge-1', 'bleu', 'self-bleu']"
```

当前支持的方法有`rouge-l`, `rouge-2`, `rouge-l`, `bleu`, `self-bleu`, `meteor`, `ppl`。

其中，如果选择`ppl`，则需要增加命令行参数`--ppl_model_path=model_path`，这个path为[模型文件(bert模型)](https://github.com/baojunshan/nlp-fluency)

如果第一次使用`meteor`，需要去[nltk](http://www.nltk.org/nltk_data/) 下载带中文的wordnet数据 [Open Multilingual Wordnet (omw)](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/omw.zip) 
以及 [wordnet](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet31.zip) ，放入`/root/nltk_data/corpora/`中解压 

### python调用
```python
from metrics import Metrics

inputs = json.load(...)

model = Metrics(metrics=["bleu", "rouge-l", "ppl"], path=...)
results = model.calc(inputs=inputs)
```

