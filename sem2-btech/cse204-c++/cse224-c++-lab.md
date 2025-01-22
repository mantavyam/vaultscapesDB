# CSE224 / C++ Lab

## Syllabus

{% file src="../.gitbook/assets/CSE224-Syllabus-BTECH-IT.pdf" %}

## Resources

<details>

<summary>EXPT 1 - Classes &#x26; Objects</summary>

Write a program that uses a class where the member functions are defined inside a class.

```cpp
#include <iostream>
using namespace std;

// Define the class
class Calculator {
public:
    // Member function to add two numbers
    int add(int a, int b) {
        return a + b;
    }

    // Member function to subtract two numbers
    int subtract(int a, int b) {
        return a - b;
    }

    // Member function to multiply two numbers
    int multiply(int a, int b) {
        return a * b;
    }

    // Member function to divide two numbers
    double divide(int a, int b) {
        if (b != 0) {
            return static_cast<double>(a) / b;
        } else {
            cout << "Error: Division by zero!" << endl;
            return 0;
        }
    }
};

int main() {
    Calculator calc;

    // Get input from the user
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    // Perform operations
    cout << "Addition: " << calc.add(num1, num2) << endl;
    cout << "Subtraction: " << calc.subtract(num1, num2) << endl;
    cout << "Multiplication: " << calc.multiply(num1, num2) << endl;
    cout << "Division: " << calc.divide(num1, num2) << endl;

    return 0;
}
```

</details>

<details>

<summary>EXPT 2 - Classes &#x26; Objects</summary>

Write a program that uses a class where the member functions are defined outside a class.&#x20;

```cpp
#include <iostream>
using namespace std;

// Define the class
class Calculator {
public:
    // Member functions declared inside the class
    int add(int a, int b);
    int subtract(int a, int b);
    int multiply(int a, int b);
    double divide(int a, int b);
};

// Define the member functions outside the class
int Calculator::add(int a, int b) {
    return a + b;
}

int Calculator::subtract(int a, int b) {
    return a - b;
}

int Calculator::multiply(int a, int b) {
    return a * b;
}

double Calculator::divide(int a, int b) {
    if (b != 0) {
        return static_cast<double>(a) / b;
    } else {
        cout << "Error: Division by zero!" << endl;
        return 0;
    }
}

int main() {
    Calculator calc;

    // Get input from the user
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    // Perform operations
    cout << "Addition: " << calc.add(num1, num2) << endl;
    cout << "Subtraction: " << calc.subtract(num1, num2) << endl;
    cout << "Multiplication: " << calc.multiply(num1, num2) << endl;
    cout << "Division: " << calc.divide(num1, num2) << endl;

    return 0;
}
```

</details>

<details>

<summary>EXPT 3 - Classes &#x26; Objects</summary>

Write a Program to Demonstrate Inline functions.

```cpp
#include <iostream>
using namespace std;

// Define a class to demonstrate inline functions
class MathOperations {
public:
    // Inline function to calculate the square of a number
    inline int square(int num) {
        return num * num;
    }

    // Inline function to calculate the cube of a number
    inline int cube(int num) {
        return num * num * num;
    }
};

int main() {
    MathOperations math;

    // Get input from the user
    int number;
    cout << "Enter a number: ";
    cin >> number;

    // Demonstrate the use of inline functions
    cout << "Square of " << number << " is: " << math.square(number) << endl;
    cout << "Cube of " << number << " is: " << math.cube(number) << endl;

    return 0;
}
```

</details>

<details>

<summary>EXPT 4 - Classes &#x26; Objects</summary>

Write a Program to Demonstrate Friend function, classes and this pointer.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Forward declaration of class
class BankAccount;

// Friend function to compare the balances of two accounts
void compareBalances(const BankAccount& acc1, const BankAccount& acc2);

class BankAccount {
private:
    string accountHolderName;
    double balance;

public:
    // Constructor to initialize the account
    BankAccount(string name, double initialBalance) {
        this->accountHolderName = name; // Using `this` pointer
        this->balance = initialBalance; // Using `this` pointer
    }

    // Deposit function
    void deposit(double amount) {
        if (amount > 0) {
            this->balance += amount; // Using `this` pointer
            cout << accountHolderName << " deposited $" << amount << ". New balance: $" << this->balance << endl;
        } else {
            cout << "Invalid deposit amount!" << endl;
        }
    }

