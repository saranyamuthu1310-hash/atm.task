import streamlit as st

# Initialize Balance
if "Balance" not in st.session_state:
    st.session_state.Balance = 5000

st.title("🏦 ATM Management System")

# PIN Verification
pin = st.text_input("Enter PIN", type="password")

if pin:
    if pin == "1234":
        st.success("Login Successful")

        choice = st.selectbox(
            "Select an Option",
            ("Check Balance", "Deposit", "Withdraw")
        )

        if choice == "Check Balance":
            st.info(f"Current Balance: {st.session_state.Balance}")

        elif choice == "Deposit":
            deposit = st.number_input(
                "Enter Deposit Amount",
                min_value=0,
                step=1
            )

            if st.button("Deposit"):
                st.session_state.Balance += deposit
                st.success(
                    f"Amount Deposited Successfully!\n\nCurrent Balance: {st.session_state.Balance}"
                )

        elif choice == "Withdraw":
            withdraw = st.number_input(
                "Enter Withdrawal Amount",
                min_value=0,
                step=1
            )

            if st.button("Withdraw"):
                if withdraw > st.session_state.Balance:
                    st.error("Insufficient Funds")
                else:
                    st.session_state.Balance -= withdraw
                    st.success(
                        f"Withdrawal Successful!\n\nCurrent Balance: {st.session_state.Balance}"
                    )

    else:
        st.error("Invalid PIN")
