[![Build Status](https://travis-ci.com/mchirico/chocolateKata.svg?branch=master)](https://travis-ci.com/mchirico/chocolateKata)
[![Board Status](https://dev.azure.com/mchirico/61841fef-32bd-4221-900e-3067d5d7800a/f521119d-02aa-44e4-bf84-892e2da3e6a5/_apis/work/boardbadge/10e08a74-b444-4da0-950e-79233a23c099?columnOptions=1)](https://dev.azure.com/mchirico/61841fef-32bd-4221-900e-3067d5d7800a/_boards/board/t/f521119d-02aa-44e4-bf84-892e2da3e6a5/Microsoft.RequirementCategory/)

# Chocolate Kata

# Bonus Rules:

For now, the bonus packs are given afer some quantity N of
chocolates are purchased. The bonus packs are strucgtured as
follows:

1) For each N number of "milk" chocolates purchased, users earn
a bonus pack with one "milk" chocolate.

2) For each N number of "dark" chocolates purchased, users earn
a bonus pack wiht two additional "dark" chocolates.

3) For each N number of "white" chocolates purchased, users earn a
bonus pack with one "white" chocolate and one "milk" chocolate."

There is no upper limit to how many bonus packs can be earned 
per order.

Any bonus chocolates that the customer receiveds do not count 
towards the redemption of additional bonus chocolates.


### Technical acceptance criteria

When run, your program should read an orders file from
`input/orders.csv` and output a list of total chocolates of each type
per order to the stdout/terminal in the below format. 

#### Sample Input File (`input/orders.csv`)

```
type,cash,price,bonus ratio
"milk",12,2,5
"dark",13,4,1
"white",6,2,2
```

Each line represents a single order.

Each order is separate, the terms of one order odes not affect any
other orders.

Each order can only include one chocolate type.

- 'type': the type of chocolate the shopper is buying in the order
- 'cash': amount in dollars the user paid for the order
- 'price': price in dollars for 1 piece of the chocolate
- 'bonus_ratio': number of chocolcate of the type needed to earn the
chocolate's bonus pack

'cash', 'price' and 'bonus_ratio' are always whole numbers,
represented by simple unsigned integers.

### ** Expected Output (`stdout`) **

milk 7,dark 0,white 0
milk 9,dark 9,white 0
milk 1,dark 0,white 4


### Explanation of a single order:

** Input:

type,cash,price,bonus_ratio
"white",15,2,3


** Output:

milk 2,dark 0,white 9

Using the above order as an example, the shopper has $15.

Each chocolate costs $2, so the shopper is able to buy 7 white
chocolates ($15/$2)

The bonus_ratio is 3 so the user receives 2 bonus packs (7/3)

Each bonus pack for the "white" type has 1 "white" chocolate and 1
"milk" chocolate, so the user receives 2 additional chocolates of each
type, since there are 2 packs.

The user therefore receives 9 "white" chocolates, 2 "milk" chocolates,
and 0 "dark" chocolates.


### Test Code
```bash
export PYTHONPATH="${PWD}/src"
pycodestyle --statistics -qq tests/tests_block_bad_ip.py
pycodestyle --statistics -qq src/block_bad_auth.py
cd tests
pytest --cov=../ -v tests_block_bad_ip.py

```

