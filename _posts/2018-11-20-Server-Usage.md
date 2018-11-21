---
layout: post
title: CIG Server Usage
category: MRI Denoising
excerpt_separator:  <!--more-->
---

<!-- <img src="{{ site.baseurl }}{{ image.path }}" alt="image" style="float: left; vertical-align: text-top;" /> -->

# Abstract
This is a note for using the CIG's server and university virtual Linux lab. 
<!--more-->

- [Abstract](#abstract)
- [1 CIG Server](#1-cig-server)
    - [1.1 Request for Permission and Install Cisco AnyConnect](#11-request-for-permission-and-install-cisco-anyconnect)
    - [1.2 SSH to Server](#12-ssh-to-server)
        - [1.2.1 Linux Users](#121-linux-users)
        - [1.2.2 Windows 10 Users](#122-windows-10-users)
        - [1.2.3 Other Windows Version Users](#123-other-windows-version-users)
    - [1.3 SSHFS to Server](#13-sshfs-to-server)
        - [1.3.1 Linux Users](#131-linux-users)
        - [1.3.2 Windows 10 Users](#132-windows-10-users)
- [2 University Linux Lab](#2-university-linux-lab)
    - [2.1 Create Linux Session](#21-create-linux-session)
    - [2.2 Start VNC](#22-start-vnc)
    - [2.3 SSH to Server](#23-ssh-to-server)
    - [2.4 SSHFS to Server](#24-sshfs-to-server)
    - [2.5 Cancel](#25-cancel)

# 1 CIG Server
## 1.1 Request for Permission and Install Cisco AnyConnect
Please ask the professor for permission to access to server. After being permitted, you can go to [Engineering IT](https://engineering.wustl.edu/our-school/leadership/offices/engineering-it/networks-remote-access/Pages/vpn.aspx) and follow the guide to install Cisco AnyConnect, the VPN software. Everytime you want to access to server, you need to start VPN first. And remember to select ```keyvpn``` in the ```Group`` option.
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/AnyConnect-Linux.png"/></center> 
<p style="text-align: center;"> Linux AnyConnect Client </p>  
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/AnyConnect-Win.png"/></center>
<p style="text-align: center;"> Windows AnyConnect Client </p>  

## 1.2 SSH to Server
This section will guide you to open a shell on the server.

### 1.2.1 Linux Users
Linux user can simply use ```SSH``` to open a shell on the server:
```bash
ssh <your WUSTL Key>@cigserver<1 or 2>.seas.wustl.edu
```
Then the server should ask you for your password, which is the same to your WUSTL account password. To avoid inputing password every time, you can following the guidenc in (this page)[https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604] to generate a RSA pair and send it to the server.

What's more, I recommend to add the ```-X``` option to enable you to run GUI programs:
```bash
ssh -X <your WUSTL Key>@cigserver<1 or 2>.seas.wustl.edu
```
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/sshX-Linux.png"/></center>
<p style="text-align: center;"> Running MATLAB </p>  

### 1.2.2 Windows 10 Users
For windows 10 users, I strongly recommend to use the windows Linux subsystem (WSL), which will make things a lot easier. You can follow this [offical guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install your favorite Linux distribution on windows. And the note is based on Ubuntu 16.04 LTS. Now you can use exact same method to ```SSH``` to the server:
```bash
ssh <your WUSTL Key>@cigserver<1 or 2>.seas.wustl.edu
```
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/SSH-Win-WSL.png"/></center>
<p style="text-align: center;"> SSH on WSL </p>  

However, you cannot directly use ```-X``` to enable GUI program since windows does not have XServer. There are many XServer software on windows, this note will be based on Xming. After installing and starting Xming, you can run this code to tell WSL where to find the XServer (run this on your local machine instead of ont the server!):
```bash
export DISPLAY=localhost:0.0
```

Then you should be able to run GUI programs. The XServer address (```localhost:0.0```) should match the port opened by Xming, which is by default ```0.0```. If your do not want to input it everytime when your open a new WSL bash, you can save it in ```~/.bachrc```.

<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/SSH-Win-Matlab.png"/></center>
<p style="text-align: center;"> Running MATLAB on WSL </p>  
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/SSH-Win-Xming.png"/></center>
<p style="text-align: center;"> Check Xming port </p>  

### 1.2.3 Other Windows Version Users
To Be Added

## 1.3 SSHFS to Server
This section will guide you to mount server's disk to your machine, which makes it much easier to explore and edit the files on the server.

### 1.3.1 Linux Users
Linux users can simply use ```sshfs``` to mount the server (though you may install it first):
```bash
sudo sshfs -o allow_other jiarui.xing@cigserver2.seas.wustl.edu:/export/project/jiarui.xing /mnt/cigserver2_jiarui_xing/
```

Please make sure the mount path (```/mnt/cigserver2_jiarui_xing/```) already exists and you have the access. You should be able to look into the files on the server in that folder, which just looks like a local disk. The files would be downloaded when you enter a folder and deleted (on your machine) when you left, so it may be a little slow when you open a folder that contains lots of files and you don't need to worry about if you have enough free space. What's more, you can also use your RSA to skip entering password everytime by adding ```-o IdentityFile``` option:
```bash
sudo sshfs -o allow_other -o IdentityFile=/home/remussn/.ssh/id_rsa jiarui.xing@cigserver2.seas.wustl.edu:/export/project/jiarui.xing /mnt/cigserver2_jiarui_xing/
```

Replace ```/home/remussn/.ssh/id_rsa``` with your RSA path. When you finish you task, you can use ```umount``` to deiconnect the disk:
```bash
sudo umount /mnt/cigserver2_jiarui_xing
```

<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/SSHFS-Linux.png"/></center>
<p style="text-align: center;"> Using SSHFS on Linux </p>  

### 1.3.2 Windows 10 Users
Unfortunately, till now WSL doesn't support sshfs and we need to use some third-part softwares. Personally I use SFTP Net Drive, which is free for non-commerical use. Using SFTP Net Drive is fairly simple: enter the inforation,  click "connect", and you're done:

<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/SSHFS-Win-SFTPpng.png"/></center>
<p style="text-align: center;"> SFTP Net Drive Interface </p>  

<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/SSHFS-Win.png"/></center>
<p style="text-align: center;"> Using SFTP Net Drive </p>  

# 2 University Linux Lab
## 2.1 Create Linux Session
You can go to [here](https://linuxlab.seas.wustl.edu/equeue/) to create your linux session. After logging with your WUSTL key and password, you can go to "Submit Job" to submit a new linux session. For general usages, I recommend to submit a "Linux_Desktop" job. After setting parameters(you can just use the default setting), the session will be created in a few seconds and the page will let you download ```xsession.jnlp```, which is a script to run a TurboVNC.
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-welcome.png"/></center>
<p style="text-align: center;"> Welcome Page </p>  
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-submit.png"/></center>
<p style="text-align: center;"> Submit Job </p>  
  

## 2.2 Start VNC
Once you have installed Java, you can directly open ```xession.jnlp```. Java may stop you to run it for securiy issue. To resolve this problem, you can open ```Java Control Panel``` and goto ```Security``` tab, and add ```http://linuxlab.seas.wustl.edu``` to the exception site list, and then you should be able to run it.
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-java.png"/></center>
<p style="text-align: center;"> Find Java Control Panel </p>
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-java-security.png"/></center>
<p style="text-align: center;"> Security Tab </p>  
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-VNC.png"/></center>
<p style="text-align: center;"> Turbo VNC </p>  


<!-- <p> BLANK LINE</p>   -->
## 2.3 SSH to Server
Again, you can simple ssh to the server without opening a remote desktop window. Open ```xession.jnlp``` as a text file, at the last lines you would find something like ```<argument>linuxlab009.seas.wustl.edu:7</argument>```, which indicates the session you just created runs on server ```linuxlab009```. Then, you can ssh to it by simply ```ssh <your WUSTL Key>@linuxlab009```.
<center><img src="{{ site.baseurl }}/assets/imgs/Server-Usage/LL-ssh.png"/></center>
<p style="text-align: center;"> ssh </p>  


## 2.4 SSHFS to Server
Since we have found the server address in the last step, we can use the same methods used in section 1.3 to mount the server.
## 2.5 Cancel 
After finishing your task, you can go to ```Job management``` page and delete your job.