
import java.nio.file.Files;
import java.nio.file.Paths;

public class ReadAll {

    public static String readFileAsString(String filename) throws Exception {
        String data = "";

        try {

            data = new String(Files.readAllBytes(Paths.get(filename)));
            

        } catch (OutOfMemoryError oome) {
            //Log the info
            System.err.println("Array size too large");
            System.out.println("Heap max size: " + (Runtime.getRuntime().maxMemory() / 1024 / 1024 / 1024) + "GB");

        }
    return data;

    }

    public static void main(String[] args) throws Exception {
        String weatherData = readFileAsString("/Users/mac-IKASIM01/decathlon/gym/1brc/measurements.txt");
        System.out.println(weatherData);

    }
}
