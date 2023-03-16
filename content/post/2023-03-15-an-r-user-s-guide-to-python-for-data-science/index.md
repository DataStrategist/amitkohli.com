---
title: an R-user's guide to Python for data science
author: Amit
date: '2023-03-15'
slug: an-r-user-s-guide-to-python-for-data-science
categories:
  - Tutorials
tags:
  - Python
---

R is for sure the best data science language period. That being said, Python is more popular... I suspect it's a priors thing (i.e. there are just a ton of Python users doing all sorts of stuff, which makes it more likely that companies will choose Python as their _de facto_ language). I will also go on the record and say that Python's NLP game is better than R's.

So little by little, I have been learning Python, and have found some parts of the process really easy, while other bits seem a bit obtuse. 

Anyway, I've been writing notes here and there, and figured I would write a guide for myself, as my personal cheat sheet. This will get updated frequently, so check back often.

Let's start off easy... here's a table of translations for common verbs (a popular NLP model maaay have given me a hand here):

# Common Verbs

## General

|R command|R description|Python command|Python description|
| ------- | ------- | ------- | ------- |
|`install.packages()`|Install an R package|`!pip install package_name`|Install a Python package using pip (although there's many ways to install packages... and it gets super messy really fast)|
|`library()`|Load an R package|`import package_name`|Import a Python package. It's typical to assign an alias here, like `import numpy as np`... and these aliases are used later. By convention, `pd` is pandas, `np` is numpy, etc|
|`data()`|Load a built-in R dataset|`from package_name import dataset_name`|Load a built-in dataset from a Python package|
|`read.csv()`|Read a CSV file|`pd.read_csv('filename.csv')`|Read a CSV file using Pandas|
|`write.csv()`|Write a data frame to a CSV file|`df.to_csv('filename.csv', index=False)`|Write a Pandas DataFrame to a CSV file|
|`head()`|View the first few rows of a data frame|`df.head()`|View the first few rows of a Pandas DataFrame|
|`summary()`|Get summary statistics of a data frame|`df.describe()`|Get summary statistics of a Pandas DataFrame|
|`dim()`|Get the dimensions of a data frame|`df.shape`|Get the dimensions of a Pandas DataFrame|
|`names()`|Get the column names of a data frame|`df.columns`|Get the column names of a Pandas DataFrame|
|`nrow()`|Get the number of rows in a data frame|`len(df)` or `df.shape[0]`|Get the number of rows in a Pandas DataFrame|
|`ncol()`|Get the number of columns in a data frame|`df.shape[1]`|Get the number of columns in a Pandas DataFrame|
|`paste()`|Concatenate strings|`''.join(list_of_strings)` or `string1 + string2` or `f'The answer to the ultimate question is {my_number}.'`|Concatenate strings in Python using join()` or `the + operator|
|`gsub()`|Replace values in a string|`str.replace(old_value, new_value)`|Replace values in a string using the replace() method in Python|
|`substr()`|Extract a substring from a string|`string[start_index:end_index]` or `string[range(start_index, end_index)]`|Extract a substring from a string in Python using indexing|
|`grep()`|Find the indices of a pattern in a vector|`[i for i, x in enumerate(list) if pattern in x]`|Find the indices of a pattern in a list in Python using list comprehension|
|`which()`|Find the indices of a logical vector that are TRUE|`np.where(array == True)`|Find the indices of True values in a NumPy array in Python|
|`sort()`|Sort a vector|`sorted(list)` or `np.sort(array)`|Sort a list or NumPy array in Python|
|`order()`|Order a vector|`np.argsort(array)`|Get the indices that would sort a NumPy array in Python|
|`max()`|Get the maximum value of a vector|`max(list)` or `np.max(array)`|Get the maximum value of a list or NumPy array in Python|
|`min()`|Get the minimum value of a vector|`min(list)` or `np.min(array)`|Get the minimum value of a list or NumPy array in Python|
|`sum()`|Get the sum of a vector|`sum(list)` or `np.sum(array)`|Get the sum of a list or NumPy array in Python|
|`mean()`|Get the mean of a vector|`np.mean(array)`|Get the mean of a NumPy array in Python|
|`sd()`|Get the standard deviation of a vector|`np.std(array)`|Get the standard deviation of a NumPy array in Python|
|`var()`|Get the variance of a vector|`np.var(array)`|Get the variance of a NumPy array in Python|
|`cor()`|Compute the correlation between two vectors|`np.corrcoef(array1, array2)`|Compute the correlation between two NumPy arrays in Python
|`class()`|... I dunno how to describe class... it gets abstract pretty quick!|`type()`||

## Tidyverse verbs

<style>
table, th, td {
  border: 1px solid black;
}
</style>
|R command|R description|Python command|Python description|
| ------- | ------- | ------- | ------- |
|`filter()`|Filter rows of a data frame based on a condition|`df[df['column_name'] == condition]`|Filter rows of a Pandas DataFrame based on a condition|
|`select()`|Select columns of a data frame|`df[['column_name1', 'column_name2']]`|Select columns of a Pandas DataFrame|
|`arrange()`|Sort a data frame|`df.sort_values('column_name')`|Sort a Pandas DataFrame by one or more columns|
|`mutate()`|Add or modify a column of a data frame|`df['new_column'] = expression`|Add or modify a column of a Pandas DataFrame using a Python expression|
|`group_by()`|Group a data frame by one or more columns|`df.groupby('column_name')`|Group a Pandas DataFrame by one or more columns|
|`summarize()`|Summarize a grouped data frame|`df.groupby('column_name').agg({'column_name': 'function'})`|Summarize a grouped Pandas DataFrame using one or more aggregation functions|
|`merge()`|Merge two data frames|`pd.merge(df1, df2, on='column_name')`|Merge two Pandas DataFrames on one or more common columns|
|`pivot_longer()` or `gather`|Transform wide data frames into long data frames by gathering multiple columns into key-value pairs.|`pandas.melt()`|Transform wide data frames into long data frames by unpivoting multiple columns into key-value pairs.|
|`pivot_wider()` or `spread()`|Transform long data frames into wide data frames by spreading values of one column into multiple columns.|`pandas.pivot_table()`|or pandas.pivot()|Transform long data frames into wide data frames by pivoting values of one column into multiple columns.|
|`separate()`|Split a column into multiple columns based on a separator.|`pandas.str.split()`|Split a column into multiple columns based on a separator using the str.split()|method in pandas.|
|`unite()`|Combine multiple columns into a single column with a separator.|`pandas.Series.str.cat()`|Combine multiple columns into a single column with a separator using the str.cat()|method in pandas.
|`map()`|Apply a function to each element of a list/vector and return a list|`map()` (from the toolz or more_itertools module) or `list(map())` or use "list comprehension"... see below|Apply a function to each element of an iterable and return a list|
|`pmap()`|Apply a function to corresponding elements of multiple lists/vectors and return a list|`list(starmap())`|Apply a function to corresponding elements of multiple iterables and return a list|

List Comprehension: In Python, list comprehension is a cool way to map through inputs. It allows you to create a new list by applying an operation to each element of an existing list, for example:

```
# create a list of even numbers from 0 to 10
even_numbers = [x for x in range(11) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10]
```

## Indexing

Speaking of zero... Python starts from `0`, not `1`, which means that everything starts from zero! This WILL trip you up for a while, and then it will be fine but will still make you pretty furious. Be warned

## Functions vs attributes

As you may have noticed in the examples above, there's some weird stuff going on in terms of sometimes functions going around the variable like `fun(x)` and other times it being all `x.fun`?

Like what's this all about:

```
import pandas as pd

data = {'name': ['John', 'Jane', 'Bob'],
        'age': [30, 25, 40],
        'city': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

df.shape # (3, 3)
len(df) # 3
```

See how `shape` comes after, but `len` comes before the `df`? That drove me crazy!!

Turns out that `shape` is an **attribute** of the pandas DataFrame object, and therefore it takes the syntax `df.shape`.

On the other hand, `len()` is a built-in Python function. It's not specific to pandas DataFrames, but it works with any object that has a length. In the case of the DataFrame object, `len()` returns the number of rows in the DataFrame as you would expect, but `len()` is not an attribute of the DataFrame object.

This is I guess a bit similar to R6 syntax in R? But I don't use R6 that much, so this was different and new to me.

I mean, I guess it's cool that objects have their own functions. Here are some useful ones that DataFrames have:

 - `Shape`: returns a tuple representing the dimensions of the DataFrame, with the number of rows and columns. You can then subset this to get the number of rows or columns... as you saw above.
 - `Columns`: returns a list of the column names in the DataFrame.
 - `Index`: returns the row index of the DataFrame.
 - `dtypes`: returns the data type of each column in the DataFrame.
 - `T`: returns a transposed version of the DataFrame
 - `iloc`: allows you to access the rows and columns of the DataFrame by their integer position.
 - `loc`: allows you to access the rows and columns of the DataFrame by their labels.
 - `head()`:returns the first n rows of the DataFrame.
 - `tail()`:returns the last n rows of the DataFrame.
 - `describe()`: provides a summary of the statistics of the numerical columns in the DataFrame
 - `info()`: provides information about the DataFrame, including the data types of each column and the number of non-null values.
 
Here are some other examples that might be useful to a data scientist:

 - NumPy arrays: NumPy arrays are used extensively in scientific computing and data analysis in Python. They have attributes like `shape`, `size`, `dtype`, `ndim`, and `data`, which can provide information about the array's dimensions, data type, and memory layout.

 - Matplotlib figures: Matplotlib is a popular plotting library in Python. Matplotlib figures have many attributes, such as `size`, `axes`, `title`, `labels`, and `legends`, which can be used to customize the appearance of the plot.

 - SciPy sparse matrices: SciPy is a library for scientific computing in Python. Sparse matrices in SciPy have attributes like `shape`, `nnz`, `data`, and `indices`, which can provide information about the matrix's sparsity and data structure.

 - TensorFlow tensors: TensorFlow is a popular library for deep learning in Python. Tensors in TensorFlow have attributes like `shape`, `dtype`, and `device`, which can provide information about the tensor's dimensions, data type, and device placement.

 - PyTorch tensors: PyTorch is another deep learning library. Tensors in PyTorch have attributes like `shape`, `dtype`, and `device`, which are similar to those in TensorFlow. Additionally, PyTorch tensors have a `requires_grad` attribute, which is used for automatic differentiation in neural networks.

## Structure

OK, there's a bit of a difference in the objects that Python uses as well... here's the skinny:

### Set

Sets are like vectors, but they are surrounded by curly brackets:

```
# Defining a set in Python
my_set = {1, 2, 3}
```

There are advantages to using sets... but let's ignore that for now. I don't think these are very commonly used in data.science?

### Tuples

Tuples are kinda like vectors, but can contain multiple classes... so like R lists.

```
# example of a tuple
thingie = (3, 4)

# example of a tuple representing a record
person = ('John', 'Doe', 30, 'Male')
```

### Lists

Python lists are like unnamed R lists. They also can contain multiple classes

```
# example of a list
my_list = [1, 2, 3, "four", True, ["nested", "list"]]
```

I asked a certain AI when to use tuples vs lists, and here's what it said:

>In Python, both lists and tuples are used to store collections of items. However, there are several differences between them:

>Mutability: Lists are mutable, which means you can add, remove or modify elements after the list is created, while tuples are immutable and cannot be changed once they are created.

>Syntax: Lists are defined using square brackets [] while tuples are defined using parentheses ().

>Performance: Tuples are generally faster than lists because they are simpler and smaller in size. This means that if you are working with a large dataset, using tuples instead of lists can help improve the performance of your program.

>Usage: Lists are more commonly used than tuples because they offer more flexibility due to their mutability. Tuples, on the other hand, are used in situations where immutability is desired, such as when you want to store a collection of items that should not be changed, or when you need to use a collection as a dictionary key.

Ok... so tuples are like simple unnamed R lists, and Lists are more complex and have a different syntax. Cool!

### Dictionaries

Dictionaries are like R named lists. Since they associate values with keys, they are more efficient than searching through Python lists or tuples. So basically, dictionaries are like JSON or something.

```
# example of a dictionary
ages = {'John': 30, 'Jane': 25, 'Bob': 40}
```

### Pandas DataFrames

Yeaaah, finally! We know what a DataFrame is! But this isn't a Python invention, it came from R and only exists through pandas. You're welcome Pythonistas!

Let's look through some examples of how to play w/ DataFrames since that's kind of a big deal.

```
# example of creating a pandas DataFrame from a dictionary
import pandas as pd

data = {'name': ['John', 'Jane', 'Bob'],
        'age': [30, 25, 40],
        'city': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)


# example of filtering a pandas DataFrame
filtered_df = df[df['age'] > 28]
print(filtered_df)

# example of grouping and aggregating a pandas DataFrame
grouped_df = df.groupby('city').agg({'age': 'mean'})
print(grouped_df)
```

## Converting

OK, in the example above, we saw how to convert a dictionary into a DataFrame. Let's look at some other ways of converting from one object type to another.

```
my_python_list = [1, 2, 3]
my_tuple = tuple(my_python_list)
```

Similarly, to convert a tuple to a list, you can call the list() constructor function:

```
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
```

To convert a dictionary to a list of tuples, you can use the items() method of the dictionary, which returns a view object that can be converted to a list:

```
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = list(my_dict.items())
```

To convert a list of tuples to a dictionary, you can use the dict() constructor function with the list as its argument:

```
my_list = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(my_list)
```

## Brackets, indenting and quotes

Let's pay more attention to brackets. In Python, square brackets `[]` are used for indexing and slicing, just like in R. For example:

```
# Indexing a list in Python
my_list = [1, 2, 3, 4, 5]
my_list[0]  # Returns the first element, equivalent to my_list[1] in R because of Zero indexing!

```

Curly brackets {} are used for defining sets, dictionaries, and for defining blocks of code. For example:

```
# Defining a set in Python
my_set = {1, 2, 3}

# Defining a dictionary in Python
my_dict = {"name": "John", "age": 30}

# Defining a block of code in Python (note how we're specifying what is run under each condition using indents!)
if x > 0:
    print("x is positive")
else:
    print("x is negative")
```

Parentheses () are used for calling functions and methods, and for grouping expressions, just like in R. For example:


```
# Calling a function in Python
my_list = [1, 2, 3]
len(my_list)  # Returns the length of the list, equivalent to length(my_list) in R

```

and what about quotes? When should I be using single quotes, double quotes, or backticks in Python? The good news is that `'` and `"` are interchangeable, just like in R.

However, the backticks are not used to define string literals like in R.

## Function writing

So in Python, functions are defined w/ `def` rather than `function`, and the error tolerance is baked into the function typically. I kinda like this better than `try` or even `safely` because it keeps all the logic in one place. I guess it's six of one and half-dozen of the other... I'm just trying to give props to Python whenever I can :D


The general structure is as follows:

```
def my_function(arg1, arg2):
    try:
        # code that may raise an error
        result = arg1 / arg2
        return result
    except:
        # code to handle the error
        return None
```

In this example, the `try` block contains the code that may raise an error, while the `except` block contains the code to handle the error. If an error occurs in the `try` block, the code in the `except` block will be executed, and the function will return `None`.

You can get more specific too, like we can specify the type of error in the `except` block. For example:

```
def my_function(arg1, arg2):
    try:
        # code that may raise an error
        result = arg1 / arg2
        return result
    except ZeroDivisionError:
        # code to handle the ZeroDivisionError
        return None
    except TypeError:
        # code to handle the TypeError
        return None
```

In this example, the function will handle a ZeroDivisionError or a TypeError differently.

## Running stuff

Now, if you're starting off in Python, chances are you're going to be running Jupyter, more or less a Rmarkdown-looking thing, which allows you to define if each block is a code-blocks, or text. It's kinda cool... has a bunch of shortcuts that make working with it fairly tolerable.

As you get more serious though, you might start writing Python code that needs to run in a crontab, or an API or in general more complex stuff... in these cases, you'll need to write a plain python file. The structure here is a bit different... you get to specify _when_ different bits of code get run.

You specify what you would like to run when the script is called directly (rather than imported in as you would w/ `source()` or something in R) by defining that code as follows:

```
if __name__ == "__main__":
    # code to execute when script/module is run directly
```

Considering that production code typically consists of a bunch of functions and what have you, it's typical to import libraries at the top, organize functions after that, and then at the end you can have your bit that checks if the script is being called directly, in which case it will execute code in the above mentioned conditional.

Takes a bit of getting used to, but it's not bad.



## Other stuff

So apparently, it's common practice to define functions within classes... cause that will help keep common functions together. This is more than a convenience, remember that in Python, objects _contain_ certain functions and what have you. Consider the following example:

```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

In this example, we define a Rectangle class that has an __init__ method to initialize the width and height of the rectangle. We also define two methods, area and perimeter, that calculate the area and perimeter of the rectangle, respectively. By defining these methods within the Rectangle class, we can easily create instances of rectangles and calculate their properties without having to write separate functions to do so. For example, we could create a rectangle object and calculate its area and perimeter like this:

```
r = Rectangle(5, 10)
print(r.area())        # Output: 50
print(r.perimeter())   # Output: 30
```

Which is pretty cool actually!


## In conclusion

I mean... there's some cool stuff here, no denying it. I do think that perhaps more data scientists should be versed in both languages. 

I'll be updating this list as I go... please do leave a comment if anything needs to be corrected or if I missed anything important!


