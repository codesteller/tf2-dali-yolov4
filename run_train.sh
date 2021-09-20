python src/main.py train /dataset/BDD/bdd100k_images_30k/images/30k/train/ \
/dataset/BDD/bdd100k_images_30k/labels_coco/bdd30k_labels_images_train_coco.json \
-b 8 -e 50 -s 2000 -o ./results/output.h5 --pipeline dali-gpu --multigpu --use_mosaic \
--learning_rate 0.00001 \
--eval_file_root /dataset/BDD/bdd100k_images_30k/images/30k/valid/ \
--eval_annotations /dataset/BDD/bdd100k_images_30k/labels_coco/bdd30k_labels_images_val_coco.json \
--eval_frequency 5 --eval_steps 500 --ckpt_dir ./results/ckpt_dir/ --log_dir ./results/logs/
