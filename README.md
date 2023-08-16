# Library_Management_System
This is a comprehensive and efficient solution designed to streamline the management of libraries, making the process of book cataloging, member management, and borrowing transactions more organized and user-friendly. Built using Python and integrated with MySQL Server, this application empowers librarians to manage their resources effectively and provide a seamless experience to library patrons.

## Table of Contents

- Features
- Prerequisites
- Installation
- Usage
- Contributions
- License
- Contact

## Features

- Book Entry: Register a new book into the library catalog.

- Register Member: Register a new member into the library system.

- Issue Book: Issue a book to a member.

- View Member Issued Books: Retrieve details about an issued book using its issue number.

- View All Books: Display a list of all the books present in the library catalog.

- View All Members: Display a list of all the members registered with the library. 

- View All Issued Books: Display a list of all books that have been issued to members.

- Update Details: Perform updates on various aspects of the library management system:
1. Extend Due Date: Extend the due date for returning a book, accommodating member requests.
2. Cancel Membership: Remove a member from the system, often due to membership expiration or other reasons.

- Return Book: Mark a book as returned by using its issue number. 

The data is also stored in MySQL database which can be used for further querying.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- MySQL Server

You also need to have the necessary Python libraries installed. You can install them using the following command in cmd :
`pip install mysql-connector-python`

## Installation

1. Clone or download this repository to your local machine using: `git clone https://github.com/sayandip20/library-management-system.git` or
2. Navigate to the project directory: `cd Library_Management_System` and use it.

## Usage

1. Create a MySQL database schema same as in `database_schema.sql` included in the repository.
2. Run the `main.py` Python script to start the application.
3. Follow the on-screen instructions to interact with the Library Management System.

## Contributions

Contributions are encouraged! If you have suggestions, improvements, or bug fixes, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Implement your changes and commit them: `git commit -am 'Add your feature'`
4. Push the branch to your forked repository: `git push origin feature/your-feature-name`
5. Open a pull request, providing a detailed explanation of your changes and their impact.

## Licence

This project is licensed under the Apache-2.0 License.

## Contact

For any query you can contact me here: sayandipadhikari20@gamil.com
