def build_business_analysis_prompt(
    dataset_summary: dict,
    statistics: dict,
    missing_values: dict
):

    prompt = f"""
    Analyze the following business dataset.

    DATASET SUMMARY:{dataset_summary}

    STATISTICS:{statistics}

    MISSING VALUE ANALYSIS:{missing_values}

    Generate:
    1. Key business insights
    2. Important trends
    3. Potential risks
    4. Recommendations
    5. Executive summary

    Keep the response business-oriented and concise.
    """

    return prompt