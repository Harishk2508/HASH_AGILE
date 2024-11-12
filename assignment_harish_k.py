import requests
import pysolr
import pandas as pd

# Define the Solr URL and core names
solr_url = 'http://localhost:8989/solr'
core_name_1 = 'Hash_harish'
core_name_2 = 'Hash_2169'
config_set = '_default'  # Use the default config set

# Function to create a core
def create_core(core_name):
    core_path = f'{solr_url}/admin/cores?action=CREATE&name={core_name}&configSet={config_set}'
    try:
        response = requests.get(core_path)
        if response.status_code == 200:
            print(f'Core {core_name} created successfully with default configuration')
        else:
            print(f'Error creating core {core_name}: {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

# Function to reload a core
def reload_core(core_name):
    reload_path = f'{solr_url}/admin/cores?action=RELOAD&core={core_name}'
    try:
        response = requests.get(reload_path)
        if response.status_code == 200:
            print(f'Core {core_name} reloaded successfully')
        else:
            print(f'Error reloading core {core_name}: {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

# Create the cores
#create_core(core_name_1)
#create_core(core_name_2)

# Connect to Solr cores
solr_1 = pysolr.Solr(f'{solr_url}/{core_name_1}', timeout=10)
solr_2 = pysolr.Solr(f'{solr_url}/{core_name_2}', timeout=10)

# Function to index data into a specific core
def index_data(solr_core, file_path, exclude_column):
    reload_core(solr_core.url.split('/')[-1])  # Reload the core before indexing
    # Load the cleaned data
    df = pd.read_csv(file_path)
    
    # Remove the specified column
    if exclude_column in df.columns:
        df.drop(columns=[exclude_column], inplace=True)
    
    # Rename 'Employee ID' to 'Employee_ID' to match the schema field
    df.rename(columns={'Employee ID': 'Employee_ID'}, inplace=True)

    df['id'] = df['Employee_ID']
    
    # Convert the DataFrame to a list of dictionaries for Solr
    data = df.to_dict(orient='records')
    
    # Index the data into Solr
    solr_core.add(data)
    solr_core.commit()  # Ensure changes are committed
    print(f"Data indexed to collection with excluded column '{exclude_column}'.")

# Function to get employee count
def get_emp_count(solr_core):
    query = "*:*"  # Search all records
    results = solr_core.search(query, rows=0)
    print(f"Total number of employees: {results.hits}")

# Function to delete employee by ID
def del_emp_by_id(solr_core, employee_id):
    query = f"Employee_ID:{employee_id}"
    results = solr_core.search(query)  # Check if the employee exists
    if results.hits > 0:
        # Get the contents of the deleted item
        deleted_item = results.docs[0]
        print(f"Deleting Employee: {deleted_item}")
        
        solr_core.delete(q=query)
        solr_core.commit()  # Ensure changes are committed
        print(f"Employee with ID {employee_id} deleted.")
        
        # Verify deletion
        new_results = solr_core.search(query)
        if new_results.hits == 0:
            print(f"Employee with ID {employee_id} deleted successfully.")
        else:
            print(f"Error: Employee with ID {employee_id} still exists.")
    else:
        print(f"No employee found with ID {employee_id}.")

# Function to search by column
def search_by_column(solr_core, column_name, column_value):
    query = f"{column_name}:{column_value}"
    results = solr_core.search(query, rows=10)
    print(f"Search results for {column_name} = {column_value}:")
    for result in results:
        print(result)

# Function to get department facet
def get_dep_facet(solr_core):
    params = {
        'facet': 'true',
        'facet.field': 'Department',
        'rows': 0
    }
    
    results = solr_core.search('*:*', **params)
    
    print("Department Facet Counts:")
    
    facet_data = results.facets['facet_fields']['Department']
    
    for i in range(0, len(facet_data), 2):
        department = facet_data[i]        # Department name (odd index)
        count = facet_data[i + 1]         # Department count (even index)
        print(f"{department}: {count}")

# File path to the cleaned data
file_path = "D:/cleaned_dataset3.csv"

#create_core(core_name_1)
#create_core(core_name_2)

# Step 1: Get employee count for 'Hash_harish' collection
#get_emp_count(solr_1)

# Step 2: Index data excluding 'Department' column in 'Hash_harish' collection
#index_data(solr_1, file_path, 'Department')

# Step 3: Index data excluding 'Gender' column in 'Hash_2169' collection
#index_data(solr_2, file_path, 'Gender')

# Step 4: Get employee count for 'Hash_2169' collection
#get_emp_count(solr_1)
#get_emp_count(solr_2)

# Step 5: Delete employee with ID 'E02003' in 'Hash_2169' collection
#del_emp_by_id(solr_2, 'E02003')

# Step 6: Get employee count after deletion in 'Hash_2169' collection
#get_emp_count(solr_2)

# Step 7: Get employee count after deletion in 'Hash_harish' collection
#get_emp_count(solr_1)

# Step 8: Search by 'Department' for 'IT' in 'Hash_harish' collection
#search_by_column(solr_1, 'Department', 'IT')

# Step 9: Search by 'Gender' for 'Male' in 'Hash_harish' collection
search_by_column(solr_1, 'Gender', 'Male')

# Step 10: Search by 'Department' for 'IT' in 'Hash_2169' collection
search_by_column(solr_2, 'Department', 'IT')

# Step 11: Get department facet for 'Hash_harish' collection
get_dep_facet(solr_1)

# Step 12: Get department facet for 'Hash_2169' collection
get_dep_facet(solr_2)
