# Sample apple.com UI autotest project

Just a sample project testing main purchase flow of apple.com website

## Description

Testing main purchase flow starting from the main page and failing with card payment

## Getting Started

### Dependencies

Please check requirements file

### Installing

Simply clone this repo and install required packages
```
$ git clone https://github.com/PurePX/sample_autotest_proj.git
$ cd sample_autotest_proj
$ pip install requirements.txt
```

### Running autotests

* Use pytest run
```
$ pip -m pytest -s -v
```

## Help

* For debugging purposes I recommend you to add "test_buy_flow()" line to a very end of tests/test_buy_flow_declined_card.py file and run standart debugging
* This autotest is not 100% stable due to website complexity. Here is the last stats:
```
====== 12 failed, 88 passed in 10490.94s (2:54:50) ======
```
