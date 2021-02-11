===========
Task 3: TDD
===========

Now we would like to implement something from scratch. Therefore it is the
perfect opportunity to try some test driven development.

Crop an Image
-------------

Your task is to implement a functionality that crops an image.

Hints
-----

As we are doing TDD you need to start with the unit test. To keep things simple
in the first place create a unit test in *test_processing.py*.

Try to think of a very simple image and a very simple crop. You might want to
copy some parts of the other unit test.

Once you have a first unit test for the pure cropping function, you can start
with a unit test for the command line interface. The command line interface
can be found in *cli.py*. The unit test for it can be found in *test_cli.py*.