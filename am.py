# Define the Access Matrix for the library system resources
access_matrix = {
    'Alice': {'Book1': 'rw', 'Magazine1': 'r', 'Journal1': 'x'},
    'Bob': {'Book1': 'r', 'Magazine1': 'rw', 'Journal1': None},
    'Charlie': {'Book1': 'w', 'Magazine1': 'd', 'Journal1': 'r'}
}

# Function to check if a user has a specific permission on a resource
def check_permission(user, resource, permission_type):
    # Check if the user exists in the access matrix
    if user not in access_matrix:
        return f"User '{user}' does not exist."
    
    # Check if the resource exists for the user
    if resource not in access_matrix[user]:
        return f"Resource '{resource}' does not exist for user '{user}'."
    
    # Get the permissions of the user for the given resource
    permissions = access_matrix[user][resource]
    
    # Check if the user has the required permission
    if permissions is None:
        return f"User '{user}' has no access to resource '{resource}'."
    elif permission_type in permissions:
        return f"User '{user}' has '{permission_type}' permission on resource '{resource}'."
    else:
        return f"User '{user}' does not have '{permission_type}' permission on resource '{resource}'."

# Example usage of the access matrix
print(check_permission('Alice', 'Book1', 'r'))  # Expected: User 'Alice' has 'r' permission on resource 'Book1'.
print(check_permission('Bob', 'Magazine1', 'w'))  # Expected: User 'Bob' has 'w' permission on resource 'Magazine1'.
print(check_permission('Charlie', 'Journal1', 'r'))  # Expected: User 'Charlie' has 'r' permission on resource 'Journal1'.
print(check_permission('Alice', 'Journal1', 'x'))  # Expected: User 'Alice' has 'x' permission on resource 'Journal1'.
print(check_permission('Bob', 'Journal1', 'r'))  # Expected: User 'Bob' does not have 'r' permission on resource 'Journal1'.
