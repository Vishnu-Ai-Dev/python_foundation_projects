# Python Foundation Projects — Applied Implementations

A collection of standalone Python projects demonstrating the practical application of core fundamentals. This repository documents the transition from basic programming syntax to real-world data handling, API integration, and visualization.

## Overview
This repository represents the second phase of a structured learning path, focusing on applied scripts and small-scale applications. Moving beyond theoretical exercises, each project folder contains a distinct implementation emphasizing specific operational skills necessary for data science and software engineering workflows.

**Period:** April 2026  
**Environment:** Python 3.12, VS Code, Jupyter Notebook  
**Focus:** Bridging foundational logic with real-world data streams and visual outputs  

## Repository Structure

    python_foundation_projects/
    ├── anime_password_generater/    # External API integration, JSON parsing
    ├── attendance_log_system/       # State management, dictionary operations
    └── tamil_nadu_budget/           # Data cleaning, matplotlib visualization

## Technical Progression

### Project 1: Smart Attendance System
Established foundational application state management through a terminal-based interface:
* Continuous execution loops coupled with conditional branching
* Instant state updates utilizing O(1) dictionary key-value lookups
* Input sanitization via string manipulation methods to prevent user-entry errors

**Key Learning:** Managed persistent application state and dynamic data modification without relying on external databases.

### Project 2: Dynamic API Password Generator
Transitioned to network-based data retrieval and algorithmic randomization:
* Algorithmic string generation combining multiple data types and punctuation
* REST API integration utilizing the `requests` library
* JSON payload extraction, dictionary traversal, and list compilations

**Key Learning:** Successfully connected a local script to a live external database (Jikan REST API) to dynamically pull, clean, and utilize remote data.

### Project 3: Tamil Nadu Budget Analysis (2025-26)
Introduced standard data science libraries for real-world tabular data processing:
* Dataset ingestion and manipulation using `pandas`
* Structural data cleaning, specifically handling null/NaN values using imputation methods
* Comparative and proportional data visualization utilizing `matplotlib.pyplot` (Bar and Pie charts)

**Key Learning:** Demonstrated the critical data engineering concept that real-world datasets require systematic cleaning prior to mathematical or visual analysis.

## Technical Decisions
* **Why the Requests library?** It is the industry standard for synchronous HTTP calls in Python, providing a necessary bridge to web-based data.
* **Why Pandas for a small dataset?** To build architectural muscle memory. Utilizing dataframes for small datasets prepares the workflow for large-scale dataset manipulation in future machine learning tasks.
* **Why strict folder modularity?** Enforcing a "1 Project = 1 Folder" architecture prevents environment dependency conflicts and maintains repository hygiene, aligning with professional version control standards.

## Learning Methodology
**40/40/20 Rule Applied:**
* 40% independent problem-solving on paper before coding
* 40% syntax lookup and official documentation reading
* 20% AI assistance for debugging and architectural logic

## Next Steps
This applied foundation enables progression to:
* Integrating Scikit-learn for baseline predictive modeling
* Transitioning from static CSV files to automated database queries
* Implementing object-oriented principles within data analysis pipelines
* Handling real world messy datas
---
*Note: This repository represents learning progression, not production code. Implementations prioritize functional understanding and readability over extreme optimization.*
