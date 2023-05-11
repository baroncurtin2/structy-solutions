package introduction

import "fmt"

func toFloat(num interface{}) (*float64, error) {
	var result float64

	switch val := num.(type) {
	case int:
		result = float64(val)
	case float32:
		result = float64(val)
	case float64:
		result = val
	case uint:
		result = float64(val)
	default:
		return nil, fmt.Errorf("unsupported type: %T", num)
	}

	return &result, nil
}
