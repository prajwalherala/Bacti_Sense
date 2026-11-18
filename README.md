# BactiSense – Predictive Machine Learning for Bacterial Antibiotic Resistance

## Project Overview

BactiSense is a machine learning project developed to predict bacterial antibiotic resistance using patient and bacterial isolate information.

The application classifies an isolate–antibiotic record into one of two categories:

- **Resistant (R):** The bacterial isolate is classified as resistant to the selected antibiotic.
- **Susceptible (S):** The bacterial isolate is classified as susceptible to the selected antibiotic.

The project combines data preprocessing, exploratory data analysis, machine learning and Streamlit to build an interactive prediction application.

This project was developed as part of my data science learning journey, with an interest in applying machine learning to real-world healthcare-related problems.

## Objectives

- Explore and understand bacterial antibiotic susceptibility data.
- Perform data cleaning and preprocessing.
- Identify patterns and relationships within the dataset.
- Develop a machine learning classification model.
- Evaluate model performance using appropriate classification metrics.
- Deploy the trained model through an interactive Streamlit application.

## Dataset

The dataset used in this project was obtained from Kaggle.

**Dataset:** Multi-Resistance Antibiotic Susceptibility  
**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/adilimadeddinehosni/multi-resistance-antibiotic-susceptibility)

The dataset contains information related to bacterial isolates, patient characteristics and antibiotic susceptibility.

The dataset is not included in this repository. Download it from the original Kaggle source and place it in the project directory using the filename expected by the notebook.

## Features Used

The application accepts the following input features:

- Age
- Gender
- Organism
- Diabetes
- Hypertension
- Previous hospitalisation
- Infection frequency
- Antibiotic

These features are passed to the trained machine learning pipeline to generate a prediction.

## Technologies and Tools

| Category | Tools |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git and GitHub |

## Project Workflow

The project follows these major stages:

1. **Data Collection:** Obtained the bacterial antibiotic susceptibility dataset from Kaggle.
2. **Exploratory Data Analysis:** Examined the dataset, distributions, patterns and relationships between variables.
3. **Data Preprocessing:** Prepared numerical and categorical features for machine learning.
4. **Model Development:** Trained and evaluated classification models.
5. **Model Evaluation:** Analysed classification performance using metrics such as accuracy, precision, recall, F1-score and confusion matrix.
6. **Model Deployment:** Saved the trained model and integrated it into a Streamlit application.
7. **Prediction:** Accepted user inputs and generated Resistant or Susceptible predictions.

## Application Features

- Interactive input form for patient and bacterial isolate information.
- Organism and antibiotic selection.
- Binary classification of antibiotic resistance.
- Prediction probability display.
- Clean and user-friendly interface.
- Educational disclaimer regarding the use of predictions.

## Project Structure

```text
Bacti_Sense/
│
├── app.py
├── Bacti_sense.ipynb
├── antibiotic_model.pkl
├── requirements.txt
├── project.txt
├── .gitignore
└── README.md
```

The dataset must be downloaded separately from Kaggle.

## Installation and Execution

Follow these steps to run the application locally.

**1. Clone the repository**

```bash
git clone https://github.com/prajwalherala/Bacti_Sense.git
```

**2. Navigate to the project directory**

```bash
cd Bacti_Sense
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

For Windows:

```bash
venv\Scripts\activate
```

**5. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the Streamlit application**

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Model Evaluation

The trained classification model was evaluated using standard classification metrics.

The evaluation focused on:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics help assess how effectively the model distinguishes between resistant and susceptible bacterial isolates.

## Limitations and Disclaimer

BactiSense is an educational machine learning project and has not been clinically validated.

The predictions are intended only for demonstration and learning purposes. They must not be used for clinical diagnosis, antibiotic selection, prescribing decisions or patient treatment.

Actual antibiotic susceptibility testing and clinical decisions must be performed by qualified healthcare professionals using validated laboratory methods.

## Future Improvements

- Explore additional machine learning algorithms.
- Improve model performance and generalisation.
- Include more diverse and representative datasets.
- Add detailed model explainability.
- Improve the application with additional analytical features.

## Author

**Prajwal Herala U**

Data Science Learner

[GitHub](https://github.com/prajwalherala)

---

This project represents my practical learning in data analysis, machine learning, model evaluation and application development.