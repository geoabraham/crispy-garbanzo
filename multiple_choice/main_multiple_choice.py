from Question import Question

question_prompts = [
    "Pregunta 1\n(a) Respuesta 1\n(b) Respuesta 2\n(c) Respuesta 3\n",
    "Pregunta 2\n(a) Respuesta 1\n(b) Respuesta 2\n(c) Respuesta 3\n",
    "Pregunta 3\n(a) Respuesta 1\n(b) Respuesta 2\n(c) Respuesta 3\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print(score)


run_test(questions)
