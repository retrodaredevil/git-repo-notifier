# Git Repo Notifier


### Setup
When you clone a repository, if it is private, you should do something like this if you need to specify a certain key.
(Usually you'll just use your regular ssh key, so it's fine without the extra parameter)
```
git clone git@private-repo-asdf.git --config core.sshCommand="ssh -i ~/Programming/git-repo-notifier/my_ssh_key"
```
Thanks https://stackoverflow.com/a/59074070/5434860
