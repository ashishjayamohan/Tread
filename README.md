# Tread 
![Logo](https://raw.githubusercontent.com/ashishjayamohan/Tread/logos/icons/logo.svg)
## A python data science package for people who just want to get on with life.
![Issues Shield](https://img.shields.io/github/issues/ashishjayamohan/Tread)
![Forks](https://img.shields.io/github/forks/ashishjayamohan/Tread)
![Stars](https://img.shields.io/github/stars/ashishjayamohan/Tread)
![License](https://img.shields.io/github/license/ashishjayamohan/Tread)

## What is Tread?
Tread is a data science package built in Python 3 that has functions that are useful for every data scientist.

## How do I work with Tread?
To get started with Tread, first ensure that your computer has Python installed. You can check this by typing `python --version` in your command line. Once you have Python installed, install pip (`pip install pip`) and instal MatPlotLib (`pip install matplotlib`). Now download the source code for this project on to your computer. You are now ready to start using Tread!

## Using Tread
Once you have installed the Tread project source code on your computer and downloaded all necessary components, simply import whichever function script you require and you can begin using all the functions that are in those function scripts. For a general overview of how this works, see `test_program.py` for an example usage of the `add` method from `basic_functions.py`.

## Tread's Functions
Tread has an ever-growing list of functions that are stored in seperate files. Namely, these are `basic_functions`, `file_processing_functions`, `graphing_functions`, `matrix_functions`, `vectorization_functions`. Each one of these hasfunctions that are generally related to their script files' name.
### basic_functions
* add() - Takes the sum of all elements in an array
* average() - Returns the average of a given array
* types() - Returns the type of every element in a given array
* highest_frequency() - Returns the value(s) and frequencies of the most frequent elements
* frequency() - Returns a dictionary with every unique element in a given array and its respective frequency
* determine_mode() - Assists in determining which mode is used for functions such as add()
* median() - Returns the median of a given data set
* mode() - Returns the numerical mode of a specific data set
* length() - Returns the length of a given array
* pare_unique() - Returns an array with only unique elements of a given array
### file_processing_functions
* read_csv() - Given a file path, will read comma seperated values
* read_file() - Given a file path, will read lines of file with  custom delimiter
* write_csv() - Takes a given matrix and writes to a given file path in CSV format
* write_file() - Takes a given matrix and writes to a given file path with custom delimiter between elements
### graphing_functions
* graph_frequency_histograms() - Given an array, will graph a histogram
* graph_scatter() - Given a list of X and Y coordinates, will graph a scatter plot
* midpoint() - Given two points, returns the coordinates of the midpoint of the line segment
* distance() - Returns the distance between two given points
### matrix_functions
* determinant() - Returns the determinant of a given matrix
* make_matrix() - Copies a given matrix into a new matrix
* multiply() - Multiplies two given matrices together and returns resultant matrix
* element_wise_multiply() - Multiplies every element in a given matrix with every element in another given matrix
* add() - Adds together two given matrices and returns resultant matrix
* subtract() - Subtracts one matrix from another and returns resultant matrix
* divide() - Divides one given matrix by another given matrix and returns resultant matrix
* add_column_values() - Adds a new column to a given matrix given the new columns' values
* remove_column() - Removes a certain indexed column from a given matrix
* extract_column() - Returns an array with given columns' values from a given matrix
* vector_function_column() - Given a table, function, and specified index, will return the function applied on elements in column
### vectorization_functions
* cumulative_sum() - Returns an array with every element having the sum of all elements prior
* skew() - Returns the skew of a given data set
* vector_functions() - Given an array and a function, will perform function on every element in array
* cast_all() - Given an array and a type, will cast all values of array into given type
### math_functions
* add_num() - Given two numbers `a` and `b`, this function will return the sum of these two numbers
* subtract_num() - Given two numbers `a` and `b`, this function will return `a-b`
* abs_diff() - Given two numbers `a` and `b`, this function will return the absoluted difference of the two numbers

## Tests
We make our best effort to add tests to `tests.py` in the `scripts` folder as frequently as possible. By running this Python script file, you can run all the tests to check that Tread's source code is working correctly and it is properly configured on your computer. If you run in to any problems, please either file an issue on Github, make a Pull Request if you can solve the issue, or [email me](mailto:ashishjayamohan@gmail.com). Alternatively, if you find a loophole in our function by implementing a test, please submit your Pull Request and make sure to [contact me](mailto:ashishjayamohan@gmail.com).

## Contributions
Please see `GUIDELINES.md`.

## Improvements to Tread
As with every other project, Tread will continue to evolve over time. If you have questions regarding the project or want to add something new, [email me](mailto:ashishjayamohan@gmail.com). You can also see what we're working on currently on our [Trello board](https://trello.com/b/0RSsd0EO/tread). Thank you for helping make Tread better for everyone!

ashishjayamohan
