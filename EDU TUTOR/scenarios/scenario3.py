def generate_diagnostic_quiz(level):
    prompt = f"Create a diagnostic quiz for a {level} level student in math."
    return llm.generate(prompt)

def adapt_quiz(diagnostic_score):
    if diagnostic_score < 50:
        return generate_diagnostic_quiz("beginner")
    elif diagnostic_score < 80:
        return generate_diagnostic_quiz("intermediate")
    else:
        return generate_diagnostic_quiz("advanced")

# Simulate
score = 72
adaptive_quiz = adapt_quiz(score)
print(adaptive_quiz)