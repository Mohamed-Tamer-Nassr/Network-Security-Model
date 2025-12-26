# Network Security System: Phishing & Malicious Website Detection

![Project Banner](images/about.png)

## 📌 Project Overview

The **Network Security System** is a machine learning-powered web application designed to detect whether a website is **safe** or **malicious** (phishing). By analyzing various network and URL-based features—such as SSL state, domain age, and URL structure—the system predicts potential security threats with high accuracy.

This project aims to enhance cybersecurity by providing users and organizations with a tool to identify risky domains proactively, leveraging a robust **ETL (Extract, Transform, Load)** and **Training Pipeline**.

## 🚀 Key Features

- **Machine Learning Analysis**: Utilizes advanced classification algorithms to detect phishing patterns.
- **Dual Prediction Modes**:
  - **Batch Prediction**: Upload a CSV file containing multiple URL entries for bulk analysis.
  - **Manual Input**: Interactive form for testing individual URL features.
- **Automated Pipeline**: End-to-end ML pipeline handling Data Ingestion, Validation, Transformation, and Model Training.
- **Web Interface**: User-friendly UI built with **FastAPI** and **Jinja2** templates.
- **Database Integration**: Stores training data and logs using **MongoDB**.

## 🏗️ System Architecture

The system follows a modular architecture:

1.  **Data Ingestion**: Reads data from source (MongoDB/CSV), splits into train/test sets.
2.  **Data Validation**: Checks for schema consistency and data drift.
3.  **Data Transformation**: Handles missing values, scaling, and feature engineering.
4.  **Model Trainer**: Trains the model using classification algorithms (e.g., Random Forest, Gradient Boosting) and saves the best model.
5.  **Prediction Service**: Exposes APIs and UI for real-time inference.

## 🛠️ Technologies Used

- **Programming Language**: Python 3.8+
- **Web Framework**: FastAPI, Uvicorn
- **Frontend**: HTML5, TailwindCSS, Jinja2
- **Database**: MongoDB (via PyMongo)
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Containerization**: Docker
- **Logging & Monitoring**: Custom Logging, Exception Handling

## 📸 Visual Walkthrough & Screenshots

### 1. How It Works

_Detailed overview of the detection flow and system logic._
![How It Works](images/how_it_works.png)

### 2. Manual Prediction Interface

_Interactive form for checking specific website features manually._
![Manual Input](images/manual_input_form.png)

### 3. Batch Upload & Prediction

_Upload CSV files for bulk website scanning._
![Upload Interface](images/upload_file_image.png)

### 4. Prediction Results

_Clear, tabulated results showing safe vs. malicious status._
![Results](images/result.png)

## 📂 Folder Structure

```bash
networkSystemML/
├── networksecurity/        # Core ML package
│   ├── components/         # Ingestion, Validation, Transformation, Training
│   ├── pipeline/           # Training and Prediction pipelines
│   ├── entity/             # Config and Artifact definitions
│   └── utils/              # Helper functions
├── templates/              # HTML Frontend templates
├── static/                 # CSS/JS assets
├── images/                 # Project screenshots
├── main.py                 # Entry point for ML Training Pipeline
├── app.py                  # Entry point for Web Application (FastAPI)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
└── README.md               # Project documentation
```

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MongoDB Account (URI required)
- Docker (optional)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/network-security-ml.git
cd networkSystemML
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory and add your MongoDB connection string:

```env
MONGODB_URL_KEY="mongodb+srv://<username>:<password>@cluster.mongodb.net/..."
```

## 🚀 Usage

### Running the Web Application

Start the FastAPI server:

```bash
python app.py
```

Access the application at: `http://localhost:8000`

### Running the Training Pipeline

To manually trigger the ETL and Model Training process:

```bash
python main.py
```

## 🔮 Future Improvements

- [ ] **Real-time URL Scanning**: Integrate with a live crawler to extract features from a raw URL automatically.
- [ ] **API Authentication**: Secure the API endpoints for external integration.
- [ ] **Cloud Deployment**: Deploy to AWS/Azure using CI/CD pipelines.
- [ ] **Dashboard**: Add a dashboard for visualizing historical threat statistics.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