    // Withdraw function
    void withdraw(double amount) {
        if (amount > 0 && amount <= this->balance) { // Using `this` pointer
            this->balance -= amount; // Using `this` pointer
            cout << accountHolderName << " withdrew $" << amount << ". New balance: $" << this->balance << endl;
        } else {
            cout << "Invalid or insufficient funds for withdrawal!" << endl;
        }
    }

    // Grant friend access to compareBalances function
    friend void compareBalances(const BankAccount& acc1, const BankAccount& acc2);
};

// Friend function to compare the balances of two accounts
void compareBalances(const BankAccount& acc1, const BankAccount& acc2) {
    cout << "Comparing balances between " << acc1.accountHolderName << " and " << acc2.accountHolderName << "..." << endl;
    if (acc1.balance > acc2.balance) {
        cout << acc1.accountHolderName << " has more money: $" << acc1.balance << endl;
    } else if (acc2.balance > acc1.balance) {
        cout << acc2.accountHolderName << " has more money: $" << acc2.balance << endl;
    } else {
        cout << "Both accounts have the same balance: $" << acc1.balance << endl;
    }
}

int main() {
    // Creating two bank accounts
    BankAccount account1("Shivam", 10000000.0);
    BankAccount account2("Ashutosh", 11000000.0);

    // Perform some transactions
    account1.deposit(500.0);
    account2.withdraw(200.0);

    // Compare balances using the friend function
    compareBalances(account1, account2);

    return 0;
}
```

</details>

<details>

<summary>EXPT 5 - Constructor &#x26; Destructor</summary>

Write a program to demonstrate the use of zero argument and parameterized constructors.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    string grade;

public:
    // Zero-argument constructor
    Student() {
        name = "Unknown";
        age = 0;
        grade = "Not Assigned";
        cout << "Zero-argument constructor called: Student created with default values." << endl;
    }

    // Parameterized constructor
    Student(string studentName, int studentAge, string studentGrade) {
        name = studentName;
        age = studentAge;
        grade = studentGrade;
        cout << "Parameterized constructor called: Student created with provided values." << endl;
    }

    // Function to display student details
    void displayDetails() {
        cout << "Student Details:" << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Grade: " << grade << endl;
        cout << "-----------------------------" << endl;
    }
};

int main() {
    // Create a student using the zero-argument constructor
    Student student1;
    student1.displayDetails();

    // Create a student using the parameterized constructor
    Student student2("Ashutosh",18, "12th");
    student2.displayDetails();

    return 0;
}
```

</details>

<details>

<summary>EXPT 6 - Operator Overloading</summary>

Write a program to demonstrate the overloading of increment and decrement operators.

```cpp
#include <iostream>
using namespace std;

class Counter {
private:
    int value;

public:
    // Constructor to initialize the counter
    Counter(int initialValue = 0) : value(initialValue) {}

    // Overload the prefix increment operator (++x)
    Counter& operator++() {
        ++value;
        return *this;
    }

    // Overload the postfix increment operator (x++)
    Counter operator++(int) {
        Counter temp = *this;
        value++;
        return temp;
    }

    // Overload the prefix decrement operator (--x)
    Counter& operator--() {
        --value;
        return *this;
    }

    // Overload the postfix decrement operator (x--)
    Counter operator--(int) {
        Counter temp = *this;
        value--;
        return temp;
    }

    // Function to display the current value of the counter
    void display() const {
        cout << "Counter Value: " << value << endl;
    }
};

int main() {
    Counter counter(10); // Initialize counter with value 10

    cout << "Initial ";
    counter.display();

    // Demonstrate prefix increment
    ++counter;
    cout << "After prefix increment (++counter): ";
    counter.display();

    // Demonstrate postfix increment
    counter++;
    cout << "After postfix increment (counter++): ";
    counter.display();

    // Demonstrate prefix decrement
    --counter;
    cout << "After prefix decrement (--counter): ";
    counter.display();

    // Demonstrate postfix decrement
    counter--;
    cout << "After postfix decrement (counter--): ";
    counter.display();

    return 0;
}
```

</details>

<details>

<summary>EXPT 7 - Inheritance</summary>

&#x20;Write a program to demonstrate the single inheritance.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class
class Person {
protected:
    string name;
    int age;

public:
    // Constructor to initialize the Person class
    Person(string personName, int personAge) {
        name = personName;
        age = personAge;
    }

