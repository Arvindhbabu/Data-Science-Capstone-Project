# 🚀 SpaceY Launch Prediction Dashboard

An interactive machine learning-powered web dashboard that predicts the success of SpaceX booster landings using public data, logistic regression, and modern data visualization tools.

> 🌐 Live App: [Click here to visit](https://your-streamlit-link.streamlit.app)  
> 📁 Repo: [GitHub Source Code](https://github.com/your-username/spacey-dashboard)

---

## 🧠 Project Overview

This capstone project simulates the role of a **data scientist at SpaceY**, a fictional competitor to SpaceX. Using publicly available SpaceX launch data, we:

- Predict whether the **booster will land successfully**
- Visualize success rates across **orbits** and **launch sites**
- Provide an interactive tool for engineers and stakeholders

---

## 📊 Features

| Feature | Description |
|--------|-------------|
| 🚀 **Launch Simulation Inputs** | Select payload mass, orbit type, booster version, and launch site |
| ✅ **Booster Landing Prediction** | ML model predicts whether the booster will land |
| 📈 **Prediction Confidence** | Displays probability/confidence in prediction |
| 🌐 **Launch Site Map** | Interactive Folium map showing launch locations |
| 📉 **Orbit vs Success Rate** | Plotly visualization of orbit-wise success trends |

---

## 💻 Tech Stack

- **Python 3.10**
- **Pandas, NumPy** – Data wrangling
- **Scikit-learn** – Model training (Logistic Regression)
- **Joblib** – Model serialization
- **Plotly** – Interactive orbit visualizations
- **Folium + streamlit-folium** – Maps
- **Streamlit** – Dashboard frontend & backend

---

## 📁 Project Structure

spacey_capstone/

├── dashboard/                 
│   ├── app.py                 
│   ├── model.pkl              
│   └── scaler.pkl  

│data/  
       └── cleaned_spacex_launches.csv  

| notebooks/                
       └── SpaceY_Modeling.ipynb   

│
├── requirements.txt          
| README.md             


---

## 🚧 How It Works

1. Load historical SpaceX launch data
2. Clean and one-hot encode categorical variables
3. Train a **logistic regression** model to predict success (1 = landed, 0 = failed)
4. Build a **Streamlit dashboard** to accept launch parameters as user input
5. Predict in real-time and display result + visualizations

---

## 📦 Installation & Local Use

```bash
git clone https://github.com/your-username/spacey-dashboard.git
cd spacey-dashboard
pip install -r requirements.txt
streamlit run dashboard/app.py


