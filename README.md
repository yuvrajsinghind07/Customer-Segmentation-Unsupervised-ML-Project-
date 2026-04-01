# Customer Segmentation using KMeans Algorithm (Unsupervised ML Project)

##  About the Project

In this project, I tried to understand different types of customers by grouping them based on their data. The idea was simple — instead of looking at customers individually, we can divide them into groups with similar behavior.

This helps businesses make better decisions like whom to target, what kind of offers to give, etc.

---

##  What I did

* Cleaned the dataset and handled missing values
* Converted categorical data into numerical form
* Scaled the data for better performance
* Applied KMeans clustering to group customers
* Used Elbow Method and Silhouette Score to choose the best number of clusters
* Visualized the clusters using PCA

---

##  Results

* Found **3 customer groups**
* Silhouette Score was around **0.21**
* Clusters are not perfectly separate, but still useful

---

##  Customer Groups

* **Experienced Professionals** → Middle-aged people with good work experience
* **Senior Customers** → Older people with lower work activity
* **Young Families** → Younger people with larger family size

---

## Business Insights

**Based on the clustering results, a few useful patterns were observed:**

* **Experienced Professionals**
These customers have good work experience and are relatively stable.
 They can be targeted with premium services, long-term plans, or high-value products.
* **Senior Customers**
This group consists of older individuals with lower work activity.
 They may prefer simple, easy-to-understand products and low-risk options.
* **Young Families**
These are younger customers with larger family sizes.
   They are ideal for family-oriented offers, discounts, and bundled services.

  ---

## Visualization

I used PCA to reduce the data into 2D and plot the clusters.

The graph shows that:

* Some groups overlap
* One group is more clearly separated
* This is normal in real-world data

---

## Pipeline Approach

Built an end-to-end pipeline that includes:

Data preprocessing (imputation, encoding, scaling)
Clustering model (KMeans)

This ensures that the model can directly handle raw input data during deployment.

---

##  Tools Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

##  Deployment

A simple Streamlit app is created where users can input their details and get their customer segment.

Run locally:

streamlit run app.py

---
## Live Demo Deployment(Streamlit app)

 * Click here :
https://deovd6eehhcr89gsxfzgza.streamlit.app/

---

##  Final Thoughts

This project helped me understand how to work with real-world data and how businesses can use data to understand their customers better.

---

## Project Structure
```
Customer-Segmentation-ML/
│
├── data/
│     └── customer_segmentation.csv
│
├── model/
│     ├── customer_segmentation_pipeline.pkl
│
├── Customer Segmentation.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

##  Author

**Yuvraj Singh**
