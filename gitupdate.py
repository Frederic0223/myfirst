#初始化倉庫
git init
#查看狀態
git status
#把所有  工作区的文件存到 暂存区
git add .
#init  是提交记录的名字  师父父可以随便写 绿的 就表示 存到 暂存区啦
 git commit -m 'init'
#link to my github
git remote add origin https://github.com/Frederic0315/myfirst.git

git push -u origin master
git push --set-upstream origin master

#if shows: ! [rejected] master -> master (fetch first) error: failed to push some refs to 'https://github.com/Frederic0315/myfirst.git' then run follows:
git fetch origin master
git merge origin master
git fetch origin master:tmp
git rebase tmp
git push origin HEAD:master
git branch -D tmp

#or you can:第一次要连接一下远程仓库 之后就是 git add   git commit   git push 这仨就好了
git rm --cached <D:\Documents\PythonLearning>
git add .
git commit -m "<your_message>"
git push --all
#use this is sufficient
git add .
git commit -m "<your_message>"
git push