    // Function to display person details
    void displayPersonDetails() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

// Derived class
class Student : public Person {
private:
    string schoolName;
    string grade;

public:
    // Constructor to initialize the Student class
    Student(string studentName, int studentAge, string studentSchool, string studentGrade)
        : Person(studentName, studentAge) { // Call base class constructor
        schoolName = studentSchool;
        grade = studentGrade;
    }

    // Function to display student details
    void displayStudentDetails() {
        // Display base class details
        displayPersonDetails();
        // Display derived class details
        cout << "School: " << schoolName << endl;
        cout << "Grade: " << grade << endl;
    }
};

int main() {
    // Create a Student object
    Student student("Ashutosh", 18, "Indian School of Life", "12th Grade");

    // Display student details
    cout << "Student Details:" << endl;
    student.displayStudentDetails();

    return 0;
}
```

</details>

<details>

<summary>EXPT 8 - Inheritance</summary>

&#x20;Write a program to demonstrate the multiple inheritance.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class 1: Person
class Person {
protected:
    string name;
    int age;

public:
    // Constructor to initialize name and age
    Person(string personName, int personAge) {
        name = personName;
        age = personAge;
    }

    // Function to display basic person details
    void displayPersonDetails() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

// Base class 2: AcademicDetails
class AcademicDetails {
protected:
    string schoolName;
    string grade;

public:
    // Constructor to initialize academic details
    AcademicDetails(string school, string studentGrade) {
        schoolName = school;
        grade = studentGrade;
    }

    // Function to display academic details
    void displayAcademicDetails() {
        cout << "School: " << schoolName << endl;
        cout << "Grade: " << grade << endl;
    }
};

// Derived class: Student
class Student : public Person, public AcademicDetails {
private:
    string hobby;

public:
    // Constructor to initialize details from both base classes and its own members
    Student(string studentName, int studentAge, string school, string studentGrade, string studentHobby)
        : Person(studentName, studentAge), AcademicDetails(school, studentGrade) {
        hobby = studentHobby;
    }

    // Function to display student details
    void displayStudentDetails() {
        // Display details from both base classes
        displayPersonDetails();
        displayAcademicDetails();
        // Display student-specific details
        cout << "Hobby: " << hobby << endl;
    }
};

int main() {
    // Create a Student object
    Student student("Ashutosh", 18, "Indian School of Life", "12th Grade", "Shooting");

    // Display all details
    cout << "Student Details:" << endl;
    student.displayStudentDetails();

    return 0;
}
```

</details>

<details>

<summary>EXPT 9 - Inheritance</summary>

Write a Program to demonstrate use of protected members, public & private protected classes, multilevel inheritance etc.&#x20;

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class: Person
class Person {
protected:
    string name;
    int age;

public:
    // Constructor to initialize the Person class
    Person(string personName, int personAge) {
        name = personName;
        age = personAge;
    }

    // Function to display basic person details
    void displayPersonDetails() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

// Derived class 1: Employee (public inheritance)
class Employee : public Person {
protected:
    string employeeID;

public:
    // Constructor to initialize Employee class and call Person's constructor
    Employee(string personName, int personAge, string id)
        : Person(personName, personAge) {
        employeeID = id;
    }

    // Function to display employee details
    void displayEmployeeDetails() {
        // Access protected members of the base class
        displayPersonDetails();
        cout << "Employee ID: " << employeeID << endl;
    }
};

// Derived class 2: Manager (multilevel inheritance from Employee)
class Manager : public Employee {
private:
    string department;

public:
    // Constructor to initialize Manager class and call Employee's constructor
    Manager(string personName, int personAge, string id, string dept)
        : Employee(personName, personAge, id) {
        department = dept;
    }

    // Function to display manager details
    void displayManagerDetails() {
        // Access Employee class members and Person class members through inheritance
        displayEmployeeDetails();
        cout << "Department: " << department << endl;
    }
};

int main() {
    // Create a Manager object (multilevel inheritance)
    Manager manager("Shivam", 100, "E12345", "Sniper");

    // Display Manager's details
    cout << "Manager Details:" << endl;
    manager.displayManagerDetails();

    return 0;
}
```

</details>

<details>

<summary>EXPT 10 - Polymorphism</summary>

Write a program to demonstrate the runtime polymorphism.&#x20;

```cpp
#include <iostream>
#include <cmath>  // For M_PI
using namespace std;

// Base class
class Shape {
public:
    // Virtual function to calculate area
    virtual double area() const {
        return 0.0;  // Default implementation (could be overridden by derived classes)
    }

