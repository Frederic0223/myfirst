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
git push --set-upstream origin master
