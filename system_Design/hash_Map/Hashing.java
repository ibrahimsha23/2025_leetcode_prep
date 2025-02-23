class Hashing{
    public static void main(String[] args) {
        String name = "Ibrahim";
        Integer hashcodeVal = name.hashCode();
        System.out.println(hashcodeVal);
        System.out.println(hashcodeVal%11);
    }
}