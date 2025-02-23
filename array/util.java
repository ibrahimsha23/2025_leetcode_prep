import java.io.BufferedReader;
import java.io.InputStreamReader;


public class util{
    public static void main(String[] args) {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String inputData;
        try {
            System.out.println("Enter the title");
            inputData = reader.readLine();
            System.out.println("inputData:" + inputData);

        }
        catch(Exception e){
            System.err.println("Hello error welcome , to see u back");

        }
        System.out.println("I am ibrahim riz, will achieve the step one");        
    }

}