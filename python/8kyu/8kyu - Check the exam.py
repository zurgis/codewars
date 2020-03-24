# The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers" array and contains student's answers.

# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

# If the score < 0, return 0.

# For example:

# checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
# checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
# checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
# checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0

# Best Practices
def check_exam(arr1,arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

# My answer
def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == '':
            pass
        elif arr2[i] == arr1[i]:
            score += 4
        else:
            score -= 1
    return 0 if score < 0 else score