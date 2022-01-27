python run.py \
--input ./jd_data_for_eval.json \
--output results.json \
--metrics "['rouge-1', 'rouge-2', 'rouge-l', 'bleu', 'self-bleu', 'meteor', 'ppl']" \
--ppl_model_path "/home/baojunshan/data/pretrained_models/chinese_bert_wwm_ext_pytorch" \
--verbose True