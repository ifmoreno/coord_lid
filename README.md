# Leadership and Coordination: Weakest Link Game with Godfather Index

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![oTree](https://img.shields.io/badge/oTree-3.0+-green.svg)](https://otree.readthedocs.io/)

## Overview

This repository contains the experimental implementation of a coordination game used to study leadership effectiveness through network analysis. The experiment is part of research on identifying community leaders using the "Godfather Index" - an algorithm based on graph theory and network centrality measures.

## Experimental Design

### Game Mechanics
- **Game Type**: Weakest Link Coordination Game
- **Participants**: 4 players per group
- **Rounds**: 12 total rounds with leadership interventions
- **Payment Structure**: Minimum effort determines group payoff
- **Leadership Intervention**: Occurs at rounds 3, 6, and 9

### Key Features
- Real-time multiplayer coordination
- Dynamic payoff matrix based on minimum group effort
- Leadership identification through network analysis
- Comprehensive data collection on coordination patterns

## Technical Implementation

### Built With
- **oTree 3.0+**: Experimental framework
- **Python 3.7+**: Backend logic
- **Bootstrap**: Frontend styling
- **PostgreSQL**: Data storage 

### Project Structure
```
coordinacion/           # Main experiment app
├── models.py          # Data models and game logic
├── pages.py           # Page sequence and forms
├── templates/         # HTML templates
│   └── coordinacion/  # Game-specific templates
└── tests.py          # Automated testing

prueba/                # Pre-experiment quiz
├── models.py          # Quiz logic and validation
├── pages.py           # Quiz page sequence
├── quiz.csv           # Question database
└── templates/         # Quiz templates

pregunta_final/        # Post-experiment survey
├── models.py          # Survey data models
├── pages.py           # Survey pages
└── templates/         # Survey templates
```

## Data Collection

### Collected Variables
- **Individual**: Effort choice, demographic data, leader evaluations
- **Group**: Minimum effort, total contributions, coordination success
- **Temporal**: Round-by-round evolution of strategies

### Experimental Flow
1. **Demographics Collection**: Participant identification and basic info
2. **Instructions & Quiz**: Comprehension verification (4 questions)
3. **Main Experiment**: 12 rounds with leadership interventions
4. **Post-Experiment Survey**: Leader evaluation and group assessment

## Usage for Researchers

### Customization Options
- Modify `Constants` class in `models.py` for different group sizes
- Adjust payoff matrices in templates
- Configure leadership intervention timing
- Customize survey questions in CSV files

### Data Export
```python
# Export participant data
otree export --app-names coordinacion pregunta_final

# Generate session reports
otree admin_report
```

