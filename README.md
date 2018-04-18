# Gonance

### Development (OS X)

```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
ln -s /usr/local/bin/python3 /usr/local/bin/python
ln -s /usr/local/bin/pip3 /usr/local/bin/pip
pip install --user pipenv
git clone https://github.com/gobeltri/gonance.git
cd gonance
pipenv install   ## Patience is king
pipenv shell
```