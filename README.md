# Agent Harness

A flexible framework for building and running AI agents with modular skills, tools, and persistent state management. Built with Python, async PostgreSQL (via SQLAlchemy + asyncpg), and OpenRouter for LLM integration.

## Introduction

Agent Harness lets you define **skills** (as Markdown files) that describe an agent’s capabilities, load them dynamically, and execute tasks with tooling support. It’s designed for:

- **Skill‑based agent loading** – drop a `SKILL.md` into `skills/` and the harness discovers it.
- **Asynchronous database storage** – uses PostgreSQL to keep conversation history, agent state, and metadata.
- **Tool integration** – extend agents with custom tools (planned structure under `tools/`).
- **LLM agnosticism** – connects to any model via OpenRouter (set your API key).

The project is still evolving – contributions are welcome!

## Startup Guide

### Prerequisites

- Python 3.10 or higher
- Docker + Docker Compose (for running PostgreSQL)
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`

### Step 1: Clone the repository

```bash
git clone https://github.com/your-org/agent-harness.git
cd agent-harness