# Insight Data Engineering Challenge
[Insight Data Engineering Fellows Program](https://www.insightdataengineering.com) - Coding Challenge

## Programming Language
Python 2.7.10

## Run Instruction
```
python ./src/prediction-validation.py ./input/actual.txt ./input/predicted.txt ./input/window.txt ./output/comparison.txt
```
or

```
sh ./run.sh
```

## Idea Explanation
1. **Read files and sort them:** Read actual.txt, predicted.txt and window.txt and save them as lists. Then sort actual data and predicted data: time component should be sorted in ascending order, when time component is same, then stock ID should be sorted in order of lexicography.
2. **Compute each hour's total error and number of matches:** Because predicted list and actual list are sorted, so we visit each element in list only once. For the first predicted list element, iterate actual list until find the matched pair and define this matched element's location in actual list is i. Then for the second predicted list element, iterate actual list from i+1 and so on.  If at certain time there is no data records, use 0.0 as total error and 0 as number of matches. Save total error as errors list and save number of matched pairs as counts list.
3. **Compute average error for each time window:** Iterate errors and counts list from location of start time. Sum elements within window and compute average error. To get the current sum of block of k elements just subtract the first element from the previous block and add the last element of the current block. So we only visit each element in list one time. 
4. **Edge cases:** If a certain predicted stock appears not in actual stock, console log shows error information.

Suppose n is the length of actual list, m is the length of predicted list, c is time length. Because c << n, so Time Complecity is: O(nlogn) + O(n + m) + O(n) = O(nlogn)

