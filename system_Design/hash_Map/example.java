import java.util.HashMap;

class example{
    public static void main(String[] args) {
        HashMap<String, Integer> dictionary = new HashMap<>(20);

        dictionary.put("Ibrahim", 10000);
        dictionary.put("Riz", 500000);
        dictionary.put("Extra", 15);


        // System.out.println(dictionary);

        System.out.println(dictionary.get("Ibrahim"));

        System.out.println(dictionary.containsKey("Riz"));

        System.out.println(dictionary.containsValue(50000));

        // HashMap(int initialCapacity, float loadFactor)



        
        
    }
}