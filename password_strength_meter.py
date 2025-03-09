import streamlit as st

def check_password_strength(password):
    """
    Evaluate the strength of a password based on predefined rules.
    """
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def main():
    st.title("Password Strength Meter")
    st.write("Enter a password to check its strength.")

    # Input field for password
    password = st.text_input("Password", type="password")

    if password:
        # Check password strength
        strength, feedback = check_password_strength(password)

        # Display strength
        st.write(f"**Strength:** {strength}")

        # Display feedback
        if feedback:
            st.write("**Feedback:**")
            for item in feedback:
                st.write(f"- {item}")

if __name__ == "__main__":
    main()