    // Virtual function to display shape type
    virtual void display() const {
        cout << "This is a shape." << endl;
    }

    // Virtual destructor for proper cleanup of derived class objects
    virtual ~Shape() {
        cout << "Shape destroyed!" << endl;
    }
};

// Derived class Circle
class Circle : public Shape {
private:
    double radius;

public:
    // Constructor
    Circle(double r) : radius(r) {}

    // Override the area function
    double area() const override {
        return M_PI * radius * radius;  // Area of circle: πr^2
    }

    // Override the display function
    void display() const override {
        cout << "This is a circle with radius " << radius << "." << endl;
    }

    // Destructor
    ~Circle() {
        cout << "Circle destroyed!" << endl;
    }
};

// Derived class Rectangle
class Rectangle : public Shape {
private:
    double length, width;

public:
    // Constructor
    Rectangle(double l, double w) : length(l), width(w) {}

    // Override the area function
    double area() const override {
        return length * width;  // Area of rectangle: length * width
    }

    // Override the display function
    void display() const override {
        cout << "This is a rectangle with length " << length << " and width " << width << "." << endl;
    }

    // Destructor
    ~Rectangle() {
        cout << "Rectangle destroyed!" << endl;
    }
};

int main() {
    // Create an array of Shape pointers
    Shape* shapes[3];

    // Create instances of Circle and Rectangle and store their pointers in the array
    shapes[0] = new Circle(5.0);           // Circle with radius 5.0
    shapes[1] = new Rectangle(4.0, 6.0);   // Rectangle with length 4.0 and width 6.0
    shapes[2] = new Circle(3.0);           // Circle with radius 3.0

    // Demonstrate runtime polymorphism
    for (int i = 0; i < 3; i++) {
        shapes[i]->display();               // Call display function (runtime polymorphism)
        cout << "Area: " << shapes[i]->area() << endl;  // Call area function (runtime polymorphism)
        cout << endl;
    }

    // Cleanup dynamically allocated memory
    for (int i = 0; i < 3; i++) {
        delete shapes[i];
    }

    return 0;
}
```

</details>

<details>

<summary>EXPT 11 - Exception Handling</summary>

Write a program to demonstrate the exception handling.

```cpp
#include <iostream>
#include <stdexcept>  // For standard exception handling
using namespace std;

// Function to perform division
double divide(double numerator, double denominator) {
    if (denominator == 0) {
        // Throw an exception if denominator is zero
        throw runtime_error("Error: Division by zero is not allowed.");
    }
    return numerator / denominator;
}

// Function to demonstrate invalid input
int getNumberFromUser() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    if (cin.fail()) {
        // Throw an exception if input is not an integer
        throw invalid_argument("Error: Invalid input, expected an integer.");
    }
    return number;
}

int main() {
    double num1, num2;

    try {
        // Get two numbers from the user
        cout << "Enter the first number: ";
        num1 = getNumberFromUser();
        cout << "Enter the second number: ";
        num2 = getNumberFromUser();

        // Perform division
        double result = divide(num1, num2);
        cout << "The result of " << num1 << " / " << num2 << " is: " << result << endl;

    } catch (const runtime_error& e) {
        // Catch division by zero error
        cout << e.what() << endl;
    } catch (const invalid_argument& e) {
        // Catch invalid input error
        cout << e.what() << endl;
    } catch (...) {
        // Catch any other exceptions
        cout << "An unknown error occurred!" << endl;
    }

    return 0;
}
```

</details>

<details>

<summary>EXPT 12 - Templates &#x26; Generic Programming</summary>

Write a program to demonstrate the use of function template.&#x20;

```cpp
#include <iostream>
using namespace std;

// Function template to swap two variables of any data type
template <typename T>
void swapValues(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    // Demonstrate swap with integers
    int x = 5, y = 10;
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swapValues(x, y);  // Swap integers
    cout << "After swap: x = " << x << ", y = " << y << endl;

    // Demonstrate swap with doubles
    double m = 3.14, n = 2.71;
    cout << "Before swap: m = " << m << ", n = " << n << endl;
    swapValues(m, n);  // Swap doubles
    cout << "After swap: m = " << m << ", n = " << n << endl;

    // Demonstrate swap with characters
    char a = 'A', b = 'B';
    cout << "Before swap: a = " << a << ", b = " << b << endl;
    swapValues(a, b);  // Swap characters
    cout << "After swap: a = " << a << ", b = " << b << endl;

    return 0;
}
```

</details>

<details>

<summary>EXPT 13 - Templates &#x26; Generic Programming</summary>

Write a program to demonstrate the use of class template.

```cpp
#include <iostream>
using namespace std;

// Class template to store a value of any type
template <typename T>
class Container {
private:
    T value;

public:
    // Constructor to initialize the value
    Container(T val) : value(val) {}

