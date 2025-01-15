# CSE104 / Comp Science

Syllabus

{% file src="../.gitbook/assets/CSE104-Syllabus-BTECH-IT.pdf" %}

## Resources

<details>

<summary>M1: Introduction to Programming</summary>



</details>

<details>

<summary>M2: Programming Essential</summary>



</details>

<details>

<summary>M3: Arrays</summary>



</details>

<details>

<summary>M4: Basic Algorithms</summary>



</details>

<details>

<summary>M5: Functions</summary>



</details>

<details>

<summary>M6: Recursion</summary>



</details>

<details>

<summary>M7: Structure</summary>



</details>

<details>

<summary>M8: Pointers</summary>



</details>

<details>

<summary>M9: File Handling</summary>



</details>

***

## Questions Directory

\[⤓] (PDF) [C Programs with Solutions](https://file.notion.so/f/f/a55e0ddd-0663-44e4-aa54-2e6bc5b00199/bb3ed200-28f1-4794-a680-3de476abf2c0/C_Programming_Questions.pdf?table=block\&id=2b988492-c5be-4c9f-b3cc-12a51c7250ca\&spaceId=a55e0ddd-0663-44e4-aa54-2e6bc5b00199\&expirationTimestamp=1736964000000\&signature=5OgCt4c-IovaRbIR5Qalmy9pu8L2GHl6AqoD7lJvsus\&downloadName=C+Programming+Questions.pdf)

### Assignment Questions

\[⤓] (PDF) [CSE124-THEORY-Assignment-Sem1-Btech.pdf](https://file.notion.so/f/f/a55e0ddd-0663-44e4-aa54-2e6bc5b00199/cbe8e13d-d309-4725-a9c4-a47d7db4c7f7/CSE-THEORY-Assignment-Sem1-Btech.pdf?table=block\&id=17c52f7c-de88-804d-a008-fe273dc040cf\&spaceId=a55e0ddd-0663-44e4-aa54-2e6bc5b00199\&expirationTimestamp=1736971200000\&signature=VkG2f_bTdpYZhhL9ujhYUoCE2K_snWQ9mXMzrf6QFew\&downloadName=CSE-THEORY-Assignment-Sem1-Btech.pdf)

{% embed url="https://www.notion.so/mantavyam/Assignment-Theory-CSE-e66686dce1df4eedb9258dbf4a10c1bc" %}
Solutions to Assignment
{% endembed %}

{% hint style="info" %}
(Ask Your Present Faculty for Qs relevant to end sem)
{% endhint %}

### Previous Year Questions

{% embed url="https://file.notion.so/f/f/a55e0ddd-0663-44e4-aa54-2e6bc5b00199/390f2f79-251e-4d31-afe4-3776638146fc/20240130_125849.jpg?downloadName=20240130_125849.jpg&expirationTimestamp=1736964000000&id=fa186760-61ff-45e5-a0fd-e67e276bb5c0&signature=CKZ-c8UK8-TCZcv7FZWGEAvIVwqvMERMT-fEAtXI_Z0&spaceId=a55e0ddd-0663-44e4-aa54-2e6bc5b00199&table=block" %}
ENDSEM-CSE104-JAN2024
{% endembed %}

### Important Codes

<details>

<summary>Factorial using Recursion</summary>

```c
#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int num;
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    printf("Factorial of %d = %d\n", num, factorial(num));

    return 0;
}
```



</details>

<details>

<summary>Generate Fibonacci Series</summary>

```c
#include <stdio.h>

void generateFibonacci(int n) {
    int first = 0, second = 1, next;

    printf("Fibonacci Series up to %d terms: ", n);

    for (int i = 0; i < n; i++) {
        printf("%d, ", first);
        next = first + second;
        first = second;
        second = next;
    }
}

int main() {
    int terms;
    printf("Enter the number of terms for Fibonacci Series: ");
    scanf("%d", &terms);

    generateFibonacci(terms);

    return 0;
}
```

</details>

<details>

<summary>Check Number and tell Positive / Negative / Zero</summary>

<pre class="language-c"><code class="lang-c"><strong>#include &#x3C;stdio.h>
</strong><strong>
</strong>int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &#x26;num);

    if (num > 0) {
        printf("The number %d is positive.\n", num);
    } else if (num &#x3C; 0) {
        printf("The number %d is negative.\n", num);
    } else {
        printf("The number is zero.\n");
    }

    return 0;
}
</code></pre>

</details>

<details>

<summary>Roots of Quad. Eqs</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c;
    double discriminant, root1, root2;

    // Input coefficients a, b, and c
    printf("Enter coefficients (a, b, c) of the quadratic equation (ax^2 + bx + c = 0):\n");
    scanf("%lf %lf %lf", &a, &b, &c);

    // Calculate discriminant
    discriminant = b * b - 4 * a * c;

    // Check the nature of roots
    if (discriminant > 0) {
        // Two distinct real roots
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("Roots are real and distinct: %.2lf and %.2lf\n", root1, root2);
    } else if (discriminant == 0) {
        // One real root (repeated)
        root1 = -b / (2 * a);
        printf("Roots are real and equal: %.2lf\n", root1);
    } else {
        // Complex roots
        double realPart = -b / (2 * a);
        double imaginaryPart = sqrt(-discriminant) / (2 * a);
        printf("Roots are complex and imaginary: %.2lf + %.2lfi and %.2lf - %.2lfi\n",
               realPart, imaginaryPart, realPart, imaginaryPart);
    }

    return 0;
}
```

</details>

<details>

<summary>Check Character and tell Vowel or Consonant?</summary>

<pre class="language-c"><code class="lang-c"><strong>#include &#x3C;stdio.h>
</strong>
int main() {
    char ch;

    printf("Enter a character: ");
    scanf(" %c", &#x26;ch);

    // Checking if the entered character is an alphabet
    if ((ch >= 'a' &#x26;&#x26; ch &#x3C;= 'z') || (ch >= 'A' &#x26;&#x26; ch &#x3C;= 'Z')) {
        // Checking if the character is a vowel
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            printf("The character %c is a vowel.\n", ch);
        } else {
            printf("The character %c is a consonant.\n", ch);
        }
    } else {
        printf("Invalid input. Please enter an alphabet character.\n");
    }

    return 0;
}
</code></pre>

</details>

<details>

<summary>Calculate and display the length of the entered string</summary>

```c
#include <stdio.h>

