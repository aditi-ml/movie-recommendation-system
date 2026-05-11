# 🎬 Movie Recommendation System

A mood-based movie recommendation system built with Python and Streamlit, 
using Content-based and Collaborative Filtering on the MovieLens dataset.

🌐 **Live Demo:** [Try it here!](https://aditi-movie-recommender.streamlit.app/)

---

## 📌 Problem Statement

Finding the right movie can be overwhelming with thousands of options. 
This system recommends movies based on your **current mood** and 
**preferred genres** using machine learning techniques.

---

## 🎯 Features

- 🎭 **Mood-based filtering** — Happy, Sad, Romantic, Adventurous, Chill, Thrilling, Family
- 🎬 **Genre selection** — Filter by Action, Comedy, Drama, Horror and more
- 🎲 **Surprise me** — Random mood and genre picker
- 📊 **Scored recommendations** — Ranked by mood fit, genre match & popularity
- ▶️ **Watch trailer** — Direct YouTube trailer link for each movie

---

## 🤖 Recommendation Techniques

| Technique | Description |
|---|---|
| **Content-based Filtering** | Matches movies by genre similarity using cosine similarity |
| **Collaborative Filtering** | Uses community ratings from MovieLens dataset |
| **Hybrid Scoring** | Combines genre score + avg rating + popularity |

---

## 📊 Dataset

- **Source:** [MovieLens](https://grouplens.org/datasets/movielens/)
- **Files:** `movies.csv`, `ratings.csv`
- **Size:** 9,000+ movies, 100,000+ ratings

---

## ⚙️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)

---

## 🚀 How to Run

```bash
pip install streamlit pandas scikit-learn
streamlit run app.py
```

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── app.py                    # Main Streamlit app
├── hybrid_recommender.py     # Recommendation logic
├── movies.csv                # MovieLens movies dataset
├── ratings.csv               # MovieLens ratings dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 👩‍💻 Author

**Aditi Prasad**  
BCA @ BIT Mesra, Ranchi  
📧 pdaditi002@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/aditi-prasad-4a56b1329)

---

## 🎓 Project Guide

**Dr. Jaya Pal**  
BIT Mesra, Ranchi
