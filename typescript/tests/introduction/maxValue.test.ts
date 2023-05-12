import {
	findMax,
	findMaxDivideAndConquer,
} from '../../src/introduction/maxValue';

interface TestCase {
	readonly numbers: number[];
	readonly maxVal: number;
}

describe('maxValue.ts', () => {
	const tests: Array<TestCase> = [
		{
			numbers: [4, 7, 2, 8, 10, 9],
			maxVal: 10,
		},
		{
			numbers: [10, 5, 40, 40.3],
			maxVal: 40.3,
		},
		{
			numbers: [-5, -2, -1, -11],
			maxVal: -1,
		},
		{
			numbers: [42],
			maxVal: 42,
		},
		{
			numbers: [1000, 8],
			maxVal: 1000,
		},
		{
			numbers: [1000, 8, 9000],
			maxVal: 9000,
		},
		{
			numbers: [2, 5, 1, 1, 4],
			maxVal: 5,
		},
	];

	tests.forEach((testCase, idx) => {
		it(`testCase: ${idx}`, () => {
			expect(findMax(testCase.numbers)).toBe(testCase.maxVal);
			expect(findMaxDivideAndConquer(testCase.numbers)).toBe(
				testCase.maxVal
			);
		});
	});
});
