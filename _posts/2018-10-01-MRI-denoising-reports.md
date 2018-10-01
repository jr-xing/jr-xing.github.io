---
layout: post
title: MRI Denoising Project Report Files
category: MRI Denoising
excerpt_separator:  <!--more-->
---
<style>
.parameter{font-size:15px; background-color:rgb(230, 230, 230); padding:10px}
</style>
<!-- https://stackoverflow.com/questions/17677094/jekyll-for-loop-over-all-images-in-a-folder -->
## Files

<ul>
{% for file in site.static_files %}
{% if file.path contains 'files/denoising' %}
	<li><a href="{{ site.baseurl }}{{ file.path }}">{{ file.name }}</a></li>
{% endif %}
{% endfor %}
</ul>
