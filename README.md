# Test These Katas
The [katas.py](katas.py) file includes our solution to the prior activity [Functions and Loops](https://github.com/KenzieAcademy/backend-katas-functions-loops).

Unfortunately, while we had good intentions and wrote a [test
harness](./tests), we didn't actually write any unit tests!

## Getting Started
There are several ways to start this activity, but we suggest that you start
by running the unit tests in a separate terminal (like the one built into VS
Code) using `rerun`:

```console
% rerun "python -m unittest discover"
```

You should see something like the following:

![failing output](./screenshots/failing.png)

Then, open up [tests/test_katas.py](./tests/test_katas.py) and start fixing those TODOs!

Once complete, you should see the following test output:

![passing output](./screenshots/passing.png)
