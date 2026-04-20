# Write a program that converts a Roman numeral to an integer
def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_numerals[char]
        
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        
        prev_value = value
    
    return total


# Write a program that calculates the factorial of a number
def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    


# Write a program that generates a blog
def generate_blog(title, content):
    blog_template = f"""
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{content}</p>
    </body>
    </html>
    """
    return blog_template    