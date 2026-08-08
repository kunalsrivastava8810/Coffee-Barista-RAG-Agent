<h1 align="center">☕ Coffee Barista RAG AI Agent</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Google%20ADK-Agent%20Framework-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google ADK"/>
  <img src="https://img.shields.io/badge/Gemini-Generative%20AI-8E75B2?style=for-the-badge&logo=google&logoColor=white" alt="Gemini"/>
  <img src="https://img.shields.io/badge/Vertex%20AI-Embeddings-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Vertex AI"/>
  <img src="https://img.shields.io/badge/Firestore-Vector%20Search-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firestore"/>
  <img src="https://img.shields.io/badge/Cloud%20Run-Serverless-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Cloud Run"/>
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status"/>
</p>

<p align="center">
  <strong>A production-style Retrieval-Augmented Generation (RAG) AI agent that delivers intelligent, grounded coffee recommendations.</strong>
</p>

<p align="center">
  Built with Google ADK, Gemini, Vertex AI, Firestore Vector Search, Streamlit, and Google Cloud Run.
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-key-features">Features</a> •
  <a href="#%EF%B8%8F-system-architecture">Architecture</a> •
  <a href="#-local-setup">Setup</a> •
  <a href="#%EF%B8%8F-cloud-run-deployment">Deployment</a> •
  <a href="#-testing">Testing</a>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [System Architecture](#%EF%B8%8F-system-architecture)
- [RAG Architecture](#-rag-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [How the System Works](#-how-the-system-works)
- [Firestore Data Model](#%EF%B8%8F-firestore-data-model)
- [Vector Embeddings](#-vector-embeddings)
- [Semantic Search](#-semantic-search)
- [AI Agent Behavior](#-ai-agent-behavior)
- [Google Cloud Architecture](#%EF%B8%8F-google-cloud-architecture)
- [Prerequisites](#%EF%B8%8F-prerequisites)
- [Google Cloud Setup](#%EF%B8%8F-google-cloud-setup)
- [Local Setup](#-local-setup)
- [Environment Variables](#-environment-variables)
- [Seeding Firestore](#-seeding-firestore)
- [Firestore Vector Index](#-firestore-vector-index)
- [Running the Application](#%EF%B8%8F-running-the-application)
- [Cloud Run Deployment](#%EF%B8%8F-cloud-run-deployment)
- [Testing](#-testing)
- [Security](#-security)
- [Challenges and Solutions](#%EF%B8%8F-challenges-and-solutions)
- [Performance Considerations](#-performance-considerations)
- [Error Handling](#-error-handling)
- [Project Screenshots](#-project-screenshots)
- [Example Interaction](#-example-interaction)
- [Why RAG Instead of a Normal Chatbot?](#-why-rag-instead-of-a-normal-chatbot)
- [Potential Real-World Applications](#-potential-real-world-applications)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Architecture Summary](#-architecture-summary)
- [Project Status](#-project-status)
- [Author](#-author)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Overview

**Coffee Barista RAG AI Agent** is an AI-powered virtual barista that provides intelligent, grounded coffee recommendations.

The project combines:

- Generative AI
- Retrieval-Augmented Generation (RAG)
- Semantic vector search
- Google ADK
- Gemini embeddings
- Firestore Vector Search
- Streamlit
- Google Cloud Run

Instead of relying solely on the language model's internal knowledge, the agent retrieves relevant information from a controlled coffee menu **before** generating a response — making the system more reliable, grounded, and suitable for applications where responses must stay tied to a specific knowledge base.

---

## 🎯 Problem Statement

Traditional AI chatbots can generate responses that sound convincing but don't correspond to the actual products or information available in an application.

For example, a customer might ask:

> "Do you have a matcha frappuccino?"

If the chatbot relies purely on a general-purpose LLM, it might incorrectly invent a product.

A real restaurant assistant should instead understand:

- What products are available
- What each product contains
- Which products match a customer's preferences
- Which products should **not** be recommended
- Which products satisfy dietary restrictions

The system therefore needs a mechanism to ground AI responses in a reliable data source.

---

## 💡 Solution

This project solves the problem using **Retrieval-Augmented Generation (RAG)**.

```
User Query
    ↓
AI Agent
    ↓
Generate Query Embedding
    ↓
Firestore Vector Search
    ↓
Retrieve Relevant Menu Items
    ↓
Provide Retrieved Context to Agent
    ↓
Gemini Generates Grounded Response
    ↓
Response to User
```

The AI agent doesn't need to memorize the entire menu — it dynamically retrieves relevant information from Firestore.

---

## 🎯 Project Objectives

- [x] Build an AI-powered coffee recommendation agent
- [x] Implement Retrieval-Augmented Generation
- [x] Store structured menu information in Firestore
- [x] Generate semantic vector embeddings for menu items
- [x] Implement vector similarity search
- [x] Ground AI responses using retrieved information
- [x] Prevent hallucinated menu items
- [x] Support dietary and allergen-aware recommendations
- [x] Deploy the application to Google Cloud Run
- [x] Demonstrate a production-style cloud AI architecture

---

## ✨ Key Features

### ☕ Intelligent Coffee Recommendations

The agent understands natural-language requests.

**Example:** `"Recommend something strong and warm."` → retrieves **Espresso** and generates an appropriate recommendation.

### 🔎 Retrieval-Augmented Generation

The agent retrieves relevant menu information before generating a response, improving grounding and reducing hallucinations.

### 🧠 Semantic Search

The system uses vector embeddings rather than relying only on keyword matching.

**Example:** `"Something powerful and hot"` retrieves **Espresso**, even though those exact words don't appear in the menu description.

### 🛡️ Out-of-Menu Protection

The agent avoids recommending products that don't exist in the menu.

```
User: Do you have a matcha frappuccino?

Agent: Politely explains the product isn't available
       instead of inventing a menu item.
```

### 🥛 Dietary-Aware Recommendations

The agent responds to dietary restrictions.

**Example:** `"I'm lactose intolerant. What can I get?"` → suggests **Oat Milk Latte, Espresso, Cold Brew**, while avoiding inappropriate dairy-based options.

### ☁️ Serverless Cloud Deployment

Deployed on Google Cloud Run:

- Serverless infrastructure
- HTTPS endpoint
- Automatic scaling
- Containerized execution
- No server management
- Native Google Cloud integration

### 🎨 Interactive UI

A simple, conversational interface built with Streamlit.

---

## 🏗️ System Architecture

```
                         ┌───────────────────────┐
                         │        USER            │
                         │ "Recommend something   │
                         │  strong and warm"      │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │      STREAMLIT         │
                         │       app.py           │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │      GOOGLE ADK        │
                         │       AI AGENT         │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   QUERY EMBEDDING      │
                         │  Gemini Embeddings     │
                         └───────────┬───────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │        CLOUD FIRESTORE          │
                    │                                  │
                    │       Menu Collection            │
                    │                                  │
                    │   ┌────────────────────────┐    │
                    │   │ Menu Data               │    │
                    │   │ +                       │    │
                    │   │ 768D Vector Embedding   │    │
                    │   └────────────────────────┘    │
                    │                                  │
                    │       Vector Search              │
                    └───────────────┬──────────────────┘
                                    │
                                    ▼
                         ┌───────────────────────┐
                         │  RETRIEVED CONTEXT     │
                         │ Relevant Menu Items    │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │    GEMINI + ADK        │
                         │   Grounded Generation  │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │      FINAL ANSWER      │
                         │ Coffee Recommendation  │
                         └───────────────────────┘
```

---

## 🧠 RAG Architecture

### Phase 1 — Indexing

```
menu.json
    ↓
Read Menu Data
    ↓
Generate Embeddings
    ↓
Gemini Embedding Model
    ↓
768-Dimensional Vector
    ↓
Firestore
```

### Phase 2 — Retrieval

```
User Question
    ↓
Query Embedding
    ↓
Vector Similarity Search
    ↓
Top Relevant Menu Items
    ↓
Retrieved Context
    ↓
Gemini / ADK
    ↓
Grounded Answer
```

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Google ADK | AI agent framework |
| Gemini | Generative AI |
| Gemini Embeddings | Semantic vector generation |
| Vertex AI | AI/ML infrastructure |
| Firestore | NoSQL database |
| Firestore Vector Search | Semantic retrieval |
| Streamlit | Web interface |
| Cloud Run | Serverless deployment |
| Google Cloud IAM | Access management |
| Cloud Shell | Cloud development environment |

---

## 📁 Project Structure

```
coffee-barista-rag-agent/
│
├── app.py               # Streamlit user interface
├── agent.py              # AI agent and RAG logic
├── menu.json              # Coffee menu knowledge base
├── seed.py                # Embedding generation and Firestore seeding
├── requirements.txt        # Python dependencies
├── README.md                # Project documentation
└── .gitignore                 # Git ignored files
```

---

## 🔄 How the System Works

1. **User Query** — the user enters a natural-language request, e.g. `"I want something strong and warm."`
2. **Query Processing** — the AI agent interprets the request and transforms it into an embedding representation.
3. **Vector Search** — the query embedding is compared against menu item embeddings stored in Firestore.
4. **Context Retrieval** — relevant menu information is retrieved (e.g. *Espresso: A concentrated coffee served hot.*)
5. **Grounded Generation** — the retrieved information is supplied to the AI agent.
6. **User Response** — the final grounded recommendation is displayed in Streamlit.

---

## 🗃️ Firestore Data Model

- **Database:** `coffee-menu`
- **Collection:** `menu`

Each document represents a menu item:

```json
{
  "name": "Espresso",
  "description": "A concentrated coffee served hot.",
  "embedding": [0.0123, -0.0456, 0.0789, "... 765 more dimensions"]
}
```

The actual embedding contains **768 dimensions**.

---

## 🧠 Vector Embeddings

The project uses `gemini-embedding-001` to generate semantic representations of menu items.

| Config | Value |
|---|---|
| Task Type | `RETRIEVAL_DOCUMENT` |
| Dimensions | `768` |

Generated vectors are stored in Firestore using Firestore's native vector type.

---

## 🔍 Semantic Search

Traditional keyword search requires exact terms. Vector search understands semantic relationships instead.

**Example:** `"Something powerful and hot"` retrieves **Espresso** because the semantic meaning is similar, even without matching keywords.

---

## 🤖 AI Agent Behavior

The agent follows these principles:

| Principle | Description |
|---|---|
| **Grounded Responses** | Use information retrieved from the menu |
| **No Invented Products** | If a product doesn't exist, never claim that it does |
| **Dietary Awareness** | Respect user-provided dietary restrictions |
| **Helpful Alternatives** | When a requested product is unavailable, suggest suitable available alternatives |

---

## ☁️ Google Cloud Architecture

```
Google Cloud
│
├── Cloud Run
│   └── Coffee Barista Application
│
├── Firestore
│   └── coffee-menu
│       └── menu collection
│
├── Vertex AI
│   └── Gemini Embeddings
│
├── Google ADK
│   └── Agent Logic
│
└── IAM
    └── Service Accounts & Permissions
```

### 🔐 Service Account

The deployment uses a dedicated service account: **`barista-agent-sa`**, used by the deployed application to interact with required Google Cloud services.

---

## ⚙️ Prerequisites

Before running the project locally, install:

- Python 3.10+ (3.12 recommended)
- Git
- Google Cloud SDK
- A Google Cloud project
- Firestore enabled
- Vertex AI access

---

## ☁️ Google Cloud Setup

**1. Authenticate**

```bash
gcloud auth login
```

**2. Set project**

```bash
gcloud config set project YOUR_PROJECT_ID
# Example:
gcloud config set project rag-ai-agent-504815
```

**3. Set region**

```bash
export REGION=asia-south2
```

**4. Enable required APIs**

```bash
gcloud services enable \
  run.googleapis.com \
  firestore.googleapis.com \
  aiplatform.googleapis.com \
  cloudbuild.googleapis.com
```

**5. Create the Firestore database**

```bash
gcloud firestore databases create \
  --database="coffee-menu" \
  --location=$REGION
```

---

## 🧪 Local Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/coffee-barista-rag-agent.git
cd coffee-barista-rag-agent
```

**2. Create a virtual environment**

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Cloud Shell / Linux / macOS:

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=asia-south2
```

Windows PowerShell:

```powershell
$env:PROJECT_ID="YOUR_PROJECT_ID"
$env:REGION="asia-south2"
```

Verify:

```bash
echo $PROJECT_ID
echo $REGION
```

---

## 🌱 Seeding Firestore

The `seed.py` script:

1. Reads `menu.json`
2. Generates embeddings
3. Creates 768-dimensional vectors
4. Adds embeddings to menu items
5. Stores documents in Firestore

Run:

```bash
python seed.py
```

Expected output:

```
Generating embedding for: Espresso
Seeded: Espresso

Generating embedding for: Oat Milk Latte
Seeded: Oat Milk Latte

...

Firestore menu collection seeded with vector embeddings successfully!
```

---

## 🔎 Firestore Vector Index

The vector index must match the embedding dimension used by `seed.py` — **768**.

```bash
gcloud firestore indexes composite create \
  --collection-group=menu \
  --query-scope=COLLECTION \
  --database="coffee-menu" \
  --field-config=field-path=embedding,vector-config='{"dimension":"768","flat":"{}"}'
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501).

---

## ☁️ Cloud Run Deployment

```bash
gcloud run deploy coffee-barista \
  --source . \
  --region $REGION \
  --service-account barista-agent-sa@$PROJECT_ID.iam.gserviceaccount.com \
  --allow-unauthenticated
```

Cloud Run builds and deploys the application as a serverless service.

**Deployment region:** `asia-south2`

> Note: the embedding client used during setup was configured separately for the available Gemini embedding quota (see [Architecture Summary](#-architecture-summary)).

---

## 🧪 Testing

| # | Scenario | Input | Expected Result | Status |
|---|---|---|---|---|
| 01 | Strong & warm coffee | `Recommend something strong and warm.` | Recommends **Espresso** | ✅ Pass |
| 02 | Unavailable product | `Do you have a matcha frappuccino?` | Politely declines instead of inventing a product | ✅ Pass |
| 03 | Lactose intolerance | `I'm lactose intolerant, what can I get?` | Suggests dairy-free options (Oat Milk Latte, Espresso, Cold Brew) | ✅ Pass |

---

## 🔐 Security

The project follows basic cloud security principles.

- **Service Accounts** — a dedicated service account is used instead of embedding credentials in the application.
- **IAM** — access is controlled using Google Cloud IAM.
- **Secrets** — never commit `.env`, `service-account.json`, `credentials.json`, API keys, private keys, or access tokens.

### 🚫 Recommended `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual environment
venv/
.venv/
env/

# Environment variables
.env
.env.*

# Google Cloud credentials
*-service-account.json
service-account.json
credentials.json

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Cache
.cache/

# Streamlit
.streamlit/secrets.toml
```

---

## ⚠️ Challenges and Solutions

### Challenge 1 — Cloud Run IAM Error

- **Problem:** Cloud Run initially failed with a permission error involving `storage.objects.get`.
- **Cause:** The build process required appropriate permissions for the build service account.
- **Solution:** Granted the required Cloud Run Builder IAM permission to the appropriate service account.

### Challenge 2 — Embedding Model Error

- **Problem:** The original configuration attempted to use `text-embedding-004`, which was unavailable in the selected configuration.
- **Solution:** Updated to `gemini-embedding-001` with 768-dimensional output.

### Challenge 3 — Embedding Quota

- **Problem:** Encountered `429 RESOURCE_EXHAUSTED`.
- **Cause:** The project had a low requests-per-minute quota for the Gemini embedding model.
- **Solution:** Throttled the Firestore seeding process with a delay between embedding requests (e.g. `time.sleep(13)`).

### Challenge 4 — Firestore Vector Compatibility

- **Problem:** The vector index dimension must match the generated embedding dimension.
- **Solution:** Configured both embedding generation and the Firestore vector index for 768 dimensions.

---

## 📈 Performance Considerations

The current implementation is optimized for a small menu. A production-scale implementation could add:

- Batch embedding generation
- Asynchronous processing
- Caching
- Retry with exponential backoff
- Query result caching
- Larger embedding quotas
- Monitoring
- Automated indexing

---

## 🔁 Error Handling

Potential errors include:

- Empty queries
- Unknown products
- Firestore connection failures
- Embedding API errors
- Quota exhaustion
- Invalid menu data
- Missing environment variables
- Authentication failures

> Production deployments should use appropriate retry and backoff mechanisms for transient API failures.

---

## 📸 Project Screenshots

Add your actual screenshots to:

```
screenshots/
├── app-interface.png
├── recommendation.png
├── allergen-test.png
├── firestore-vector-search.png
└── cloud-run-deployment.png
```

Then reference them in the README:

```markdown
## Application Interface

![Coffee Barista UI](screenshots/app-interface.png)
```

---

## 💻 Example Interaction

> **User:** Recommend something strong and warm.
>
> **AI Barista:** I'd recommend an Espresso. It's a concentrated coffee served hot, making it a great option if you're looking for something strong and warm.

---

## 🧠 Why RAG Instead of a Normal Chatbot?

**Traditional LLM**

```
User → LLM → Answer
```

A general LLM can potentially hallucinate information.

**RAG Architecture**

```
User → Query Embedding → Vector Search → Relevant Menu Data → LLM → Grounded Answer
```

This architecture provides greater control over the information used by the AI agent.

---

## 🌎 Potential Real-World Applications

<details>
<summary><strong>🛍️ E-Commerce — Product recommendation assistant</strong></summary>

```
Customer Query → Product Vector Search → Relevant Products → AI Recommendation
```
</details>

<details>
<summary><strong>🏢 Enterprise Knowledge Assistant</strong></summary>

```
Employee Question → Knowledge Base Search → Relevant Documents → AI Answer
```
</details>

<details>
<summary><strong>🧑‍💻 Developer Documentation Assistant</strong></summary>

```
Developer Question → Documentation Retrieval → Relevant Documentation → AI Explanation
```
</details>

<details>
<summary><strong>🍽️ Restaurant Assistant</strong></summary>

```
Customer Preferences → Menu Vector Search → Relevant Food Items → AI Recommendation
```
</details>

---

## 🔮 Future Improvements

- [ ] Conversation memory
- [ ] User authentication
- [ ] Order placement & shopping cart
- [ ] Payment integration
- [ ] Real-time menu management
- [ ] Admin dashboard
- [ ] Multi-location support
- [ ] Multilingual support
- [ ] Voice-based ordering (speech-to-text / text-to-speech)
- [ ] Personalized recommendations
- [ ] Hybrid keyword + vector search
- [ ] Automated RAG evaluation
- [ ] Cloud Logging & Monitoring
- [ ] CI/CD with GitHub Actions
- [ ] Automated Firestore indexing
- [ ] Production caching & rate limiting
- [ ] Observability dashboard

### 🧪 Possible Advanced Architecture

```
                         ┌──────────────┐
                         │     User      │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │  Streamlit / Web    │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │   Google ADK        │
                     │    AI Agent         │
                     └─────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                 ▼             ▼             ▼
          ┌────────────┐ ┌───────────┐ ┌────────────┐
          │ Firestore   │ │ Gemini     │ │  External   │
          │ Vector DB   │ │ Embedding  │ │  Tools      │
          └──────┬─────┘ └───────────┘ └────────────┘
                 │
                 ▼
          ┌────────────┐
          │ Retrieved   │
          │  Context    │
          └──────┬─────┘
                 │
                 ▼
          ┌────────────┐
          │  Gemini     │
          │ Generation  │
          └──────┬─────┘
                 │
                 ▼
          ┌────────────┐
          │   Final     │
          │  Response   │
          └────────────┘
```

---

## 📚 Learning Outcomes

This project provided practical experience with:

| Domain | Skills |
|---|---|
| **Artificial Intelligence** | Generative AI, AI agents, prompt grounding, RAG architecture, semantic retrieval |
| **Machine Learning** | Vector embeddings, similarity search, embedding dimensionality, retrieval systems |
| **Cloud Computing** | Google Cloud Platform, Cloud Run, Vertex AI, Firestore, Cloud Shell |
| **Software Engineering** | Python, modular architecture, environment variables, dependency management, cloud deployment |
| **Cloud Security** | IAM, service accounts, least-privilege concepts, credential management |

---

## 📊 Architecture Summary

| Component | Implementation |
|---|---|
| AI Agent | Google ADK |
| LLM | Gemini |
| Embedding Model | `gemini-embedding-001` |
| Embedding Size | 768 |
| Vector Database | Cloud Firestore |
| Vector Search | Firestore Vector Search |
| Frontend | Streamlit |
| Deployment | Cloud Run |
| Cloud Platform | Google Cloud |
| Primary Region | `asia-south2` |
| Embedding Client Region | `us-central1` |
| Database | Firestore Native |
| Programming Language | Python |

---

## 🏁 Project Status

🟢 **COMPLETED**

- [x] Developed
- [x] Grounded with Firestore
- [x] Embedded using Gemini
- [x] Configured for Vector Search
- [x] Deployed to Cloud Run
- [x] Tested with multiple user scenarios

---

## 👨‍💻 Author

**Kunal Srivastava**
B.Tech Computer Science Engineering

Areas of interest: Artificial Intelligence · Data Analytics · Generative AI · Cloud Computing · Cybersecurity · Software Development

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

```bash
# 1. Create a feature branch
git checkout -b feature/your-feature

# 2. Commit your changes
git add .
git commit -m "Add new feature"

# 3. Push your changes
git push origin feature/your-feature
```

Then open a Pull Request.

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐.

---

## 📄 License

This project is intended for educational, demonstration, and portfolio purposes. If you plan to reuse or distribute it, add an appropriate open-source license such as [MIT](https://opensource.org/licenses/MIT).

<p align="center">
  <strong>☕ From a simple coffee menu to a grounded AI experience.</strong>
  <br><br>
  Built with ❤️ using Google Cloud, Gemini, Google ADK, Firestore, and Streamlit.
</p>
