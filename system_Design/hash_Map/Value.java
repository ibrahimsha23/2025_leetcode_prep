

public class Value {

    private int value;

    public Value(int v) {
        value = v;
    }

    public int getValue() {
        return value;
    }

    public boolean equals(Object obj) {
        return (this == obj);
    }

}
