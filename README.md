# Sample Python Project

This project demonstrates a simple school management system implemented in Python, with MySQL as the database backend. It allows you to manage students, courses, and enrollments.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MySQL

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/Su-HackZ/sample-python-project.git
    cd sample-python-project
    ```

2. **Install Dependencies:**

    Install the required Python package using pip:

    ```sh
    pip install mysql-connector-python
    ```

3. **Set Up the Database:**

    Ensure you have MySQL running on your local machine and update the `db_config` dictionary in your scripts with your MySQL username and password.

    ```python
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Pass@123',  # replace with your MySQL password
        'database': 'school_management'
    }
    ```

### Usage

1. **Set Up the Database Schema:**

    Run the `setup_database.py` script to create the necessary database and tables.

    ```sh
    python setup_database.py
    ```

2. **Run the Main Script:**

    Execute the `main.py` script to interact with the school management system.

    ```sh
    python main.py
    ```

### Project Structure

- `course.py`: Contains the `Course` class.
- `database.py`: Contains the `Database` class for handling database operations.
- `school.py`: Contains the `School` class for managing students and courses.
- `setup_database.py`: Script to set up the initial database and tables.
- `student.py`: Contains the `Student` class.
- `main.py`: Main script to run the application.
- `README.md`: Project documentation.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License.

### Enjoy using the school management system!
