# Git

1、安装好Git

2、创建git仓库

​	在git终端进入， 想创建仓库的路径（拿immortal举例）

```git
mkdir immortal
cd immortal
git init	#初始化为git仓库
```

3、在仓库中添加文件

​	首先创建好一个文本文档里面随便写点东西（比如immortal文档）

```git
git add immortal
git commit -m "这里写的是提交说明"
```

遇到提交邮箱和用户名提示解决办法如下:

```git
$ git init	#初始化
$ git config user.name "用户名"
$ git config user.email "邮箱"
```

然后可以继续提交

```git
git add 需要提交的文件
git commit -m "提交标签"
git push
```

远程删除GitHub里的文件

```git
git pull origin master	#先将仓库中的文件拉下来
git rm -r --cached 需要删除的文件	#删除磁盘上的文件
git commit -m '删除了文件'	#提交声明
入git push -u origin master	#更新到ithub仓库
```

![img](https://upload-images.jianshu.io/upload_images/13183799-5104e1cd3d16e7b0.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)