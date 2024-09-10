import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Simple Calculator",  # Title of the webpage
    page_icon="https://example.com/calculator-icon.png",  # URL to your favicon file
    layout="centered",
    initial_sidebar_state="auto"
)

# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Custom CSS to enhance the style
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stNumberInput>div>div>input {
        border-radius: 8px;
        border: 2px solid #4CAF50;
    }
    .stRadio>div>label {
        color: #4CAF50;
    }
    .stTitle {
        font-size: 2rem;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title("💡 **Simple Calculator**")

# Layout: Using columns for better alignment
col1, col2 = st.columns(2)

with col1:
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    
with col2:
    num2 = st.number_input("Enter the second number", value=0.0)

# Radio buttons for operation choice
operation = st.radio("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the chosen operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    # Display the result with some styling
    st.markdown(f"""
        <div style="font-size: 1.5rem; color: #333;">
            The result of {operation.lower()}ing <b>{num1}</b> and <b>{num2}</b> is ~ <span style="color: #4CAF50;">{result}</span>
        </div>
        """, unsafe_allow_html=True)
