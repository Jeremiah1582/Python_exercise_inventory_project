# Backstory:

You've been hired as a software developer for "ShopEasy Retailers". They have a list of products in their inventory, and they want a simple program to track the position of each product on their shelves.
You will build this program for them, allowing the user to use the command-line-interface to interact with the program. 

# Objective: Write a Python program that can:
- Display products along with their shelf positions.
- Check if a product is in the list and display its position.
- Display products available within a specified range of shelf positions.

# Tasks:
1) Display Products with Positions: 
- Use the enumerate() function to display each product along with its position (starting from 1).

2) Product Position Checker:
- Take user input for a product name.
- Use the enumerate() function to check if the product is in the list and display its position. If not found, display "Product not found."

3) Display Products within a Range:
- Take user input for start and end positions.
- Use the range() function combined with enumerate() to display products within the specified range of positions.

# Requirements:
- Use the enumerate() function for tasks related to positions.
- Ensure you account for the fact that list indexes start at 0 while shelf positions start at 1.
- Make sure your solution is user-friendly and provides clear instructions and outputs.

**Example Inventory List: copy this code**

products = ["Laptop", "Mobile Phone", "Television", "Refrigerator", "Microwave", "Washing Machine", "Blender"]

**Expected Outputs for Each Task:**

Laptop - 1
Mobile Phone - 2
Television - 3
... and so on

*Input:* Mobile Phone
*Output:* Mobile Phone is at position 2.

*Input:* Tablet
*Output:* Product not found.

*Input (range):*
    Enter the starting position: 2
    Enter the ending position: 3

*Output:*
Mobile Phone - 2
Television - 3
Refrigerator - 4
Microwave - 5

This exercise will help you understand the usefulness of enumerate() in real-world scenarios where positions or indexes of elements in an iterable are essential. They'll also get to combine this with the range() function to filter and display products within a particular range of positions.