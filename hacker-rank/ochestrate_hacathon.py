# Catogery: Account, Billing, Security 
# Account: Keywords: = Password, login, forgot
# response: "Please reset your password using 'forgot password' option"

# Billing: Keywords = payment, refunded, failed
# response: "Please check your payment details or contact billing support"

# Security: keywords = Hacked, fraud, unauthorized
# response: " This is a security issue. Escalation to support team"

# Catogery: Account, Billing, Security 
# Account: Keywords: = Password, login, forgot
# response: "Please reset your password using 'forgot password' option"

# Billing: Keywords = payment, refunded, failed
# response: "Please check your payment details or contact billing support"

# Security: keywords = Hacked, fraud, unauthorized
# response: " This is a security issue. Escalation to support team"

# Catogery: Account, Billing, Security 
# Account: Keywords: = Password, login, forgot
# response: "Please reset your password using 'forgot password' option"

# Billing: Keywords = payment, refunded, failed
# response: "Please check your payment details or contact billing support"

# Security: keywords = Hacked, fraud, unauthorized
# response: " This is a security issue. Escalation to support team"

# Catogery: Account, Billing, Security 
# Account: Keywords: = Password, login, forgot
# response: "Please reset your password using 'forgot password' option"

# Billing: Keywords = payment, refunded, failed
# response: "Please check your payment details or contact billing support"

# Security: keywords = Hacked, fraud, unauthorized
# response: " This is a security issue. Escalation to support team"

# Catogery: Account, Billing, Security 
# Account: Keywords: = Password, login, forgot
# response: "Please reset your password using 'forgot password' option"

# Billing: Keywords = payment, refunded, failed
# response: "Please check your payment details or contact billing support"

# Security: keywords = Hacked, fraud, unauthorized
# response: " This is a security issue. Escalation to support team"

# Catogery: Account, Billing, Security 
# Account: Keywords: = Password, login, forgot
# response: "Please reset your password using 'forgot password' option"

# Billing: Keywords = payment, refunded, failed
# response: "Please check your payment details or contact billing support"

# Security: keywords = Hacked, fraud, unauthorized
# response: " This is a security issue. Escalation to support team"

import csv

queries = [
    "i forgot my password",
    "payment failed",
    "account hacked",
    "hello i need help"
]

with open("output.csv", "w", newline="") as file, open("log.txt", "w") as log_file:
    writer = csv.writer(file)
    writer.writerow(["query", "category", "response"])

    for q in queries:
        q_lower = q.lower()

        if any(word in q_lower for word in ['hacked', 'fraud', 'unauthorized']):
            category = "Security"
            response = "This is a security issue. Escalation to support team"

        elif any(word in q_lower for word in ['payment', 'refunded', 'failed']):
            category = "Billing"
            response = "Please check your payment details or contact billing support"

        elif any(word in q_lower for word in ['password', 'login', 'forgot']):
            category = "Account"
            response = "Please reset your password using 'forgot password' option"

        else:
            category = "General"
            response = "Please contact support"

        writer.writerow([q, category, response])

        log_file.write(f"Query: {q}\n")
        log_file.write(f"Category: {category}\n")
        log_file.write(f"Response: {response}\n\n")