import os
import json
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser(description='bdd2coco')
parser.add_argument('--bdd_dir', type=str, default='/dataset/BDD/bdd100k_images_100k')
parser.add_argument('--bdd_30k_dir', type=str, default='/dataset/BDD/bdd100k_images_30k')
cfg = parser.parse_args()

src_val_dir = os.path.join(cfg.bdd_dir, 'labels', 'bdd100k_labels_images_val.json')
src_train_dir = os.path.join(cfg.bdd_dir, 'labels', 'bdd100k_labels_images_train.json')

dest_val_label = os.path.join(cfg.bdd_30k_dir, 'labels', 'bdd30k_labels_images_val.json')
dest_train_label = os.path.join(cfg.bdd_30k_dir, 'labels', 'bdd30k_labels_images_train.json')

os.makedirs(os.path.join(cfg.bdd_30k_dir, 'labels'), exist_ok=True)

os.makedirs(os.path.join(cfg.bdd_dir, 'labels_coco'), exist_ok=True)

dst_val_dir = os.path.join(cfg.bdd_dir, 'labels_coco', 'bdd100k_labels_images_val_coco.json')
dst_train_dir = os.path.join(cfg.bdd_dir, 'labels_coco', 'bdd100k_labels_images_train_coco.json')

# -----------------------------------------------------------------------------------------------------
#                                      Create Training Label File
# -----------------------------------------------------------------------------------------------------

print('Loading training set...')
with open(src_train_dir) as f:
    train_labels = json.load(f)

train_labels_30k = list()
for ilabel in tqdm(train_labels):
    filename = os.path.join(cfg.bdd_30k_dir, 'images', '30k', 'train', ilabel['name'])
    
    # print("----------------------------------------------------------------")
    # print(filename)
    # print("----------------------------------------------------------------")

    if os.path.exists(filename):
        # print("PASSED")
        train_labels_30k.append(ilabel)
    # else:
        # print("FAILED")

# Serializing Training json 
json_object = json.dumps(train_labels_30k, indent = 4)
# Writing to training json
with open(dest_train_label, "w") as outfile:
    outfile.write(json_object)

# -----------------------------------------------------------------------------------------------------
#                                      Create Validation Label File
# -----------------------------------------------------------------------------------------------------


print('Loading validation set...')
with open(src_val_dir) as f:
    valid_labels = json.load(f)

valid_labels_30k = list()
for ilabel in tqdm(valid_labels):
    filename = os.path.join(cfg.bdd_30k_dir, 'images', '30k', 'valid', ilabel['name'])
    
    # print("----------------------------------------------------------------")
    # print(filename)
    # print("----------------------------------------------------------------")

    if os.path.exists(filename):
        # print("PASSED")
        valid_labels_30k.append(ilabel)
    # else:
        # print("FAILED")

# Serializing Training json 
json_object = json.dumps(valid_labels_30k, indent = 4)
# Writing to training json
with open(dest_val_label, "w") as outfile:
    outfile.write(json_object)