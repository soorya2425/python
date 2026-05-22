# Step 1: Create Boolean variables
has_account = True
email_verified = False

# Step 2: Check if user can log in
can_login = has_account and email_verified

# Step 3: Validate email
email = "g@example.com"
is_email_valid = "@" in email

# Step 4: Check age validity
user_age = 17
is_age_valid = user_age >= 18

# Step 5: Final login condition
can_login_final = (
    has_account and
    email_verified and
    is_email_valid and
    is_age_valid
)

# Step 6: Print results
print("Can Login:", can_login)
print("Is Email Valid:", is_email_valid)
print("Is Age Valid:", is_age_valid)
print("Final Login Status:", can_login_final)

# Step 7: Identity operator check
print("Has Account is True:", has_account is True)