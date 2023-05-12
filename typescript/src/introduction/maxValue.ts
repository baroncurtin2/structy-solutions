function findMax(numbers: number[]): number {
	let max = -Infinity;

	for (const num of numbers) {
		if (num > max) {
			max = num;
		}
	}

	return max;
}

function findMaxDivideAndConquer(numbers: number[]): number {
	return findMaxDivideAndConquerHelper(numbers, 0, numbers.length - 1);
}

function findMaxDivideAndConquerHelper(
	numbers: number[],
	low: number,
	high: number
): number {
	if (low === high) {
		return numbers[low];
	}

	const mid = Math.floor((low + high) / 2);

	const leftMax = findMaxDivideAndConquerHelper(numbers, low, mid);
	const rightMax = findMaxDivideAndConquerHelper(numbers, mid + 1, high);

	return Math.max(leftMax, rightMax);
}

export { findMax, findMaxDivideAndConquer };
