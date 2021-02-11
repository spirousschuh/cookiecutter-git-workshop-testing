==================
Task 1: Unit Tests
==================

Please create a seperate branch for each of the sub-tasks and create a
Merge Request every time.
You can find detailed instructions on the :ref:`git-workflow` page.

Understand the Function
-----------------------

The repository that you created in task 0 mostly consists of two python files
*cli.py* and *processing.py*. The file *processing.py* contains a function
called *invert_image* which is not properly tested.

Try to understand what it does.

If you want more clarity on how it works, it might be a good idea to take a
look on a unit test. Try to find the unit test that corresponds the
*invert_image* function.


Extend a Unit Test
------------------


Now it is your job to change that. In the file *tests/test_processing.py* there
is a function called *test_invert_image_one_pixel*. This is a first
basic unit test you can start with.

Do not forget to create a Merge Request and merge it.


Add a Second Unit Test
----------------------

Now that we have one unit test for the function *invert_image* we want to
check if it really works properly. Therefore we want to write a another
unit test.

In the file *tests/test_processing.py* there is a function called
*test_invert_image_two_pixel*. Please use this function to write a second unit
test.