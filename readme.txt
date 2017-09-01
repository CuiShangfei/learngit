Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.

从历史的提交建立新分支的方法：
方法一： checkout到历史提交，然后checkout -b。
方法二： reset到历史提交，checkout -b，然后再reset到原来的版本。
方法三： git branch <branch> <start point>

将某个历史版本全部拉到工作区和暂存区：
方法一： 可能的需求是为了将过去删除掉的修改重新应用到最新的版本，这时可以先回到历史版本处建立分支，然后回到原来的最新的版本，进行merge分支的操作。
方法二： reset加上hard参数到需要的历史版本，然后再reset加上soft参数回来。

将历史版本的某文件版本拉到当前工作区或者暂存区进行处理：
方法一： git reset HEAD~2 foo.py，直接拉到暂存区。
方法二： git checkout HEAD~2 foo.py，拉到工作区和暂存区。

已经有添加到暂存区的文件修改，之后又进行了修改。想要都撤销掉，变为和仓库中的版本相同（仓库覆盖工作和暂存）：
方法一：1、git reset HEAD file 清空暂存区的提交，变为和仓库中的版本相同。2、git checkout  --  file 以暂存区为蓝本，覆盖掉工作区。
方法二：git checkout HEAD --  file 。

已经添加到暂存区的修改之后又进行了修改，想要都撤销掉，变为和仓库中的版本相同（仓库覆盖工作和暂存）：
方法一：git reset --hard HEAD 重设HEAD，hard参数覆盖工作区和暂存区。
方法二：强制切换到其他分支丢弃更改，然后再切回来。

撤销当前工作区的文件修改，变为和暂存区相同（暂存覆盖工作）：
方法一：git checkout -- file 暂存区覆盖工作区(以暂存区为蓝本，覆盖掉工作区)。

撤销添加到暂存区的文件修改，将修改退回到工作区（暂存先覆盖工作，然后仓库覆盖暂存）：
方法一：1、git checkout  --  file 以暂存区为蓝本，覆盖掉工作区。 2、git reset HEAD file 清空暂存区的提交，变为和仓库中的版本相同。

清空暂存区文件修改：
方法一：git reset -- file 清空暂存区的文件修改。

清空暂存区：
方法一：git reset HEAD file 清空暂存区。

checkout文件层面的操作：
主要对暂存区和工作区起作用，一般有暂存区覆盖工作区的行为特征。

reset文件层面的操作：
主要对暂存区起作用。

Creating a new branch is quick & simple.

Git鼓励大量使用分支：

查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>

创建+切换分支：git checkout -b <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>



要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；

关联后，使用命令git push -u origin master第一次推送master分支的所有内容；

此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；


