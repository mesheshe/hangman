import java.util.*;

public class GrammarSolver {
    private SortedMap<String, List<List<String>>> mape;
    public GrammarSolver(List<String> grammar){
        if (grammar.isEmpty()){throw new IllegalArgumentException();}
        mape = new TreeMap<>();
        for (String h: grammar){
            String[] arr = h.split("::=");
            String key = arr[0];
            if (grammarContains(key)){   // can i call grammarcontains??
                throw new IllegalArgumentException();
            }
            String[] s = arr[1].trim().split("[|]+");
            mape.put(key, new ArrayList<>());
            for (String word: s){
                List<String> str = new ArrayList<>();
                splitter(word, str);
                mape.get(key).add(str);
            }
        }
    }
    private void splitter(String s, List<String> list){
        String[] str = s.trim().split("[ \t]+");
        for (String w: str){
            list.add(w);
        }
    }
    public boolean grammarContains(String symbol){
        return mape.containsKey(symbol);
    }

    private String lookThroughRule(List<String> list, String str){
        for (int i = 0; i < list.size(); i++){
            if (!grammarContains(list.get(i))){
                str+= list.get(i);                   //terminal rules get printed
            }else{
                str = generateRule(str, list.get(i)); //non-terminal gets called and then printed
            }
            if (i != list.size() - 1){
                str+= " ";
            }
        }
        return str;
    }
    private String generateRule(String returnString, String symbol){
        Random r = new Random();   // gets random index from a list where each index of an array holds a rule 
        int randomIndex = r.nextInt(mape.get(symbol).size());
        return lookThroughRule(mape.get(symbol).get(randomIndex), returnString);       
    }

    public String[] generate(String symbol, int times){
        if (!grammarContains(symbol) || times < 0){
            throw new IllegalArgumentException();
        }
        String splitaAndReturn = "";
        // start is to build a string up with all the grammar
        // separted by space if they are part of the same rule
        // otherwise separted by "|" for each new times
        for (int i = 0; i < times; i++){
            splitaAndReturn = generateRule(splitaAndReturn, symbol);
            if (i != times - 1){
                splitaAndReturn += "|";
            }
        }

        return splitaAndReturn.trim().split("[|]+");
    }

    public String getSymbols(){
        String returnString = "[";
        for (String e: mape.keySet()){
            if (returnString.equals("[")){
                returnString += e;
            }else{
                returnString += "," + e;
            }
        }
        return returnString + "]";
    }
}
