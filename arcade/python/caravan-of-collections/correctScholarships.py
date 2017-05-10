def correctScholarships(bestStudents, scholarships, allStudents):
    return set(scholarships) < set(allStudents) and set(bestStudents) <= set(scholarships)