    // Function to set the value
    void setValue(T val) {
        value = val;
    }

    // Function to get the value
    T getValue() const {
        return value;
    }

    // Function to display the value
    void display() const {
        cout << "Value: " << value << endl;
    }
};

int main() {
    // Create a Container for integer type
    Container<int> intContainer(100);
    cout << "Integer Container: ";
    intContainer.display();
    cout << "Getting Value: " << intContainer.getValue() << endl;

    // Create a Container for double type
    Container<double> doubleContainer(3.14);
    cout << "\nDouble Container: ";
    doubleContainer.display();
    cout << "Getting Value: " << doubleContainer.getValue() << endl;

    // Create a Container for string type
    Container<string> stringContainer("Hello, Templates!");
    cout << "\nString Container: ";
    stringContainer.display();
    cout << "Getting Value: " << stringContainer.getValue() << endl;

    return 0;
}
```

</details>

<details>

<summary>EXPT 14 - File Handling</summary>

Write a Program to Show how file management is done in C++.&#x20;

```cpp
#include <iostream>
#include <fstream>  // For file operations (fstream)
#include <string>
using namespace std;

int main() {
    string filename = "example.txt";

    // 1. Writing to a file (create a new file)
    ofstream outFile(filename);  // Opens the file in write mode
    if (!outFile) {
        cerr << "Error: Could not create the file." << endl;
        return 1;  // Return if file creation failed
    }

    outFile << "This is a demonstration of file handling in C++.\n";
    outFile << "We can write multiple lines to this file.\n";
    outFile << "You're on Vaultscapes Database webpage\n";
    outFile.close();  // Close the file after writing

    cout << "File created and written successfully.\n";

    // 2. Reading from the file
    ifstream inFile(filename);  // Opens the file in read mode
    if (!inFile) {
        cerr << "Error: Could not open the file for reading." << endl;
        return 1;  // Return if file opening for reading failed
    }

    string line;
    cout << "\nReading from the file:\n";
    while (getline(inFile, line)) {
        cout << line << endl;  // Display each line read from the file
    }
    inFile.close();  // Close the file after reading

    // 3. Appending to the file
    ofstream appendFile(filename, ios::app);  // Opens the file in append mode
    if (!appendFile) {
        cerr << "Error: Could not open the file for appending." << endl;
        return 1;  // Return if file opening for appending failed
    }

    appendFile << "This is an additional line appended to the file.\n";
    appendFile << "Appending data to a file is useful for adding information later.\n";
    appendFile.close();  // Close the file after appending

    cout << "\nData appended to the file successfully.\n";

    // 4. Reading the file after appending
    inFile.open(filename);  // Re-open the file for reading after appending
    if (!inFile) {
        cerr << "Error: Could not open the file for reading after appending." << endl;
        return 1;  // Return if file opening for reading failed
    }

    cout << "\nReading the file after appending:\n";
    while (getline(inFile, line)) {
        cout << line << endl;  // Display each line read from the file
    }
    inFile.close();  // Close the file after reading

    return 0;
}
```

</details>

## Assignment Questions

\[⤓] \[PDF] [Assignment-CSE224-Btech](https://drive.google.com/file/d/1ZMqRUzMuC0qvAWGKibVACaLMkoHgEM-1/view?usp=drive_link)

***

{% embed url="https://mantavyam.notion.site/18152f7cde8880d699a5f2e65f87374e?pvs=105" %}
Get Credited for sharing your Knowledge Source with your Peers
{% endembed %}

{% embed url="https://mantavyam.notion.site/17e52f7cde8880e0987fd06d33ef6019" %}
