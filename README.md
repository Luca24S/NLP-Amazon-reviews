# Amazon Reviews Sentiment Analysis

## Overview
This project analyzes Amazon reviews of Android apps to determine sentiments (Positive, Neutral, or Negative) using a pretrained RoBERTa model. The pipeline includes preprocessing, sentiment analysis, and visualization of the data. It is based on the methodology outlined in the paper: [Multi-Domain Sentiment Analysis](https://arxiv.org/abs/1907.11692).

---

## Dataset

### Download
The dataset used for this project can be downloaded from the Stanford SNAP dataset:
- **URL**: [Amazon reviews of Android apps](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Apps_for_Android_5.json.gz)

### Data Format
The dataset is provided in JSON format, where each review is written as a single line separated by an endline.

---

## Features
1. **Text Preprocessing**:
   - Remove punctuation, lowercase text, and clean up blank lines.
   - Extract relevant features such as word count and review length.
   
2. **Sentiment Analysis**:
   - Use a pretrained RoBERTa model (`cardiffnlp/twitter-roberta-base-sentiment`) to classify reviews into Positive, Neutral, or Negative sentiments.
   
3. **Visualization**:
   - Distribution of ratings over time.
   - Number of reviews by day.
   - Comparison of actual vs predicted sentiments.

4. **Parallel Processing**:
   - Analyze reviews efficiently using multithreading for model inference.

---

## Installation

### Prerequisites
- Python 3.9 or higher

### Directory Structure

```text
project/
│
├── main.py                 # Main script to execute the pipeline
├── config.py              # Configuration settings and constants
├── utils/
│   ├── data_loader.py     # Data loading and saving utilities
│   ├── preprocessing.py    # Text preprocessing functions
│   ├── visualization.py    # Visualization functions
│   ├── sentiment_model.py  # Sentiment analysis model functions
│   ├── analysis.py        # Sentiment evaluation functions
│   └── helper_functions.py # Miscellaneous utility functions
│
├── input/                 # Directory for raw input data
├── output/                # Directory for processed data and charts
└── README.md             # Project documentation
```
---

## Usage

### 1. Download the Dataset
Download the JSON file from the link provided above and place it in the `input/` directory.

### 2. Run the Main Script
Execute the pipeline with the following command:
```bash
python main.py
```

### 3. Outputs

After running the script, the following outputs will be available:

- **Processed Data**:
  - JSON file with processed reviews and sentiment predictions.
  - File location: `output/processed_reviews.json`.

- **Visualizations**:
  - Distribution of ratings and reviews saved as PNG files in the `output/` directory.

## Results

### Validation Accuracy
The pipeline calculates the validation accuracy of the RoBERTa model on the provided dataset, comparing predicted sentiments with actual ratings.

## References

1. **Paper**: [Multi-Domain Sentiment Analysis](https://arxiv.org/abs/1907.11692)
2. **Dataset**: [Amazon reviews of Android apps](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Apps_for_Android_5.json.gz)
3. **Model**: [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)