// Class HangmanMain is the driver program for the Hangman program.  It reads a
// dictionary of words to be used during the game and then plays a game with
// the user.  This is a cheating version of hangman that delays picking a word
// to keep its options open.  You can change the setting for SHOW_COUNT to see
// how many options are still left on each turn.

import java.util.*;
import java.io.*;

public class modHangmanMain  {
    public static final String DICTIONARY_FILE = "dictionary.txt";
    public static final boolean SHOW_COUNT = true;  // show # of choices left

    public static void main(String[] args) throws FileNotFoundException {
        runThisBeforeAnything();
        System.out.println("Welcome to the cse143 hangman game.");
        System.out.println();

        // open the dictionary file and read dictionary into an ArrayList
        Scanner input = new Scanner(new File("java\\ass4\\"+DICTIONARY_FILE));
        Scanner input2 = new Scanner(new File("java\\ass4\\test2.txt"));
        List<String> dictionary = new ArrayList<>();
        while (input.hasNext()) {
            dictionary.add(input.next().toLowerCase());
        }

        // set basic parameters
        Scanner console = new Scanner(System.in);
        int length = input2.nextInt();// console.nextInt();
        System.out.println("What length word do you want to use? "+length);
        int max = input2.nextInt();//.nextInt();
        System.out.println("How many wrong answers allowed? "+max);
        System.out.println();

        // set up the HangmanManager and start the game
        List<String> dictionary2 = Collections.unmodifiableList(dictionary);
        HangmanManager hangman = new HangmanManager(dictionary2, length, max);
        if (hangman.words().isEmpty()) {
            System.out.println("No words of that length in the dictionary.");
        } else {
            playGame(console, hangman,input2);
            showResults(hangman);
        }
    }

    // Plays one game with the user
    public static void playGame(Scanner console, HangmanManager hangman, Scanner test) {
        while (hangman.guessesLeft() > 0 && hangman.pattern().contains("-")) {
            System.out.println("guesses : " + hangman.guessesLeft());
            if (SHOW_COUNT) {
                System.out.println("words   : " + hangman.words().size());
            }
            System.out.println("guessed : " + hangman.guesses());
            System.out.println("current : " + hangman.pattern());
            char ch = test.next().charAt(0);
            System.out.println("Your guess? " + ch);
            //char ch = console.next().toLowerCase().charAt(0);
            if (hangman.guesses().contains(ch)) {
                System.out.println("You already guessed that");
            } else {
                int count = hangman.record(ch);
                if (count == 0) {
                    System.out.println("Sorry, there are no " + ch + "'s");
                } else if (count == 1) {
                    System.out.println("Yes, there is one " + ch);
                } else {
                    System.out.println("Yes, there are " + count + " " + ch +
                                       "'s");
                }
            }
            System.out.println();
        }
    }

    public static void runThisBeforeAnything() throws FileNotFoundException {
        Scanner file = new Scanner(new File("java\\ass4\\test.txt"));
        PrintStream output = new PrintStream(new File("java\\ass4\\test2.txt"));
        String returnString;
        file.nextLine();  //Welcome to the cse143...
        file.nextLine();  //blank line
        for (int i = 0; i < 2; i++){
            returnString = file.nextLine();   //Could be: What length... How many wrong...
            int index  = returnString.length()- 1;
            while (returnString.charAt(index) != ' '){  // figuring out where last value starts
                index--;
            }
            output.println(returnString.substring(index + 1)); //pushing the number at the end of line above to the file
        }
        String test;
        while (file.hasNextLine()){
            file.nextLine();                   // blank line
            test = file.nextLine();            // Could be - guesses : .... answer = ..... No words ...
            if (test.contains("answer =") || test.contains("No words")){
                break;
            }
            if (SHOW_COUNT){
                file.nextLine();              // words : ...
            }
            file.nextLine();                  // guessed : [] ...
            file.nextLine();                  // current : .... 
            returnString = file.nextLine();   // Your guess? x ....
            output.println(returnString.substring(returnString.length()-1));  // pushes x to file
            file.nextLine();                 // Sorry, there are no.... Yes, there is ....
        }
    }

    // reports the results of the game, including showing the answer
    public static void showResults(HangmanManager hangman) {
        // if the game is over, the answer is the first word in the list
        // of words, so we use an iterator to get it
        String answer = hangman.words().iterator().next();
        System.out.println("answer = " + answer);
        if (hangman.guessesLeft() > 0) {
            System.out.println("You beat me");
        } else {
            System.out.println("Sorry, you lose");
        }
    }
}
