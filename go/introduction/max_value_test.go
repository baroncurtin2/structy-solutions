package introduction

import (
	"testing"

	"github.com/stretchr/testify/require"
)

var testCases = []struct {
	numbers  []interface{}
	maxValue float64
}{
	{
		numbers:  []interface{}{4, 7, 2, 8, 10, 9},
		maxValue: 10,
	},
	{
		numbers:  []interface{}{10, 5, 40, 40.3},
		maxValue: 40.3,
	},
	{
		numbers:  []interface{}{-5, -2, -1, -11},
		maxValue: -1,
	},
	{
		numbers:  []interface{}{42},
		maxValue: 42,
	},
	{
		numbers:  []interface{}{1000, 8},
		maxValue: 1000,
	},
	{
		numbers:  []interface{}{1000, 8, 9000},
		maxValue: 9000,
	},
	{
		numbers:  []interface{}{2, 5, 1, 1, 4},
		maxValue: 5,
	},
}

func Test_maxValue(t *testing.T) {
	for _, tc := range testCases {
		actualMax, err := maxValue(tc.numbers)

		require.NoError(t, err)
		require.NotEmpty(t, actualMax)
		require.NotNil(t, actualMax)
		require.Equal(t, tc.maxValue, *actualMax)
	}
}

func Test_maxValueDivideAndConquer(t *testing.T) {
	for _, tc := range testCases {
		actualMax, err := maxValueDivideAndConquer(tc.numbers)

		require.NoError(t, err)
		require.NotEmpty(t, actualMax)
		require.NotNil(t, actualMax)
		require.Equal(t, tc.maxValue, *actualMax)
	}
}

func Test_maxValueDivideAndConquerConcurrency(t *testing.T) {
	for _, tc := range testCases {
		actualMax, err := maxValueDivideAndConquerConcurrency(tc.numbers)

		require.NoError(t, err)
		require.NotEmpty(t, actualMax)
		require.NotNil(t, actualMax)
		require.Equal(t, tc.maxValue, *actualMax)
	}
}
