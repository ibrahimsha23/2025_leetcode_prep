
import java.util.Objects;

public class Key {

    private int key;

    public Key(int k) {
        key = k;
    }

    public int hashCode() {
        return Objects.hash(key); //returns unique number;
    }

    public boolean equals(Object obj) {
        return (this == obj);
    }
}
