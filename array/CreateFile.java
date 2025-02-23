
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


class CreateFile {


    public static String JAVA_CODE = """
            public class GeneratedClass {
                public static void main(String[] args) {
                    System.out.println("Hello from the dynamically created Java class!");
                }
            }
            """;

    public static Boolean createFile(String fileName){
        Boolean created = false;

        return created;
    }


    public static void overwriteFile(String filename, boolean append, String content) throws Exception {
        try (FileWriter writer = new FileWriter(filename, append)) {
            writer.write(content);
            System.out.println("Data is updated in file successfully");
        } catch (IOException e) {
        }
    }

    public static void main(String[] args) throws Exception {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Enter the title");
            String filename = reader.readLine();
            System.out.println("inputData:" + filename);


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
                counter = counter + 1;

                overwriteFile("counter.txt", false, Integer.toString(counter));
                overwriteFile("DS/" + filename + ".java", false, JAVA_CODE);
            }

        } catch (FileNotFoundException e) {
            System.out.println("File not found, an error occured");
            e.printStackTrace();
        }

    }
}
