//package easy;

/*
 * https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
 * Given an array A of integers, we must modify the array in the following way: 
 * we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  
 * (We may choose the same index i multiple times.)
 * Return the largest possible sum of the array after modifying it in this way.
 * 
 * Input: A = [4,2,3], K = 1
 * Output: 5
 * Explanation: Choose indices (1,) and A becomes [4,-2,3].
 * 
 */

public class largest_sum_after_k_negations {

	public static void main(String[] args) {
		
		int[] A = {4, 2, 3};
		int K = 1;
		
		System.out.println(largestSumAfterKNegations(A,K));

	}
	
    public static int largestSumAfterKNegations(int[] A, int K) {
        
        int sum = 0;
            
        for (int i = 0; i < K; i++) {
        	
        	int max = 100;
        	int smallest_index = -1;
        	
        	for (int j = 0; j < A.length; j++) {
        		if (A[j] < max) {
        			max = A[j];
        			smallest_index = j;
        		}
        	}
        	A[smallest_index] = -A[smallest_index];
        }
        
        for (int i = 0; i < A.length; i++) {
        	sum += A[i];
        }
        
        return sum;
    
        
    }

}
