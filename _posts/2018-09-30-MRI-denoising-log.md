---
layout: post
title: MRI Denoising Project Log
category: MRI Denoising
excerpt_separator:  <!--more-->
---
<style>
.parameter{font-size:15px; background-color:rgb(230, 230, 230); padding:10px}
</style>
<!-- https://stackoverflow.com/questions/17677094/jekyll-for-loop-over-all-images-in-a-folder -->

## Ongoing Projects


| Index | Name                                                           | Location        | Description | Comment | Start        | To              | Speed           | End         |
| ----- | -------------------------------------------------------------- | --------------- | ----------- | ------- | ------------ | --------------- | --------------- | ----------- |
| 1     | l2_3C_motion_masked_gradient_masked_reg_no_drop_0.75_FULL_data | cigserver1/gpu2 |             |         | Oct 1 16:10  | 27 Oct 1 19:10  | 0.11 hour/epoch | Oct 2 14:00 |
| 2     | l2_3C_motion_gradient_reg_no_drop_0.75_FULL_data               | cigserver1/gpu3 |             |  END    | Sep 30 22:32 | 189 Oct 1 19:09 | 0.1 hour/epoch  |             |
| 3     | test_MRI_cont3_motion_l2_masked_grad_masked_w3_FULL            | cigserver2      |             |  END    | Oct 1 12:53  |                 |                 | Oct 2 11:30 |
| 4     | test_MRI_cont3_motion_l2_masked_grad_masked_w3_FULL_SEG        | cigserver2      |             |         | Oct 2 11:40  |                 |                 | Oct 3 17:30 |
| 5     | l2_3C_motion_masked_gradient_masked_reg_no_drop_0.75_FULL_data_w2 | cigserver1/gpu3 |             |  300Eps       | Oct 2 15:20  |   | x hour/epoch | Oct 3 21:20 |
| 6     | l2_3C_motion_masked_gradient_masked_reg_no_drop_0.75_FULL_SEG | cigserver1/gpu2 |             |  300Eps     | Oct 2 15:20  |   | x hour/epoch | Oct 3 21:20 |

<!--more-->

## Experiment Record
1. **MRI_cont3_motion_l2_masked (Pix2Pix)**
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
    - Outputs
        - <details style="margin-top:0px; width:1000px">
                <summary>Training</summary>
                {% for image in site.static_files %}
                    {% if image.path contains 'MRI_cont3_motion_l2_masked/training' %}
                        <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" />
                    {% endif %}
                {% endfor %}
            </details>    
        - <details style="margin-top:0px; width:1000px">
                <summary>Test</summary>
                {% for image in site.static_files %}
                    {% if image.path contains 'MRI_cont3_motion_l2_masked/test' %}
                        <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" />
                    {% endif %}
                {% endfor %}
            </details>    
    - Strangely, training outputs seem to distort the shape of organs —— which may could be solved by put larger weight on l2 loss —— test outputs look much better than training outputs and only oversmooth. 
    - Direction: Use more data and larger l2 weight

2. **MRI_cont3_motion_l2_weight1**
    -   <details><summary>Parameters</summary>
        <pre class="parameter">
            "GEN_LOSS": "L2",
            "GPU_IND": "3",
            "aspect_ratio": 1.0,
            "batch_size": 1,
            "beta1": 0.5,
            "checkpoint": "../training_checkpoint/MRI_cont3_motion_l2_weight1_train",
            "custom_loss_weight": 10.0,
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
            "output_dir": "../test_result/MRI_cont3_motion_l2_weight1_test",
            "output_filetype": "png",
            "progress_freq": 50,
            "save_freq": 5000,
            "scale_size": 256,
            "seed": 385461128,
            "separable_conv": false,
            "summary_freq": 100,
            "trace_freq": 0,
            "which_direction": "BtoA"
        </pre>
        </details>
    - Outputs
        - <details style="margin-top:0px; width:1000px">
                <summary>Training</summary>
                {% for image in site.static_files %}
                    {% if image.path contains 'MRI_cont3_motion_l2_weight1/training' %}
                        <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" />
                    {% endif %}
                {% endfor %}
            </details>    
        - <details style="margin-top:0px; width:1000px">
                <summary>Test</summary>
                {% for image in site.static_files %}
                    {% if image.path contains 'MRI_cont3_motion_l2_weight1/test' %}
                        <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" />
                    {% endif %}
                {% endfor %}
            </details>    
    - Again....WHY!(╯°Д°）╯︵ 



## Log
### 2018-09-30
- Create FIle
