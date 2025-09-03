"""
Authors: Owen Cook, Wayne Yu
Creation Date: 2025/09/03
Program: Calculates length of string excluding spaces, periods, commas, and exclamation points
"""

def countchars(st):
    # Replace specific special characters with an empty string
    st = st.replace(' ', '')
    st = st.replace('.', '')
    st = st.replace(',', '')
    st = st.replace('!', '')

    return len(st)

if __name__ == '__main__':
    print(countchars('Hello'))
    print(countchars('Hello!. !'))
    # Test special characters outside designated set
    print(countchars('??@@#^T^#'))