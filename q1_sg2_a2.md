Annex C
# Code Quality Assessment Worksheet

Section: PINATUBO Score:____________

C#4,5,6 / Name: ESDRELON, DUCUSIN, DE LEON Date: 8/16/2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

PseudoCode 2

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm



Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm

Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- 

Checklist to guide your answer:

2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- 


3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- 


4. Testability
Which algorithm is easier to test with different inputs? Why?
-

5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
-

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
-
