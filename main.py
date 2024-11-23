# Import libraries
import streamlit as st
import pandas as pd
from PIL import Image
import joblib

# Load the model from disk
model = joblib.load(r"./Models/model.sav")

# Import preprocessing function
from preprocessing import preprocess

# Inject custom CSS for neon-themed buttons and background image
def set_custom_background():
    st.markdown(
        """
        <style>
        body {
            background-image: url('Background.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #333;
        }

        .stButton > button {
            background-color: #ff7eb3;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            box-shadow: 0px 5px 10px rgba(255, 126, 179, 0.6);
            transition: transform 0.3s, background-color 0.3s;
        }

        .stButton > button:hover {
            background-color: #ff9ec7;
            transform: scale(1.1);
        }

        .stSidebar {
            background-color: rgba(255, 255, 255, 0.8) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display Project Synopsis content
def display_project_synopsis():
    st.subheader("Project Synopsis")
    synopsis = """
    - **Name / Title of the Project**: Churn Prediction for a Telecom Company  
    - **Statement about the Problem**:  
      The telecom industry faces significant challenges in retaining customers, with many customers switching to competitors. This issue, known as customer churn, directly impacts revenue and growth. The goal of this project is to predict which customers are likely to leave the service, allowing the company to implement retention strategies proactively.  
    - **Why is the Particular Topic Chosen?**:  
      Churn prediction is crucial for the telecom sector as retaining existing customers is more cost-effective than acquiring new ones. With fierce competition, predicting customer churn helps maintain profitability and customer satisfaction.  
    - **Objective and Scope of the Project**:  
      The project aims to develop a predictive model to accurately forecast customer churn based on historical data. It involves data collection, preprocessing, model development, and evaluation to reduce churn rates and improve loyalty.  
    - **Methodology**:  
      - Data Collection: Customer usage patterns, billing history, demographics, and interactions.  
      - Data Preprocessing: Handle missing values, scale features, encode variables.  
      - Model Development: Use algorithms like Logistic Regression, Random Forest, Gradient Boosting.  
      - Evaluation: Measure performance using accuracy, precision, recall, and F1-score.  
    - **Tools and Technologies**:  
      Python, Scikit-learn, Pandas, MySQL, Jupyter Notebook, PyCharm, Git/GitHub.  

    For full details, refer to the project's documentation.
    """
    st.markdown(synopsis)

# Display Data Visualization content
def display_data_visualization():
    st.subheader("Data Visualization")
    st.info("Explore the visual insights derived from the data and model.")

    # Display each visualization with captions
    viz_images = {
        "ChurnVsNoChurn based on Monthly Charges Histogram": "A histogram comparing churn and no-churn customers based on their monthly charges.",
        "ChurnVsNoChurn based on Tenure Histogram": "This visualization shows the tenure distribution for churned vs non-churned customers.",
        "ChurnVsNoChurn for categorical features": "A count plot that breaks down churn for different categorical features.",
        "ChurnVsNoChurn Pie Chart": "A pie chart providing an overall view of churned and non-churned customers.",
        "Correlation between the Numeric Features": "A heatmap showing correlations among numeric features in the dataset.",
        "Count Plot for various categorical features": "This plot shows the count distribution for various categorical features in the dataset.",
        "Histogram of all Numeric Features": "This visualization displays the distribution of all numeric features in the dataset."
    }

    # Loop through and display each image with description
    for image_name, description in viz_images.items():
        st.image(f"images/{image_name}.png", caption=image_name, use_column_width=True)
        st.markdown(f"**Description**: {description}")
        st.markdown("---")  # Add a divider

# Main function
def main():
    # Set page configuration
    st.set_page_config(page_title="Telco Churn Prediction System", layout="centered")
    
    # Apply Background
    set_custom_background()

    # Sidebar for Navigation
    st.sidebar.title("Navigation")
    st.sidebar.image("university_logo.jpg", width=150)  # Replace with your university's logo file
    option = st.sidebar.radio("Choose Prediction Type:", 
                              ("Landing Page", "Online Prediction", "Batch Prediction", "Project Synopsis", "Data Visualization"))

    if option == "Landing Page":
        # Landing Page with University Details
        st.image("university_logo.jpg", width=200)  # Replace with your university's logo file
        st.title("Dev Bhoomi Uttarakhand University")
        st.markdown("<h2>Minor Project: Telco Customer Churn Prediction System</h2>", unsafe_allow_html=True)
        
        # Details in Two Columns
        col1, col2 = st.columns(2)

        # Project Guide Block
        with col1:
            st.subheader("Project Guide")
            st.image("adarsh_tiwari.jpg", width=150, caption="Mr. Adarsh Tiwari")  # Replace with Mr. Tiwari's profile picture file
            st.markdown("""**Mr. Adarsh Tiwari**  
            (ByteXL)  
            """)

        # Project Submitted By Block
        with col2:
            st.subheader("Project Submitted By")
            col2_1, col2_2 = st.columns(2)
            with col2_1:
                st.image("anshul.jpg", width=100, caption="Anshul")  # Replace with Anshul's profile picture file
                st.markdown("""**Anshul**  
                ERP: 22BTCSE0200  
                B.Tech CSE, 3rd Year  
                """)
            with col2_2:
                st.image("ishika_saxena.jpg", width=100, caption="Ishika Saxena")  # Replace with Ishika's profile picture file
                st.markdown("""**Ishika Saxena**  
                ERP: 22BTCSEAI0026  
                B.Tech CSE (AIML), 3rd Year  
                """)

        # Button to Redirect to Online Prediction
        if st.button("Go to Prediction System"):
            st.session_state["redirect_to"] = "Online Prediction"

    if option == "Project Synopsis":
        display_project_synopsis()

    if option == "Data Visualization":
        display_data_visualization()

    # Online Prediction Page
    if option == "Online Prediction" or st.session_state.get("redirect_to") == "Online Prediction":
        st.session_state["redirect_to"] = None  # Reset redirection state
        st.header("Online Prediction")
        st.info("Fill in the customer details below for prediction:")

        # Collect input features from user
        seniorcitizen = st.selectbox('Senior Citizen:', ('Yes', 'No'))
        dependents = st.selectbox('Dependent:', ('Yes', 'No'))
        tenure = st.slider('Tenure (Months):', min_value=0, max_value=72, value=0)
        contract = st.selectbox('Contract:', ('Month-to-month', 'One year', 'Two year'))
        paperlessbilling = st.selectbox('Paperless Billing:', ('Yes', 'No'))
        paymentmethod = st.selectbox('Payment Method:', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
        monthlycharges = st.number_input('Monthly Charges:', min_value=0, max_value=150, value=0)
        totalcharges = st.number_input('Total Charges:', min_value=0, max_value=10000, value=0)
        multiplelines = st.selectbox("Multiple Lines:", ('Yes', 'No', 'No phone service'))
        phoneservice = st.selectbox('Phone Service:', ('Yes', 'No'))
        internetservice = st.selectbox('Internet Service:', ('DSL', 'Fiber optic', 'No'))
        onlinesecurity = st.selectbox('Online Security:', ('Yes', 'No', 'No internet service'))
        onlinebackup = st.selectbox('Online Backup:', ('Yes', 'No', 'No internet service'))
        techsupport = st.selectbox('Tech Support:', ('Yes', 'No', 'No internet service'))
        streamingtv = st.selectbox('Streaming TV:', ('Yes', 'No', 'No internet service'))
        streamingmovies = st.selectbox('Streaming Movies:', ('Yes', 'No', 'No internet service'))

        # Prepare data
        data = {
            'SeniorCitizen': seniorcitizen,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phoneservice,
            'MultipleLines': multiplelines,
            'InternetService': internetservice,
            'OnlineSecurity': onlinesecurity,
            'OnlineBackup': onlinebackup,
            'TechSupport': techsupport,
            'StreamingTV': streamingtv,
            'StreamingMovies': streamingmovies,
            'Contract': contract,
            'PaperlessBilling': paperlessbilling,
            'PaymentMethod': paymentmethod,
            'MonthlyCharges': monthlycharges,
            'TotalCharges': totalcharges
        }
        features_df = pd.DataFrame.from_dict([data])
        st.dataframe(features_df)

        preprocess_df = preprocess(features_df, 'Online')
        if st.button('Predict'):
            prediction = model.predict(preprocess_df)
            if prediction == 1:
                st.warning('Yes, the customer will terminate the service.')
            else:
                st.success('No, the customer is happy with Telco Services.')

    # Batch Prediction Page
    if option == "Batch Prediction":
        st.header("Batch Prediction")
        st.info("Upload a CSV file to predict churn for multiple customers.")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.dataframe(data.head())
            preprocess_df = preprocess(data, "Batch")
            if st.button('Predict'):
                prediction = model.predict(preprocess_df)
                prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
                prediction_df = prediction_df.replace({
                    1: 'Yes, the customer will terminate the service.',
                    0: 'No, the customer is happy with Telco Services.'
                })
                st.dataframe(prediction_df)

if __name__ == '__main__':
    main()
