package Java.arrays_and_hashing;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
    public static void main(String[] args) {
        ContainsDuplicate cd = new ContainsDuplicate();
        System.out.println(cd.containsDuplicate(new int[]{1, 2, 3, 1}));
        System.out.println(cd.containsDuplicate(new int[]{1, 2, 3, 4}));
        System.out.println(cd.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4}));
        System.out.println(cd.containsDuplicate(new int[]{}));
    }

    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            if(seen.contains(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
        }
        return false;
    }
}
