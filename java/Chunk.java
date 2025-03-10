import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8,}; // Sample array
        int k = 3;  // Subarray size
        int n = arr.length;
        int i = 0;
        int end = k;

        List<int[]> data = new ArrayList<>();

        while (i < n) {

            end = Math.min(end, arr.length);
            // Ensure we don't go out of bounds
            int[] subArray = Arrays.copyOfRange(arr, i, end);
            data.add(subArray);
            System.out.println(data);

            i = end;
            end += 3;
        }

        // Print the subarrays
        for (int[] sub : data) {
            System.out.println(Arrays.toString(sub));
        }
    }

}