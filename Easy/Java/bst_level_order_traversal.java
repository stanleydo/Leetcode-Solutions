//package easy;

/*
 * 
 * https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
 * 
 * Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
 * (ie, from left to right, level by level from leaf to root).
 * For example: Given binary tree [3,9,20,null,null,15,7],
 * return its bottom-up level order traversal as:
 * [[15,7],[9,20],[3]]
 * 
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class bst_level_order_traversal {
	
	public static void main(String[] args) {
		TreeNode root_r_r = new TreeNode(7);
		TreeNode root_r_l = new TreeNode(15);
		TreeNode root_l = new TreeNode(9);
		TreeNode root_r = new TreeNode(20, root_r_l, root_r_r);
		TreeNode root = new TreeNode(3, root_l, root_r);
		
		System.out.println(Solution.levelOrderBottom(root));
	}
	
	static class Solution {
	    public static List<List<Integer>> levelOrderBottom(TreeNode root) {
	    	
	    	List<List<Integer>> ans = new ArrayList<List<Integer>>();
	    	
	    	if (root == null) {
	    		return ans;
	    	}
	    	
	    	List<Tuple> ans_tuples = new ArrayList<Tuple>();
	    	
	    	Queue<Tuple> queue = new LinkedList<Tuple>();
	    	
	    	Tuple first = new Tuple(root, 0);
	    	
	    	queue.add(first);
	    	
	    	while (!queue.isEmpty()) {
	    		Tuple cur = queue.poll();
	    		ans_tuples.add(cur);
	    		
	    		if (cur.node.left != null) {
	    			queue.add(new Tuple(cur.node.left, cur.depth+1));
	    		}
	    		
	    		if (cur.node.right != null) {
	    			queue.add(new Tuple(cur.node.right, cur.depth+1));
	    		}
	    		
	    	}
	    	
	    	for (Tuple tuple : ans_tuples) {

	    		if (ans.size() != tuple.depth+1) {
	    			List<Integer> start = new ArrayList<Integer>();
	    			start.add(tuple.node.val);
	    			ans.add(0, start);
	    		} else {
	    			List<Integer> col = ans.get(0);
	    			col.add(tuple.node.val);
	    		}
	    		
	    		
	    	}
	    	
	    	return ans;
	    	
	    }
	}

}

class Tuple {
	TreeNode node;
	int depth;
	Tuple(TreeNode node, int depth) {
		this.node = node;
		this.depth = depth;
	}
}

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode() {}
	TreeNode(int val) {this.val = val;}
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
	
	
}
