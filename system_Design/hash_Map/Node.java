public class Node<K,V>{
    private long hashVal;
    private K key;
    private V value;
    private Node<K,V> next;

    public K getKey(){
        return key;

    }

    public void setKey(K key){
        this.key = key;
    }

    public V getValue(){
        return value;
    }

    public void setValue(V value){
        this.value = value;
    }

    public Node<K, V> getNext(){
        return next;
    }

    public void setNext(Node<K, V> next){
        this.next = next;

    }

    public long getHashCode(){
        return hashVal;
    }

    public void setHashCode(long hashVal){
        this.hashVal = hashVal;
    }

}