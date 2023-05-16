#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

"""Add custom configs and default values"""


def add_custom_config(_C, CfgNode):
    # Add your own customized configs.
    
    # MeMViT
    _C.MEMVIT = CfgNode()
    _C.MEMVIT.ENABLE = True
    # Length of memory to attend to.
    _C.MEMVIT.ATTN_MAX_LEN = 2
    # Memory sampler type.
    _C.MEMVIT.SAMPLER = "all"
    # No memory attention in these layers.
    _C.MEMVIT.EXCLUDE_LAYERS = []
    
    # Memory compression.
    _C.MEMVIT.COMPRESS = CfgNode()
    _C.MEMVIT.COMPRESS.ENABLE = False
    # Memory compression kernel size.
    _C.MEMVIT.COMPRESS.POOL_KERNEL = [3, 3, 3]
    # Memory compression stride.
    _C.MEMVIT.COMPRESS.POOL_STRIDE = [2, 2, 2]

    # If True, make model causal (used in, e.g., anticipation tasks).
    _C.MVIT.CAUSAL = True

    _C.MVIT.BOX_DEPTH = 0

    _C.MVIT.BOX_DROPPATH_RATE = 0.1

    _C.MVIT.BOX_DROP_ATTN_RATE = 0.0

    _C.MVIT.BOX_DROP_QKV_RATE = 0.0

    _C.MVIT.BOX_DROPOUT_RATE = 0.0

    # LePE pos
    _C.MVIT.CONV_Q = 0

    # Dim mul in qkv linear layers of attention block instead of MLP
    _C.MVIT.DIM_MUL_IN_ATT = False

    _C.MVIT.SEPARATE_QKV = False

    # Initial stride size for KV at layer 1. The stride size will be further reduced with
    # the raio of MVIT.DIM_MUL. If will overwrite MVIT.POOL_KV_STRIDE if not None.
    _C.MVIT.POOL_KV_STRIDE_ADAPTIVE = []

    # If True, do frame-level prediction (e.g., used in online-memory EPIC models).
    _C.MVIT.FRAME_LEVEL = False

    # If True, log the model info.
    _C.LOG_MODEL_INFO = True

    _C.TRAIN.CHECKPOINT_IN_INIT = False

    # # Whether enable video detection.
    # _C.DETECTION.ENABLE = False
    