import os

def create_wp_config():
    # Prompt user for input
    db_name = input("Enter the database name: ")
    db_user = input("Enter the MySQL username: ")
    db_password = input("Enter the MySQL password: ")
    db_host = input("Enter the database host (default is 'localhost'): ") or 'localhost'
    
    # Template for wp-config.php
    wp_config_content = f"""<?php
define('DB_NAME', '{db_name}');
define('DB_USER', '{db_user}');
define('DB_PASSWORD', '{db_password}');
define('DB_HOST', '{db_host}');

// Other optional settings can go here
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');

// Security keys (you can generate them from the WordPress secret-key service)
define('AUTH_KEY',         'put your unique phrase here');
define('SECURE_AUTH_KEY',  'put your unique phrase here');
define('LOGGED_IN_KEY',    'put your unique phrase here');
define('NONCE_KEY',        'put your unique phrase here');
define('AUTH_SALT',       'put your unique phrase here');
define('SECURE_AUTH_SALT', 'put your unique phrase here');
define('LOGGED_IN_SALT',   'put your unique phrase here');
define('NONCE_SALT',       'put your unique phrase here');

// WordPress Database Table prefix
$table_prefix = 'wp_';

// Debugging mode
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */
if ( !defined('ABSPATH') )
    define('ABSPATH', __DIR__ . '/');
require_once(ABSPATH . 'wp-settings.php');
"""

    # Specify the path to save wp-config.php
    config_file_path = os.path.join(os.getcwd(), 'wp-config.php')

    # Create and write to the wp-config.php file
    with open(config_file_path, 'w') as config_file:
        config_file.write(wp_config_content)
    
    print(f"wp-config.php file created successfully at {config_file_path}")

if __name__ == "__main__":
    create_wp_config()
