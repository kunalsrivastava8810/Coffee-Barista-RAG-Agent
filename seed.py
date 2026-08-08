# seed.py

import json
import os
import time

from google import genai
from google.cloud import firestore
from google.cloud.firestore_v1.vector import Vector
from google.genai import types


# Firestore database
db = firestore.Client(database="coffee-menu")


# Vertex AI Gemini client
client = genai.Client(
    vertexai=True,
    project=os.environ.get("PROJECT_ID"),
    location="us-central1",
)


# Load menu data
with open("menu.json", "r") as f:
    menu_items = json.load(f)


# Generate embeddings and seed Firestore
for item in menu_items:

    # Use menu item name as document ID
    doc_id = item["name"].lower().replace(" ", "-")

    # Text used to generate the embedding
    text_to_embed = f"{item['name']}: {item['description']}"

    print(f"Generating embedding for: {item['name']}")

    # Generate 768-dimensional embedding
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text_to_embed,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=768,
        ),
    )

    embedding = response.embeddings[0].values

    # Add embedding to Firestore document
    item["embedding"] = Vector(embedding)

    db.collection("menu").document(doc_id).set(item)

    print(f"Seeded: {item['name']}")

    # Stay below the current 5 requests/minute quota
    time.sleep(13)


print("Firestore menu collection seeded with vector embeddings successfully!")