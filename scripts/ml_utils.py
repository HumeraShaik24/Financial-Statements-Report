import streamlit as st
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

def run_ml(df):
    st.header("🤖 Machine Learning")

    if 'target' not in df.columns:
        st.warning("Please make sure your dataset contains a 'target' column for ML.")
        return

    X = df.drop('target', axis=1)
    y = df['target']

    problem_type = detect_problem_type(y)
    st.write(f"Detected problem type: {problem_type}")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model, best_params = tune_model(X_train, y_train, problem_type)
    st.write(f"Best hyperparameters: {best_params}")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if problem_type == 'classification':
        st.subheader("Classification Report")
        st.text(classification_report(y_test, y_pred))

        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', ax=ax)
        st.pyplot(fig)

    else:
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        r2 = r2_score(y_test, y_pred)
        st.write(f"RMSE: {rmse}")
        st.write(f"R^2 Score: {r2}")

        st.subheader("Residual Plot")
        fig, ax = plt.subplots()
        sns.residplot(x=y_test, y=y_pred, lowess=True, ax=ax, line_kws={'color': 'red', 'lw': 1})
        st.pyplot(fig)

def detect_problem_type(y):
    if y.dtype == 'object' or y.nunique() < 20:
        return 'classification'
    else:
        return 'regression'

def tune_model(X_train, y_train, problem_type):
    if problem_type == 'classification':
        model = RandomForestClassifier(random_state=42)
        param_grid = {
            'n_estimators': [50, 100],
            'max_depth': [None, 10, 20]
        }
    else:
        model = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [50, 100],
            'max_depth': [None, 10, 20]
        }
    grid_search = GridSearchCV(model, param_grid, cv=3)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_