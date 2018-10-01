---
layout: post
title: Log of MRI Denoising Project
category: MRI Denoising
excerpt_separator:  <!--more-->
---
<style>
.parameter{font-size:15px; background-color:rgb(230, 230, 230); padding:10px}
</style>

## Experiment Record
1. MRI_cont3_motion_l2_masked_test(Pix2Pix)
    -   <details><summary>Parameters</summary>
        <pre class="parameter">
        "GEN_LOSS": "L2_masked",
        "GPU_IND": "3",  
        "aspect_ratio": 1.0,  
        "batch_size": 1,  
        "beta1": 0.5,  
        "checkpoint": "../training_checkpoint/MRI_cont3_motion_l2_masked_train",  
        "custom_loss_weight": 100.0,  
        "display_freq": 1000,  
        "flip": false,  
        "gan_weight": 1.0,  
        "input_dir": "../training_data/MRI_cont3_motion/val",  
        "lab_colorization": false,  
        "lr": 0.0002,  
        "max_epochs": null,  
        "max_steps": null,  
        "mode": "test",  
        "ndf": 64,  
        "ngf": 64,  
        "output_dir": "../test_result/MRI_cont3_motion_l2_masked_test",  
        "output_filetype": "png",  
        "progress_freq": 50,  
        "save_freq": 5000,  
        "scale_size": 256,  
        "seed": 1035730246,  
        "separable_conv": false,  
        "summary_freq": 100,  
        "trace_freq": 0,  
        "which_direction": "BtoA"  
        Dataset_size: 2100
        </pre>
        </details>
    - Images
        - training
            ![]("{{ site.baseurl }}/assets/imgs/denoising/MRI_cont3_motion_l2_masked_test/training/00202000-1095-inputs.png")


<details style="margin-top:0px; width:1000px">
    <summary>Parameters</summary>
    <pre style="margin-top:0px; width:1000px">
    {% for image in site.static_files %}
        {% if image.path contains 'MRI_cont3_motion_l2_masked_test/training' %}
            <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" />
        {% endif %}
    {% endfor %}
    </pre>
</details>

## Log
### 2018-09-30
- Create FIle
