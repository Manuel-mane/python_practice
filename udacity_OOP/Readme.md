# Practice Outline

   In this practice repository, he following topics are covered:
   
   Object-oriented programming syntax:
        
        * classes, objects, methods and attributes
        * coding a class
        * magic methods
        * inheritance

   Use of object-oriented programming to make a Python package:
    
        * making a package
        * putting your package on PyPi

### Uploading a package on PyPi

1. You'll need to register separately at each website: [PyPi](https://pypi.org/) and [PyTest](https://test.pypi.org/). If you only register at Pypi, you will not be able to upload to the testPyPi repository.
`Note`: Remember that your package name must be unique. If you use a package name that is already taken, you will get an error when trying to upload the package.

2. The following link has a good tutorial of how to submit your Python packages in PyPi including many configuration options for your setup.py file: [tutorial on distributing packages](https://packaging.python.org/tutorials/packaging-projects/). In exchange for the python command to run the setup.py you can use the following:

`python3 setup.py sdist bdist_wheel` 

3. To know more about PyPi, you can hit the following link:
* [Overview of Pypi](https://docs.python.org/3/distutils/packageindex.html)
 
