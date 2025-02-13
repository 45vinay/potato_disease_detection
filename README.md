# potato_disease_detection
# 🍃 Potato Disease Detection using CNN & Streamlit

This is a deep learning-based web application for detecting potato leaf diseases (*Early Blight, Late Blight, and Healthy). The model is trained using a "CNN (Convolutional Neural Network)" and deployed using "Streamlit".

---

## *📂 Project Structure*
potato_disease_detection/ 
  │── data_set/ │   
    ├── Train/ │   
    ├── Test/ │   
    ├── Valid/ |
├── potato_disease_model.keras 
├── background.jpg 
├── test.ipynb 
│── app.py 
│── venv/ (Optional)

2️⃣ Create a Virtual Environment (Optional)
    python -m venv venv
    Activate it:
    venv\Scripts\activate

3️⃣ Install Dependencies
    streamlit
    tensorflow
    Pillow
    numpy

**-->How to Train the Model**
  You can train the CNN model using:
   open train.ipynb in Jupyter Notebook or vscode and run the cells

**-->Run the Web App**
  streamlit run app.py
  Upload a potato leaf image
  View the disease classification
