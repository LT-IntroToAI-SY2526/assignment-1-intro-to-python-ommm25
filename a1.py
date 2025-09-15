# Assignment 1: AI-Generated Python Problems
# Name: Omar Arellano 

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class. I have some experience with [mention your previous programming language if any, or say 'I'm new to programming']. Can you create 5-7 practice problems that cover:
Variables and basic data types, Conditionals (if/elif/else), Loops (for and while), Functions, Basic list operations, and Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
Write a function multiply_evens(numbers) that multiplies all even numbers in a list. If there are no even numbers, return 1.

print(multiply_evens([2, 3, 4]))      8
print(multiply_evens([1, 3, 5]))      1 (Due to no evens)
print(multiply_evens([]))            1( due to no evens)
print(multiply_evens([10, 20]))      200
print(multiply_evens([7]))            1(due to no evens)










# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
def multiply_evens(numbers):
    # Start with 1 because we're multiplying
    result = 1
    found_even = False
    
    for num in numbers:
        if num % 2 == 0:
            result *= num
            found_even = True
    
    # If no even numbers found, return 1 (default)
    return result if found_even else 1

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


