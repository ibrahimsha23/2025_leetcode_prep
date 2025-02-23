import java.util.Arrays;


class MergeSortedArray{
    public static void main(String[] args){
        int[] nums1 = {1, 2, 5, 0, 0, 0};
        int[] nums2 = {2, 3, 6};
        int m = 3;
        int n = 3;
        int k = m +n;
        System.out.println(nums1);
        while (m > 0 & n >0){
            System.out.println("Iteration of:"+k);
            System.out.println(Arrays.toString(nums1));
            System.out.println(Arrays.toString(nums2));
            if (nums1[m-1] > nums2[n-1]){
                nums1[k-1] = nums1[m-1];
                m--;
            }else{
                nums1[k-1] = nums2[n-1];
                n--;
            }
        k--;
        System.out.println(Arrays.toString(nums1));

        }
        System.out.println(Arrays.toString(nums1));

        // initializing array
        // int[] arr = { 1, 2, 3, 4, 5 };

        // // size of array
        // int n = arr.length;


        // System.out.println(arr);
        // traversing array
    //     for (int i = 0; i < n; i++){
    //         System.out.print(arr[i] + " ");
    // }

    }
}