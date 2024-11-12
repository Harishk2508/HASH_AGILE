## Task 1: Bash Script

The bash script provided performs the following task:

1. Defines a user-defined function called `secondlargest()` that takes a list of elements as arguments.
2. The function checks if the input list has at least two elements. If not, it prints a message and returns.
3. The function initializes the largest element (`max1`) as the first element of the list.
4. It then iterates through the list to find the largest element.
5. Next, it initializes the second-largest element (`seclgt`) to a very low value (-999999) to simulate negative infinity.
6. It iterates through the list again to find the second-largest element, ensuring that it is not the same as the largest element.
7. If the second-largest element is not found (all elements are equal), it prints a message indicating that there is no second-largest element.
8. Otherwise, it prints the second-largest element in the list.
9. The script then calls the `secondlargest()` function with a sample test case `(25 7 6 21 18 28 2 31)`.

## Task 2: Python Script

The Python script provided performs the following tasks:

1. Defines functions to create and reload Solr cores.
2. Indexes data into two Solr cores, excluding specific columns.
3. Retrieves the total number of employees in the Solr cores.
4. Deletes an employee from one of the Solr cores.
5. Searches for employees by specific columns.
6. Retrieves the department facet for the Solr cores.

The script uses the `pysolr` library to interact with the Solr search engine and performs various operations on the data.

The main components of the Python script are:

1. `create_core()` and `reload_core()` functions to manage Solr cores.
2. `index_data()` function to index data into Solr cores.
3. `get_emp_count()` function to retrieve the total number of employees.
4. `del_emp_by_id()` function to delete an employee by ID.
5. `search_by_column()` function to search for employees by specific columns.
6. `get_dep_facet()` function to retrieve the department facet.

The script also includes sample data and calls to these functions to demonstrate the functionality.

Please note that the Python script is provided separately, and this README file only covers the information related to Task 1 and Task 2.
