import os
import subprocess
import sys

description = "Update WordPress Plugins - This script will update and create a Git Commit for each plugin that has updates available."

def check_wp_cli():
    """Check if WP-CLI is installed and accessible."""
    try:
        subprocess.run(['wp', '--info'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("WP-CLI is installed.")
        return True
    except subprocess.CalledProcessError:
        print("WP-CLI is not installed or not configured properly.")
        return False

def install_wp_cli():
    """Install WP-CLI if it's not installed."""
    print("Installing WP-CLI...")
    try:
        # Download wp-cli.phar
        subprocess.run(['curl', '-O', 'https://raw.githubusercontent.com/wp-cli/builds/gh-pages/gh-cli-info', '-o', 'wp-cli.phar'], check=True)
        
        # Move to /usr/local/bin and make executable
        subprocess.run(['sudo', 'mv', 'wp-cli.phar', '/usr/local/bin/wp'], check=True)
        subprocess.run(['sudo', 'chmod', '+x', '/usr/local/bin/wp'], check=True)
        
        print("WP-CLI installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing WP-CLI: {e}")

def update_plugins():
    """Update all plugins in the specified WordPress directory."""
    # Get the current working directory
    current_dir = os.getcwd()

    # Construct the path to the plugins directory
    wp_plugins_dir = os.path.join(current_dir, 'app', 'public', 'wp-content', 'plugins')
    
    # Check if the plugins directory exists
    if not os.path.isdir(wp_plugins_dir):
        print(f"No plugins directory found in {wp_plugins_dir}. Please check the directory structure.")
        return
    
    # Navigate to the plugins directory
    os.chdir(wp_plugins_dir)
    
    # Update all plugins using WP-CLI
    try:
        print("Updating plugins...")
        subprocess.run(['wp', 'plugin', 'update', '--all'], check=True)
        print("Plugins updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while updating plugins: {e}")

if __name__ == "__main__":
    if not check_wp_cli():
        install_wp_cli()
        if not check_wp_cli():
            print("WP-CLI installation failed. Exiting.")
            sys.exit(1)

    update_plugins()