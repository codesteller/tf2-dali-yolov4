docker run --gpus '"device=0,1,2,3"' -it --rm --shm-size=1g --ulimit memlock=-1 \
-p 9000:8888 -p 0.0.0.0:9006:6006 \
-v $(pwd):/workspace/myspace \
-v /media/d3a/01_Datasets/CV_Data/MSCoco/coco2017:/dataset/coco2017 \
-v /media/d4a/cv_dataset/BDD:/dataset/BDD \
-w /workspace/myspace \
codesteller/rachetnet:21.04
