python BERT_NER.py \
    --task_name=NER \
    --do_lower_case=True \
    --do_train=False \
    --do_eval=True \
    --do_predict=True \
    --train_batch_size=32 \
    --eval_batch_size=8 \
    --predict_batch_size=8 \
    --data_dir=data/ \
    --vocab_file=vocab.txt \
    --bert_config_file=cased_L-12_H-768_A-12/bert_config.json \
    --init_checkpoint=cased_L-12_H-768_A-12/bert_model.ckpt \
    --max_seq_length=128   \
    --learning_rate=2e-5   \
    --num_train_epochs=1.0 \
    --output_dir=./output/result_dir/ \