// Function to calculate the length of a string
int stringLength(const char *str) {
    int length = 0;

    // Loop until the null character '\0' is encountered
    while (str[length] != '\0') {
        length++;
    }

    return length;
}

int main() {
    char inputString[100];

    printf("Enter a string: ");
    scanf("%s", inputString);

    // Calculate and display the length of the entered string
    printf("Length of the string: %d\n", stringLength(inputString));

    return 0;
}
```

</details>

<details>

<summary>Print Number in Reverse Order</summary>

```c
#include <stdio.h>

void printReverseFor(int n) {
    printf("Printing in reverse using for loop: ");
    for (int i = n; i >= 1; i--) {
        printf("%d ", i);
    }
    printf("\n");
}

void printReverseWhile(int n) {
    printf("Printing in reverse using while loop: ");
    int i = n;
    while (i >= 1) {
        printf("%d ", i);
        i--;
    }
    printf("\n");
}

int main() {
    int num;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    printReverseFor(num);
    printReverseWhile(num);

    return 0;
}
```

</details>

<details>

<summary>Swap 2 Variables by Pointer Addition</summary>

```c
#include <stdio.h>

void swap(int *a, int *b) {
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

int main() {
    int num1, num2;

    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    printf("Before swapping: num1 = %d, num2 = %d\n", num1, num2);

    swap(&num1, &num2);

    printf("After swapping: num1 = %d, num2 = %d\n", num1, num2);

    return 0;
}
```

</details>

<details>

<summary>Sort an Array Using Quick Sort</summary>

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    quickSort(arr, 0, n - 1);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}
```

</details>

<details>

<summary>Check if a number is an Armstrong number</summary>

```c
#include <stdio.h>
#include <math.h>

// Function to check if a number is an Armstrong number
int isArmstrong(int num) {
    int originalNum, remainder, result = 0, n = 0;

    originalNum = num;

    // Counting the number of digits
    while (originalNum != 0) {
        originalNum /= 10;
        ++n;
    }

    originalNum = num;

    // Calculating the sum of nth powers of digits
    while (originalNum != 0) {
        remainder = originalNum % 10;
        result += pow(remainder, n);
        originalNum /= 10;
    }

    // Checking if the number is Armstrong
    if (result == num)
        return 1; // True, the number is Armstrong
    else
        return 0; // False, the number is not Armstrong
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    // Checking if the entered number is Armstrong
    if (isArmstrong(num))
        printf("%d is an Armstrong number.\n", num);
    else
        printf("%d is not an Armstrong number.\n", num);

    return 0;
}
```

</details>

<details>

<summary>Count Values using Conditional (Ternary) Operator</summary>

```c
#include <stdio.h>

int main() {
    int num, positiveCount = 0, negativeCount = 0, zeroCount = 0;

    printf("Enter integers (enter 0 to stop):\n");

    while (1) {
        scanf("%d", &num);

        // Check if the entered number is zero, and exit the loop
        if (num == 0)
            break;

        // Use conditional operator to count positive, negative, or zero values
        (num > 0) ? positiveCount++ : (num < 0) ? negativeCount++ : zeroCount++;
    }

    printf("Count of positive numbers: %d\n", positiveCount);
    printf("Count of negative numbers: %d\n", negativeCount);
    printf("Count of zero values: %d\n", zeroCount);

    return 0;
}
```

</details>

<details>

<summary>Illustrate Difference b/w Iteration &#x26; Selection</summary>

```c
#include <stdio.h>

int main() {
    // Iteration using a for loop
    printf("Iteration using a for loop:\n");
    for (int i = 1; i <= 5; i++) {
        printf("Iteration %d\n", i);
    }

    // Iteration using a while loop
    printf("\nIteration using a while loop:\n");
    int j = 1;
    while (j <= 5) {
        printf("Iteration %d\n", j);
        j++;
    }

    // Selection using if-else statement
    int number;

    printf("\nEnter a number: ");
    scanf("%d", &number);

    if (number > 0) {
        printf("The number %d is positive.\n", number);
    } else if (number < 0) {
        printf("The number %d is negative.\n", number);
    } else {
        printf("The number is zero.\n");
    }

    return 0;
}
```

</details>

<details>

<summary>Matrix Calculation</summary>

```c
#include <stdio.h>

// Function to add two matrices
void addMatrices(int firstMatrix[10][10], int secondMatrix[10][10], int result[10][10], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = firstMatrix[i][j] + secondMatrix[i][j];
        }
    }
}

// Function to display a matrix
void displayMatrix(int matrix[10][10], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int rows, cols;

    printf("Enter the number of rows and columns for the matrices: ");
    scanf("%d %d", &rows, &cols);

    int firstMatrix[10][10], secondMatrix[10][10], resultMatrix[10][10];

    printf("Enter elements of the first matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &firstMatrix[i][j]);
        }
    }

    printf("Enter elements of the second matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &secondMatrix[i][j]);
        }
    }

    // Adding two matrices
    addMatrices(firstMatrix, secondMatrix, resultMatrix, rows, cols);

    // Displaying the result matrix
    printf("Resultant Matrix:\n");
    displayMatrix(resultMatrix, rows, cols);

    return 0;
}
```

</details>

***

## External Sources

Links to Cover Syllabus Content

