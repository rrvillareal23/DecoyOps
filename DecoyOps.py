import os
import random
import time
import sys

# Function to generate random file modification
def modify_file(file_path):
    with open(file_path, 'a') as file:
        file.write('\nModified by decoy script.')

# Function to log alterations
def log_alteration(action, file_path):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open('alterations.log', 'a') as log_file:
        log_file.write(f'{timestamp} - {action}: {file_path}\n')

# Function to create a decoy directory structure
def create_decoy_structure(directory):
    departments = ['Finance', 'HR', 'Marketing', 'Operations']
    for department in departments:
        department_dir = os.path.join(directory, department)
        os.makedirs(department_dir, exist_ok=True)
        # Create dummy files for each department
        for i in range(random.randint(2, 5)):
            with open(os.path.join(department_dir, f'file_{i}.txt'), 'w') as f:
                f.write(f'Dummy file for {department}')

# Trap approach: Monitoring file access
def monitor_file_access(file_path):
    print(f"Trap: Someone accessed {file_path}")

# Trap approach: Monitoring file modification
def monitor_file_modification(file_path):
    print(f"Trap: Someone modified {file_path}")

# Trap approach: Monitoring file deletion
def monitor_file_deletion(file_path):
    print(f"Trap: Someone deleted {file_path}")

# Trap approach: Monitoring file addition
def monitor_file_addition(file_path):
    print(f"Trap: Someone added a file {file_path}")

# Main function to simulate live activity
def simulate_activity(directory):
    try:
        while True:
            # Check if directory is empty
            subdirs_with_files = [
                os.path.join(directory, subdir) 
                for subdir in os.listdir(directory) 
                if os.path.isdir(os.path.join(directory, subdir)) and len(os.listdir(os.path.join(directory, subdir))) > 0
            ]
            if not subdirs_with_files:
                print(f"No directories with files found in '{directory}'. Exiting simulation.")
                return

            # Select a random action: modify, add, or delete a file
            action = random.choice(['modify', 'add', 'delete'])

            if action == 'modify':
                # Select a random directory with files
                directory_to_modify = random.choice(subdirs_with_files)
                # Select a random file within the directory for modification
                files = [
                    os.path.join(directory_to_modify, filename) 
                    for filename in os.listdir(directory_to_modify) 
                    if os.path.isfile(os.path.join(directory_to_modify, filename))
                ]
                if not files:
                    print(f"No files found in directory '{directory_to_modify}'. Exiting simulation.")
                    return
                file_path = random.choice(files)

                # Simulate modification to the filez
                modify_file(file_path)
                # Log the alteration
                log_alteration('Modified', file_path)
                # Simulate trap mechanisms
                monitor_file_access(file_path)  # Trap: File access
                monitor_file_modification(file_path)  # Trap: File modification
            
            elif action == 'add':
                # Select a random department directory
                directory_to_add_file = random.choice(subdirs_with_files)
                # Create a new file in the selected directory
                new_file_path = os.path.join(directory_to_add_file, f'new_file_{time.time()}.txt')
                with open(new_file_path, 'w') as f:
                    f.write(f'New file created in {os.path.basename(directory_to_add_file)} department.')
                # Log the addition
                log_alteration('Added', new_file_path)
                # Simulate trap mechanism
                monitor_file_addition(new_file_path)  # Trap: File addition

            elif action == 'delete':
                # Select a random directory with files
                directory_to_delete_file = random.choice(subdirs_with_files)
                # Select a random file within the directory for deletion
                files = [
                    os.path.join(directory_to_delete_file, filename) 
                    for filename in os.listdir(directory_to_delete_file) 
                    if os.path.isfile(os.path.join(directory_to_delete_file, filename))
                ]
                if not files:
                    print(f"No files found in directory '{directory_to_delete_file}'. Exiting simulation.")
                    return
                file_path = random.choice(files)
                # Delete the selected file
                os.remove(file_path)
                # Log the deletion
                log_alteration('Deleted', file_path)
                # Simulate trap mechanism
                monitor_file_deletion(file_path)  # Trap: File deletion
            
            time.sleep(random.randint(5, 10))  # Wait for random time interval

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting simulation.")
        sys.exit()

if __name__ == "__main__":
    decoy_directory = 'decoy_directory'
    
    # Create the decoy directory structure
    create_decoy_structure(decoy_directory)
    
    # Start simulation
    simulate_activity(decoy_directory)
