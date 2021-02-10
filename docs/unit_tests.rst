==========
Unit Tests
==========

Idea
____

We want to test a unit of code to make sure it does what we expect, i.e.

.. code-block:: python

   def test_addition():
       # given
       summands = [3, 2]

       # when
       the_sum = sum(summands)

       # then
       assert the_sum == 5

Main ingredience of a unit test

* test data
* the functionality you want to test
* meaningful assert statements

Code of Conduct
_______________

Some things to keep in mind when writing your unit tests.


+--------------------------+--------------------------+
| Does                     | Do nots                  |
+==========================+==========================+
| bring your own test data | API calls                |
+--------------------------+--------------------------+
| temporary files          | read test data from files|
+--------------------------+--------------------------+
| negative control         | mocks                    |
+--------------------------+--------------------------+
| self-sufficiency         |                          |
+--------------------------+--------------------------+
| focus on your own package|                          |
+--------------------------+--------------------------+
