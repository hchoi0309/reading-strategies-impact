# Reading Strategies Impact Analysis

A comprehensive statistical analysis investigating the impact of different reading strategies on text comprehension performance using repeated measures ANOVA.

## Overview

This research examines how three different reading strategies affect comprehension scores among high school students:

- **Highlighting** text while reading
- **Underlining** text while reading  
- **Passive reading** (no annotations)

The study uses a within-subjects experimental design with standardized SAT reading passages to ensure robust, comparable results.

## Experimental Design

- **Participants**: High school students (ages 15-18)
- **Materials**: Practice SAT reading passages
- **Procedure**: Randomized within-subjects design
- **Time Limit**: 13 minutes per passage
- **Measures**: Comprehension test scores (0-100%)

## Key Findings

- **Highlighting and underlining significantly improve comprehension** compared to passive reading
- **No significant difference** between highlighting and underlining strategies
- **Optimal highlighting proportion**: ~38% of text highlighted leads to peak performance (~91% score)
- **Quadratic relationship** between amount of text highlighted and comprehension scores

## Analysis Highlights

- **Statistical Methods**: Repeated measures ANOVA with Greenhouse-Geisser correction
- **Assumption Testing**: Normality, homogeneity of variance, and sphericity validation
- **Post-hoc Analysis**: Pairwise comparisons with Holm correction
- **Additional Analysis**: Regression modeling of highlighting proportion vs. performance

## 🚀 View Full Analysis

**[📋 Complete Statistical Report](main.qmd)** - Interactive Quarto document with all analyses, visualizations, and code

## 📁 Project Structure

```
├── main.qmd                    # Main analysis document (Quarto)
├── data/
│   ├── participant_responses.xls    # Raw experimental data
│   └── passages/                    # Reading passages (PDFs)
├── extract_proportions.py      # Python script for OCR text analysis
└── requirements.txt           # Python dependencies
```

## 📊 Results Summary

The analysis reveals that active reading strategies (highlighting/underlining) provide significant advantages over passive reading, with an optimal "sweet spot" for text highlighting that maximizes comprehension performance.

