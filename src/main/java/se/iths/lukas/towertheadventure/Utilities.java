package se.iths.lukas.towertheadventure;

public class Utilities {

    public static void printLetters(String word) {
        long typingSpeed = 60;
        for (int i = 0; i < word.length(); i++) {
            System.out.print(word.charAt(i));
            try {
                Thread.sleep(typingSpeed);
            } catch (InterruptedException e) {
                return;
            }
        }
        System.out.print("\n");
    }

}
