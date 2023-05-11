package introduction

import (
	"fmt"
	"math"
)

func maxValue(numbers []interface{}) (*float64, error) {
	maxVal := math.Inf(-1)

	for _, num := range numbers {
		val, err := toFloat(num)

		if err != nil {
			return nil, err
		}

		if *val > maxVal {
			maxVal = *val
		}
	}

	return &maxVal, nil
}

func maxValueDivideAndConquer(numbers []interface{}) (*float64, error) {
	return maxValDCHelper(numbers, 0, len(numbers)-1)
}

func maxValDCHelper(numbers []interface{}, low int, high int) (*float64, error) {
	if low == high {
		val, _ := toFloat(numbers[low])
		return val, nil
	}

	mid := (low + high) / 2

	leftMax, leftErr := maxValDCHelper(numbers, low, mid)
	rightMax, rightErr := maxValDCHelper(numbers, mid+1, high)

	if leftErr != nil || rightErr != nil {
		return nil, fmt.Errorf("could not find maximum value")
	}

	if *leftMax > *rightMax {
		return leftMax, nil
	} else {
		return rightMax, nil
	}
}

func maxValueDivideAndConquerConcurrency(numbers []interface{}) (*float64, error) {
	return maxValDCHelperConcurrency(numbers, 0, len(numbers)-1)
}

func maxValDCHelperConcurrency(numbers []interface{}, low int, high int) (*float64, error) {
	if low == high {
		val, _ := toFloat(numbers[low])
		return val, nil
	}

	mid := (low + high) / 2

	// create channels to receive max values from left and right
	leftChan := make(chan *float64)
	rightChan := make(chan *float64)

	// launch goroutunes to find max values in left and right paths
	go findMaxConcurrently(numbers, low, mid, leftChan)
	go findMaxConcurrently(numbers, mid+1, high, rightChan)

	// receive max values
	leftMax := <-leftChan
	rightMax := <-rightChan

	if leftMax == nil || rightMax == nil {
		return nil, fmt.Errorf("could not find maximum value")
	}

	if *leftMax > *rightMax {
		return leftMax, nil
	} else {
		return rightMax, nil
	}
}

func findMaxConcurrently(numbers []interface{}, low int, high int, maxChan chan<- *float64) {
	maxVal, err := maxValDCHelperConcurrency(numbers, low, high)

	if err == nil {
		maxChan <- maxVal
	}
}
