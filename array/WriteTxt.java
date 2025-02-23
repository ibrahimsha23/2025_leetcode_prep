
import java.io.FileWriter;
import java.io.IOException;

class WriteTxt {

    public static void main(String[] args) throws Exception {

        boolean append = false;
        try (FileWriter writer = new FileWriter("counter.txt", append)) {
            writer.write("IBRAHIM_RIZWANA_");
        } catch (IOException e) {
        }
    }
}
