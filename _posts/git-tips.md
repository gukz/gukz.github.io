## pro git
### git hooks
.git/hooks/ 钩子文件写完后需要修改权限为可执行 
### git config
```bash
git config            这个项目
git config --global   当前登录用户
git config --system   这台计算机
配置生效优先级:  git config > --global > --system
git config [_ --global --system] user.name gukz
git config [_ --global --system] user.email 1685605435@qq.com
git config [_ --global --system] core.editor vim
git config --list [_ --global --system]     查看所有git的配置
git config -e [_ --global --system]         打开配置文件
git config [_ --global --system] user.email 查看当前的user.email
```
### gitignore
- *.a
- !lib.a
- __pycache__/
### 常用操作注意事项
```bash
git mv <filename>            相当于执行以下三条命令
    mv <filename_o> <filename_n>
    git rm <filename_o>
    git add <filename_n>
git status -sb               只显示简略的信息
git log -p                   显示每次提交之间的修改
git log --stat               显示简略的文件修改统计信息
git log --pretty=format:"%h  %an" 格式化log的输出信息
git log --graph --oneline    简略图形化显示
```
### 撤销操作
```
  HEAD              Index            WorkDir
  分支 <- commit <- 暂存区 <- add <- 本地修改
```
```bash
git reset --soft HEAD~1      回滚HEAD, 与git commit --amend 作用类似
git reset [--mixed] HEAD~1   回滚HEAD, Index 默认
git reset --hard HEAD~1      回滚HEAD, Index, WorkDir [危险]
git reset fileA              回滚Index
git reset 38eb94 -- fileA    使用38eb94的fileA替换Index中的文件
git reset --soft HEAD~n, git commit 压缩最近n个提交为一个
git checkout -- <filename>   丢弃本地单个文件的修改
git checkout -f              丢弃暂存区和本地的修改, 恢复至commit状态
git commit --amend           将暂存区的修改覆盖提交
```
### 远程仓库操作
```bash
git fetch --all              抓取远程仓库的最新数据
git remote add <shortname default=origin> <url> 添加远程仓库, 如果url是本地仓库, 会把本地仓库上传到远端
git remote rename <name1> <name2> 修改远程分支名称, origin->orange
git remote rm <name> 删除远程仓库
```
### 打标签
```bash
git tag 1.1.1                轻量标签
git tag -a 1.1.1             含有批注的标签
git tag -a 1.0.9 9fceb02     给历史分支补打标签
```
### git 命令别名
```bash
git config --global alias.unstage 'reset HEAD --' 
git congit --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit 
git config --global alias.st status
```
### git 分支, 跟踪远程分支(支持git pull push)
```bash
git branch -vv               查看所有本地分支跟踪的分支情况
git branch -u origin/bra2    任何时刻修改本地分支关联的远程分支 -u=--set-upstream-to
git checkout -b branch1      本地新建一个分支, 并切换
git checkout -b branch1 origin/bra2 本地新建一个分支,跟踪远程分支 git pull
git push origin branch       把当前分支推送到远程分支branch
git push origin --delete bra2 删除远程分支
```
### 变基(git 整合不同分支的修改主要有 merge, rebase merge) 不要对别处有副本的分支进行变基
```bash
merge bra 将当前分支和bra和公共祖先进行三方合并,合并的结果作为当前分支的一个新的提交, 有分叉
rebase bra,merge bra                  将bra序到当前分支的后面. 之后再merge bra, 不再有分叉
rebase bra brb,co bra,merge brb       将brb的修改序到bra的后面
git rebase --onto bB bC,merge bC   找出bC相对于bB公共祖先之后的修改, 在当前分支上重播
```
### 使用git的协议 HTTP ssh

### git工具
```bash
git stash                        暂存没有commit的已跟踪文件的修改
git stash list                   查看所有暂存
git stash apply                  应用暂存
git stash -u                     暂存所有文件的修改
git stash --all                  暂存所有文件的修改, 包括忽略的文件和未跟踪的文件
git stash branch brA             根据暂存文件生成一个新分支
git clean -f -d                  移除未跟踪未忽略和空子目录
git clean -x                     移除包括忽略名单上的文件
git clean -sfd                   删除任何忽略或未被跟踪的文件
git grep [_ --count] fileContent 查找文件内容 
git cherry-pick b4sc23           手动合并任意一个提交
git blame -L 12,22 simple.py     查看文件第12-22行的修改信息
git mergetool --tool=vimdiff3    使用vimdiff工具来显示冲突
```
### 重写历史
```bash
git commit --amend               覆盖最近一次提交的快照
git rebase -i HEAD~n   改写最近n次提交, 在最近第n+1次提交上依次重演所有提交
git filter-branch -f --commit-filter '
    if ["$GIT_AUTHOR_EMAIL" = "aa@bbb.ccc"];
    then
        GIT_AUTHOR_NAME="gukz";
        GIT_AUTHOR_EMAIL="1685605435@qq.com";
        git commit-tree "$@";
    else
        git commit-tree "$@";
    fi' HEAD                           批量修改历史提交的邮箱和用户名
```
