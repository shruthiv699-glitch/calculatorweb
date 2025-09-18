from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# ✅ Replace these with your values from Azure Portal
endpoint = "https://cog-sentiment-uni123.cognitiveservices.azure.com/"
key = "YOUR_KEY_HERE"

# Authenticate with Azure SaaS
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Example texts to analyze
documents = [
    "Azure for Students is fantastic and very helpful!",
    "I am frustrated because my deployment region was blocked."
]

# Call Azure SaaS API
response = client.analyze_sentiment(documents=documents)

# Print results
for idx, doc in enumerate(response):
    print(f"Text: {documents[idx]}")
    print(f"Sentiment: {doc.sentiment}")
    print(f"Scores: Positive={doc.confidence_scores.positive:.2f}, Neutral={doc.confidence_scores.neutral:.2f}, Negative={doc.confidence_scores.negative:.2f}")
    print("-" * 50)
