---
layout: post
title: CIG Server Usage
category: CIG
excerpt_separator:  <!--more-->
---

<!-- <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" /> -->

# Abstract
This is a note for using the CIG's server and university virtual Linux lab. 
<!--more-->

# 1 CIG Server
## 1.1 Request for Permission and Install Cisco AnyConnect
## 1.2 SSH to Server
## 1.3 SSHFS to Server


# 2 University Linux Lab
## 2.1 Create Linux Session
You can go to [here](https://linuxlab.seas.wustl.edu/equeue/) to create your linux session. After logging with your WUSTL key and password, you can go to "Submit Job" to submit a new linux session. For general usages, I recommend to submit a "Linux_Desktop" job. After setting parameters(you can just use the default setting), the session will be created in a few seconds and the page will let you download ```xsession.jnlp```, which is a script to run a TurboVNC.
<img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-welcome.png" alt="image" style="float: left; vertical-align: text-top;" />
<p style="text-align: center;"> Welcome Page </p>  
<img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-submit.png" alt="image" style="float: left; vertical-align: text-top;" />
<p style="text-align: center;"> Submit Job </p>  
  

## 2.2 Start VNC
Once you have installed Java, you can directly open ```xession.jnlp```. Java may stop you to run it for securiy issue. To resolve this problem, you can open ```Java Control Panel``` and goto ```Security``` tab, and add ```http://linuxlab.seas.wustl.edu``` to the exception site list, and then you should be able to run it.
<img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-java.png" alt="image" style="float: left; vertical-align: text-top;" />
<p style="text-align: center;"> Find Java Control Panel </p>
<img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-java-security.png" alt="image" style="float: left; vertical-align: text-top;" />
<p style="text-align: center;"> Security Tab </p>  
<img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-VNC.png"/>
<p style="text-align: center;"> Turbo VNC </p>  


<p> BLANK LINE</p>  
## 2.3 SSH to Server
Again, you can simple ssh to the server without opening a remote desktop window. Open ```xession.jnlp``` as a text file, at the last lines you would find something like ```<argument>linuxlab009.seas.wustl.edu:7</argument>```, which indicates the session you just created runs on server ```linuxlab009```. Then, you can ssh to it by simply ```ssh <your WUSTL Key>@linuxlab009```.
<img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-ssh.png" alt="image" style="float: left; vertical-align: text-top;" />
<p style="text-align: center;"> ssh </p>  


## 2.4 SSHFS to Server
Since we have found the server address in the last step, we can use the same methods used in section 1.3 to mount the server.
## 2.5 Cancel 
After finishing your task, you can go to ```Job management``` page and delete your job.