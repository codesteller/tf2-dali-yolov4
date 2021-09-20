# tf2-dali-yolov4
Train YoloV4 Architecture on MultiGPU with DALI input Pipeline


## Convert Data
Change the path in the file accordingly

```
python bdd2coco/convert_bdd2coco.py --bdd_dir <path to bdd data>
```

```
python src/main.py train /dataset/BDD/bdd100k_images_30k/images/30k/train /dataset/BDD/bdd100k_images_30k/labels_coco/bdd30k_labels_images_train_coco.json -b 8 -e 2 -o output.h5 --pipeline dali-gpu --multigpu --use_mosaic
```

```
python src/main.py train /dataset/BDD/bdd100k_images_30k/images/30k/train /dataset/BDD/bdd100k_images_30k/labels_coco/bdd30k_labels_images_train_coco.json -b 10 -e 50 -s 2400 -o ./results/output.h5 --pipeline dali-gpu --multigpu --use_mosaic --eval_file_root /dataset/BDD/bdd100k_images_30k/images/30k/valid --eval_annotations /dataset/BDD/bdd100k_images_30k/labels_coco/bdd30k_labels_images_val_coco.json --eval_frequency 5 --ckpt_dir ./results/ckpt --log_dir ./results/logs
```