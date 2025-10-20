

### Project: Sentiment Analysis and Topic Modeling on Amazon Product Reviews**

### **Overview**

In this project, I analyzed thousands of Amazon product reviews to understand how customers feel about different products and what topics they talk about the most.
The main goal was to identify overall sentiment (positive, neutral, or negative) and uncover hidden patterns in customer opinions using advanced NLP techniques.


### **What I Did**

I started by cleaning and preparing the text data, removing links, symbols, and stopwords, and converting everything to lowercase. Then I explored the dataset visually to see how sentiments and text lengths were distributed.

To classify the reviews, I first built a **baseline machine learning model** using **TF-IDF** and **Logistic Regression**, which gave an accuracy of about **88%**.

After that, I moved on to an advanced **Transformer-based model (DistilBERT)** for fine-tuning. Using the **Hugging Face Transformers** library, I trained the model on the cleaned dataset, which improved accuracy to around **92%**. This showed how powerful deep learning can be for understanding text meaning and context.

Once I had sentiment predictions, I wanted to dig deeper to understand *what* people were talking about. So, I applied **BERTopic**, a modern topic modeling technique that combines **Sentence Transformers**, **UMAP**, and **HDBSCAN**.
This helped group reviews into meaningful topics such as:

* Coffee flavor and aroma
* Shipping and packaging quality
* Product ingredients and nutrition
* Pricing and customer satisfaction

---

### **Tools & Techniques**

* **Python Libraries:** Pandas, NumPy, Scikit-learn, NLTK, Matplotlib, Seaborn
* **Deep Learning:** Hugging Face Transformers (DistilBERT), PyTorch
* **Topic Modeling:** BERTopic, UMAP, HDBSCAN
* **Visualization:** Power BI, Seaborn, BERTopic visualizer

---

### **Key Results**

✅ Processed and analyzed over **50,000 customer reviews**
✅ Improved sentiment prediction accuracy from **88% (Logistic Regression)** to **92% (DistilBERT)**
✅ Discovered **10 major topics** representing common customer discussions
✅ Reduced manual feedback review time by **over 70%**
✅ Helped uncover actionable insights such as product taste preferences, packaging issues, and pricing concerns

---

### **Business Impact**

The insights from this project can help e-commerce and marketing teams understand customer experiences at scale.
By identifying key sentiment drivers and recurring themes, businesses can improve product quality, tailor marketing messages, and enhance customer satisfaction.


### **Summary**

“This project showcases how Natural Language Processing can turn thousands of unstructured reviews into meaningful business intelligence. From data cleaning and visualization to BERT-based modeling and topic discovery, I applied the full data science pipeline to uncover insights that directly support product and marketing decisions.”

---

