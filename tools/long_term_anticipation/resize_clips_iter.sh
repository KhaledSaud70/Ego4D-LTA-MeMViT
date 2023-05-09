#!/bin/bash

source ~/.bashrc

cd /home/khaled/workspaces/Ego4D/Ego4D_lta/

EGO4D_CLIP_DIR=data/long_term_anticipation/clips_hq/
TARGET_DIR=data/long_term_anticipation/clips/

mkdir -p ${TARGET_DIR}

for CLIP in $(find ${EGO4D_CLIP_DIR} -name "*.mp4")
do
    FILENAME=$(basename $CLIP)
    ffmpeg -y -i $CLIP \
        -c:v libx264 \
        -crf 28 \
        -vf "scale=320:320:force_original_aspect_ratio=increase,pad='iw+mod(iw,2)':'ih+mod(ih,2)'" \
        -an ${TARGET_DIR}/${FILENAME}
done
