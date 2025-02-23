import java.util.LinkedList;

public class HashMapImpl{
    LinkedList<Entry>[] hashMap = new LinkedList[2];
    int size =0;

    public HashMapImpl(){

    }

    public void resize(){
    }

    public void put(Key k, Value v){

        if(size >= hashMap.length){
            resize();
        }

        int ix = getIndex(k) % hashMap.length;

        if (hashMap[ix] == null) {
            hashMap[ix] = new LinkedList<>();
            hashMap[ix].add(new Entry(k, v));
        }else{
            for (Entry entry: hashMap[ix]){
                if(entry.key.equals(k)){
                    entry.value = v;
                    size++;
                    return;
                }
                else{

                }
            }

        }
    }


    public Value get(Key k){
        int ix = Key.getIndex(k) % hashMap.length;

        if (hashMap[ix]==null){
            return null;
        }

        
        for (Entry entry: hashMap[ix]){
            if(entry.key.equals(k)){
                return entry.value;
            }
        }

    }


    public void remove(Key k){
        int ix = Key.getIndex(k) % hashMap.length;


    }
}