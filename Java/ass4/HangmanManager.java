import java.util.*;

public class HangmanManager {
    private String returnPattern; 
    private Set<Character> letterGuessed;              // holds the letters guessed
    private Map<String, Set<String>> mapWord;          // maps the pattern to list of words that fit in that set
    private int numOfGuesses;                         // num of guesses

    HangmanManager(Collection<String> dictionary, int length, int max){
        if(length < 1 || max < 0){
            throw new IllegalArgumentException();
        }
        numOfGuesses = max;
        letterGuessed = new TreeSet<>();
        returnPattern = "-";
        for(int i = 1; i != length; i++){
            returnPattern += " -";
        }
        mapWord = new TreeMap<>();
        mapWord.put(returnPattern, new TreeSet<>());
        for (String w: dictionary){
            if (w.length() == length && !mapWord.get(returnPattern).contains(w)){
                mapWord.get(returnPattern).add(w);}
        }
    }
    
    public Map<String, Set<String>> returnMap(){return mapWord;}
   
    public Set<String> words(){return mapWord.get(returnPattern);}
 
    public int guessesLeft(){return numOfGuesses;}

    public Set<Character> guesses(){return letterGuessed;}

    public String pattern(){return returnPattern;}

    public int record(char guess){
        if (guessesLeft() < 1 || words().isEmpty()){throw new IllegalStateException();
        }else if(letterGuessed.contains(guess)){throw new IllegalArgumentException();}
        createNewMap(guess);
        int count = 0;
        for (int i = 0; i < returnPattern.length(); i++){
            if (returnPattern.charAt(i) == guess){count++;}
        }
        if (count == 0){numOfGuesses--;}
        letterGuessed.add(guess); // already know that letterGuessed doesn't contain guess       
        return count;
    }

    private void createNewMap(char guess){
        Map<String, Set<String>> newMap = new TreeMap<>();
        for (String word: words()){
            String newPattern = getNewPattern(returnPattern, word, guess);
            addToMap(newMap, newPattern, word);
        }
        int count = 0;
        for (String pattern: newMap.keySet()){
            if (newMap.get(pattern).size() > count){
                returnPattern = pattern;
                count = newMap.get(pattern).size();
            }
        }
        mapWord.put(returnPattern, newMap.get(returnPattern)); // This way I am not wasting memory. Only putting the winner in mapWord
    }

    private void addToMap(Map<String, Set<String>> newMap, String pattern, String word){
        if(!newMap.containsKey(pattern)){
            newMap.put(pattern, new TreeSet<>());
        }
        newMap.get(pattern).add(word);
    }

    private String getNewPattern(String old, String word, char target){
        for (int i = 0; i < word.length(); i++){
            if (word.toLowerCase().charAt(i) == target){
                int newIndex = 2*i;
                if (newIndex == 0){
                    old = target + old.substring(1);
                }else if (newIndex == old.length() - 1){
                    old = old.substring(0, old.length() - 1) + target;
                }else{
                    String str1 = old.substring(0, newIndex);
                    String str2 = old.substring(newIndex + 1);
                    old = str1 + target + str2;
                }
            }
        }
        return old;
    }

}
