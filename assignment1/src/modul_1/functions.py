import warnings
from typing import List, Optional


def find_best_threshold(thresholds: List[float],
                        tp: List[int],
                        fn: List[int],
                        tn: Optional[List[int]] = None,
                        fp: Optional[List[int]] = None) -> Optional[float]:
    """
    Finds the best threshold where recall >= 0.9 and maximizes precision (if FP is provided).

    Args:
        thresholds (list): List of threshold values.
        tp (list): List of true positives for each threshold.
        fn (list): List of false negatives for each threshold.
        tn (list, optional): List of true negatives for each threshold (optional).
        fp (list, optional): List of false positives for each threshold (optional).

    Returns:
        float or None: The best threshold that yields recall >= 0.9 and maximizes precision
                       (if FP is provided). If no threshold meets the condition, returns None.
    """
    
    best_threshold, best_precision = None, -1
    valid_thresholds = []

    # Collect all input lists to validate length and non-negative values
    input_lists = [thresholds, tp, fn] + [lst for lst in [tn, fp] if lst]

    # Validate all input values: all must be non-negative
    if not all(all(val >= 0 for val in lst) for lst in input_lists if lst):
        raise ValueError("All inputs must be non-negative.")

    # Ensure no empty lists are provided
    if any(len(lst) == 0 for lst in input_lists):
        raise ValueError("All input lists must be non-empty.")

    # Ensure all input lists have the same length
    if not all(len(lst) == len(thresholds) for lst in input_lists):
        raise ValueError("All input lists must have the same length.")

    # Loop through thresholds and evaluate recall and precision
    for i, threshold in enumerate(thresholds):
        # Check to avoid division by zero for recall calculation
        if tp[i] + fn[i] == 0:
            warnings.warn("Both true positive and false negative are zero, recall cannot be calculated.",
                          UserWarning)
            continue  # Skip this threshold if recall can't be calculated

        recall = tp[i] / (tp[i] + fn[i])
        
        # Check if recall meets the requirement (>= 0.9)
        if recall >= 0.9:
            valid_thresholds.append(threshold)

            # Check for zero inputs before calculating precision
            if fp and (tp[i] + fp[i]) == 0:
                warnings.warn("Both true positive and false positive are zero; precision cannot be calculated.",
                              UserWarning)
                continue  # Skip the rest of this iteration

            # If FP is provided, calculate precision
            if fp and (tp[i] + fp[i]) > 0:
                precision = tp[i] / (tp[i] + fp[i])
                # Update the best threshold if this one has better precision
                if precision > best_precision:
                    best_threshold, best_precision = threshold, precision

    # If no precision was calculated (FP and TN not provided), use minimum valid threshold
    return best_threshold or (min(valid_thresholds) if valid_thresholds else None)
