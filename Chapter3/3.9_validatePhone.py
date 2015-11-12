import re

def validate(n):
    if re.search(r'^(0|\+91)?[789]\d{9}$', n):
            return "Your mobile number is valid in India."
    return "Sorry, your number is invalid in India."

print validate('9712345789')
print validate('+918934567890')
