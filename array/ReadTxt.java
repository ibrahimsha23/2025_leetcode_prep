
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


class ReadTxt {

    public static void overwriteFile(Integer counter) throws Exception {

        boolean append = false;
        counter = counter + 1;
        try (FileWriter writer = new FileWriter("counter.txt", append)) {
            writer.write(Integer.toString(counter));
            System.out.println("Counter is updated in file successfully");
        } catch (IOException e) {
        }
    }

    public static void main(String[] args) throws Exception {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Enter the title");
            String inputData = reader.readLine();
            System.out.println("inputData:" + inputData);

            File fileObj = new File("counter.txt");
            Scanner scanObj = new Scanner(fileObj);
            String data = "";
            while (scanObj.hasNextLine()) {
                data = scanObj.nextLine();
                System.out.println(data);
                 if (data instanceof String) {
                    System.out.println("The value is a String.");
                } else {
                    System.out.println("Unknown data type.");
                }
            }
            scanObj.close();
            if (data != null) {
                System.out.println(data);
                Integer counter = Integer.parseInt(data);
                overwriteFile(counter);
            }

        } catch (FileNotFoundException e) {
            System.out.println("File not found, an error occured");
            e.printStackTrace();
        }

    }
}
