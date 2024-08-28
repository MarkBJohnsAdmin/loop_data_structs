# Loop Data Structures

We know how to loop over iterables like strings and lists, but we can also loop over more complex data types. Take this dictionary of different countries and their populations:

```py
world_pop = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21,
    ...
    "vietnam": 92.70,
    "zimbabwe": 16.15
}

# The full dictionary is in app.py
```

How would be iterate through all of the keys and values in a dictionary? You might think we could declare the key and value separately like we did for the index:

```py
for key, value in world_pop:
    print(f"{key} - population: {value} million")
    
# ValueError: too many values to unpack (expected 2)
```

But this is more than Python knows what to do with. We had to use a special `enumerate` function to get the indexes, so for loops don't come out of the box ready to reference multiple variables. But this is where we can use built in methods that come with the dictionary data type. Specifically, `.keys()`, `.values()`, and in this case, `.items()`.

The "keys" method returns a list of all a dictionary's keys, "values" returns a list of all the dictionary's values, and "items" returns the connected keys and values as a list of `tuples`. Tuples are a limited data type similar to lists, but less functional, letting them take up less memory and run faster. Tuples are "immutable", meaning their internal values can't change once they are created. They are wrapped in paratheses instead of brackets.

```py
johto_starters = {
    "chikorita": "grass",
    "cyndaquil": "fire",
    "totodile": "water"
}

johto_starters.keys()

# dict_keys(["chikorita", "cyndaquil", "totodile"])

johto_starters.values()

# dict_values(["grass", "fire", "water"])

johto_starters.items()

# dict_items([("chikorita", "grass"), ("cyndaquil", "fire"), ("totodile", "water")])
```

You can utilize these dictionary methods to run for loops on dictionaries as well:

```py
for cntry, pop in world_pop.items():
    print(f"{cntry} - population: {pop} million")
    
# afghanistan - population: 30.55 million
# albania - population: 2.77 million
# algeria - population: 39.21 million
# andorra - population: 0.08 million
# angola - population: 25.83 million
# argentina - population: 43.85 million
# armenia - population: 2.92 million
# australia - population: 24.13 million
# austria - population: 8.69 million
# azerbaijan - population: 9.65 million
# bangladesh - population: 161.2 million
# belarus - population: 9.5 million
# belgium - population: 11.31 million
# bhutan - population: 0.78 million
# bolivia - population: 11.05 million
# brazil - population: 207.65 million
# canada - population: 36.29 million
# chile - population: 17.91 million
# china - population: 1408.09 million
# colombia - population: 48.65 million
# cuba - population: 11.24 million
# denmark - population: 5.75 million
# egypt - population: 94.98 million
# ethiopia - population: 102.4 million
# france - population: 66.9 million
# germany - population: 82.79 million
# india - population: 1324.17 million
# indonesia - population: 260.58 million
# iran - population: 80.28 million
# iraq - population: 37.2 million
# italy - population: 60.6 million
# japan - population: 126.7 million
# kenya - population: 47.25 million
# mexico - population: 127.54 million
# nigeria - population: 186.99 million
# russia - population: 144.34 million
# south africa - population: 55.91 million
# spain - population: 46.56 million
# united kingdom - population: 65.64 million
# united states - population: 323.95 million
# vietnam - population: 92.7 million
# zimbabwe - population: 16.15 million
```

Note again that the variables declared in for loops are still mostly arbitrary and can be whatever you want (`k, v`, `key, value`, `foo, bar`, and so on), but it's still best practice to give them names that explain at a glance what they represent.

## Looping NumPy Arrays

Let's go back to the bmi example for NumPy arrays:

```py
import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2
```

Here, an array is practically the same as a list, so you can do a traditional for loop through the values:

```py
for val in bmi:
    print(val)
    
# 21.852
# 20.975
# 21.750
# 24.747
# 21.441
```

But NumPy lets you convert two connected arrays into a 2d NumPy array, or a matrix:

```py
np_data = np.array([np_height, np_weight])

# [[ 1.73  1.68  1.71  1.89  1.79]
#  [65.4  59.2  63.6  88.4  68.7 ]]
```

How would you loop through this?

```py
for val in np_data:
    print(val)
    
# [1.73 1.68 1.71 1.89 1.79]
# [65.4 59.2 63.6 88.4 68.7]
```

If you look at np_data, you can see it's just two arrays in side an outer array. So iterating through the outer array just returns the two arrays. Not particularly useful.

Instead, we can use a NumPy function called `nditer()`, which goes into the actual values of our sub-arrays instead of the two inner arrays themselves:

