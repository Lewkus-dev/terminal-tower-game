package se.iths.lukas.towertheadventure;

import java.util.Scanner;

import static se.iths.lukas.towertheadventure.Utilities.printLetters;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Game game = Game.getInstance(scanner);

        game.init(scanner);

        game.gameLoop();

        printLetters("Thank you for playing!");

    }

}

//TODO: implement maidens, who are the object of the game.
// rescue the maidens by leading them out of the tower.
// maidens they give birth to your sons and over time you build an army to win the war.

// the higher up into the tower you climb, the more maidens you can rescue.
// but you can't leave the maidens alone or they will get lost and wander to some other part of the tower.
// you can't let the maidens die, and you can't leave them alone
// the more maidens you rescue, the more children you can breed.
// sons give attack to your army
// daughters give heath to your army