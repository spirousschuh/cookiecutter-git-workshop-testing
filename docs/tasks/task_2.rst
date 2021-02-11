===================
Task 2: Refactoring
===================

Please create a seperate branch for each of the sub-tasks and create a
Merge Request every time.
You can find detailed instructions on the :ref:`git-workflow` page.

Rewrite function
----------------

Now that we tested our function *invert_image* properly its time to refactor it.

Why do we want to do that? Well the package
`Pillow <https://pillow.readthedocs.io/en/stable/index.html>`_ already has this
functionality build-in. So there is no need to implement it ourself.

Now it is your turn. Please try to find the *invert* functionality of Pillow and
change the function *invert_image* such that it uses the Pillow version of
inverting an image.