```py
for val in np.nditer(np_data):
    print(val)
    
# 1.73 - heights
# 1.68
# 1.71
# 1.89
# 1.79
# 65.4 - weights
# 59.2
# 63.6
# 88.4
# 68.7
```

Now it's printing out each of the values, starting with all of the height, and then all of the weights.

## Looping DataFrames

Let's go back to the old reliable brics.csv file:

```csv
,country,capital,area,population
BR,Brazil,Brasilia,8.516,200.4
RU,Russia,Moscow,17.10,143.5
IN,India,New Delhi,3.286,1252
CH,China,Beijing,9.597,1357
SA,South Africa,Pretoria,1.221,52.98
```

We can set up a data frame with this file, and try to iterate through the data within. First, we can try a regular for loop to see where that gets us:

```py
import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)

for val in brics:
    print(val)
    
# country
# capital
# area
# population
```

We just get the column names. Obviously we're more interested in the data nested inside these columns, so how do we get those instead? For data frames, you have to be more explicit with what you want to iterate through, and like NumPy arrays, we're given special functions we can utilize. For starters, let's use `iterrows`:

```py
for lbl, row in brics.iterrows():
    print(lbl)
    print(row)
    
# BR
# country         Brazil
# capital       Brasilia
# area             8.516
# population       200.4
# Name: BR, dtype: object
# RU
# country       Russia
# capital       Moscow
# area            17.1
# population     143.5
# Name: RU, dtype: object
# IN
# country           India
# capital       New Delhi
# area              3.286
# population       1252.0
# Name: IN, dtype: object
# CH
# country         China
# capital       Beijing
# area            9.597
# population     1357.0
# Name: CH, dtype: object
# SA
# country       South Africa
# capital           Pretoria
# area                 1.221
# population           52.98
# Name: SA, dtype: object
```

When you look directly at the brics.csv file, you can see you're looking at literal rows, which we're representing in our for loop. The 'label' is the index of the row, which we set using `index_col=0`, and the 'row' is just the rest of the data following that index.

We can also use bracket notation to only print specific data from our rows:

```py
for lbl, row in brics.iterrows():
    print(f"{lbl}: {row["capital"]}")
    
# BR: Brasilia
# RU: Moscow
# IN: New Delhi
# CH: Beijing
# SA: Pretoria
```

In addition to printing out data, you can also add data to a dataframe by using for loop. Something simple we can do just for demonstration is to add a column for the length of each country's name.

Remember that for data types with keys, you can add a new key by using bracket notation with a value that isn't already present:

```py
my_dict = {
    "name": "Mark",
    "age": 29
}

my_dict["job"] = "help"

print(my_dict)

# {
#   "name": "Mark",
#   "age": 29,
#   "job": "help"
# }
```

We can just apply this to our data frame, adding a new key to each of the Series objects by iterating through the entire data frame.

```py
for lbl, row in brics.iterrows():
    brics.loc[lbl, "name_length"] = len(row["country"])
    
print(brics)

#          country    capital    area  population  name_length
# BR        Brazil   Brasilia   8.516      200.40          6.0
# RU        Russia     Moscow  17.100      143.50          6.0
# IN         India  New Delhi   3.286     1252.00          5.0
# CH         China    Beijing   9.597     1357.00          5.0
# SA  South Africa   Pretoria   1.221       52.98         12.0
```

This works, but when working with data, performance is key. A for loop typically isn't efficient for large databases, so even though this works pretty well for a small collection of countries, this isn't a process we want to use for bigger data sets.

## Apply

If you want to add data to a data frame without having to iterate through every Series, you can instead use the `apply` method. To demonstrate this, we'll add a new column with the length of the capital instead of the country. But instead of a for loop, we just add ".apply()" to the column we want to reference, and pass a function into apply that we want to run on each of the data points:

```py
brics["cap_length"] = brics["capital"].apply(len)

print(brics)

#          country    capital    area  population  name_length  cap_length
# BR        Brazil   Brasilia   8.516      200.40          6.0           8
# RU        Russia     Moscow  17.100      143.50          6.0           6
# IN         India  New Delhi   3.286     1252.00          5.0           9
# CH         China    Beijing   9.597     1357.00          5.0           7
# SA  South Africa   Pretoria   1.221       52.98         12.0           8
```

We've "applied" the len function to each "capital" value in our data set, adding a cap_length column to that Series. But instead of looping through all the data, we created an entire array at once, and passed that array into the data frame.
