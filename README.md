# What is it?
A repo used to maintain scores of badminton of a club

## How to install and develop?

```
git clone git@github.com:vinodsaikumar/baddy-scores.git
cd baddy-scores
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

## How to update scores?

Add an entry to games.csv and run install.sh

## Games CSV explained

ex: 1,2,3,4

* comma separated player ids
* The first 2 digit players(1,2) team have beaten the next 2 (3,4)




