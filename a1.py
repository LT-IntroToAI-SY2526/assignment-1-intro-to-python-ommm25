# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

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
[I am learnin python basics in high school programming class. I have a decent amount of experience with java. Can you create 5 practice problems
that test my soutions with different inputs, and include comments explaining your approach to the answer.]

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
Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print(longest_word(["apple", "banana", "kiwi"]))  
# Should print "banana"

print(longest_word(["one", "two", "three"]))    
Should print "three" 

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


