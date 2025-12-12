## 🌱 FOUNDATION — Day 1 (Generative AI Learning Summary)

Today marks the official start of my Generative AI learning journey.
I focused on setting up my structure, understanding the core concepts, and building the foundation needed to create real LLM, RAG, and Agent applications.

This file captures a brief, clean summary of everything I learned today.

## ⚡ 1. How a Generative AI App Works

A modern AI system follows this flow:
```
User Input → Prompt → Model → Output Parsing → (Memory) → (RAG) → Final Answer
```

This helped me understand how all components fit together in an actual application.

## ⚙️ 2. What LangChain Is

LangChain is a framework that helps build modular, structured, production-ready AI apps.

Today I learned that LangChain allows:

- Connecting prompts → models → memory → retrievers

- Building pipelines with LCEL (prompt | model | parser)

- Handling complex AI workflows with simple blocks

LangChain = the toolkit for modern LLM applications.

## 🧩 3. Key LangChain Components I Learned Today

These are the essential blocks of any LLM system:

- Models

- Prompts

- Output Parsing

- Runnables & LCEL

- Chains

- Memory

- Indexes

- Tools / Agents (later)

Today I explored the first seven.

## 🤖 4. Models — The Brain of the System

I learned the 3 types of models used in Generative AI:

LLM Models

Generate text → summaries, descriptions, answers.

Chat Models

Understand conversations → used for chatbots and agents.

Embedding Models

Convert text → vectors → used for RAG.

Key point:

Models don’t remember anything. They need memory, prompts, and indexes.

## 💬 5. Prompts — How We Control the Model

Prompts are instructions we give the model.

I learned:

- PromptTemplate

- ChatPromptTemplate

- Few-shot learning

- Prompt variables

- How to structure a good prompt

- How prompts connect into pipelines

- Good prompts = better output.

## 🔗 6. Chains — Automating Multi-Step Workflows

Chains help connect multiple components into a pipeline.

Today I learned:

- Sequential Chains

- Parallel Chains

- Map-Reduce Chains

- LCEL pipelines (prompt | model | parser)

LCEL is the modern, cleaner way to build chains.

## 🧠 7. Memory — Making the AI Remember

Today I learned that memory helps an AI app maintain conversation context.

Memory types:

- Buffer Memory

- Buffer Window Memory

- Summary Memory

- Entity Memory

Memory is essential for chatbots and agents.

## 📚 8. Indexes — The Foundation of RAG

Indexes allow an LLM to search and retrieve knowledge.

The 4 components of an Index:

- Documents

- Text Splitters

- Embeddings

- Vector Stores

This becomes a retriever, which powers RAG systems.

## 🎯 9. Overall Understanding from Today

By the end of Day 1, I now understand:

How LLM apps function end-to-end

What LangChain is and why it’s useful

The core components (models, prompts, parsing, chains, memory, indexes)

Basics of RAG structure

How everything will fit together when I start building apps

Today = foundation day.
Tomorrow = practical coding day.
