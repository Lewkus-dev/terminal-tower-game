package se.iths.lukas.towertheadventure;

import se.iths.lukas.towertheadventure.model.Player;
import se.iths.lukas.towertheadventure.model.Room;

import java.util.Scanner;

import static se.iths.lukas.towertheadventure.Utilities.printLetters;

public class Game {
    final private Scanner scanner;
    private Room[] rooms;
    static Game instance = null;
    private Player player;

//singleton!

    public Game(Scanner scanner) {
        this.scanner = scanner;
    }

    public void init(Scanner scanner){
        this.player = initPlayer(scanner);
        this.rooms = initRooms();
    }

    public Player initPlayer(Scanner scanner) {
        printLetters("Name your player:");
        String name = scanner.nextLine();
        return new Player(name);
    }

    public Room[] initRooms(){

        String[] cellarDescriptions = {
                "You are under the ground, its dark, and dank",
                "The dirt floor is cold and there is a foul stench"
        };

        String[] dungeonDescriptions = {
                "The smell of dried blood and tears fill the air." ,
                "The screams of pain still echo on these stone walls" ,
                "The remains of a man are chained to the crude stone wall."
        };

        String[] towerDescriptions = {
                "The winding stairs ascend higher than you are brave enough to climb." ,
                "The wind is howling through the windows" ,
                "The tower seems to sway in the storm." ,
                "The wind like the screams of those who died here."
        };


        Room cellar = new Room("Cellar", cellarDescriptions);
        Room dungeon = new Room("Dungeon", dungeonDescriptions);
        Room tower = new Room("Tower", towerDescriptions);

        return rooms = new Room[]{cellar, dungeon, tower};
    }

    public void gameLoop(){
        int choice;
        boolean isRunning = true;

        while (isRunning){
            showOverworld();
            choice = selectAction();
            isRunning = overworldMenu(choice, player, scanner);

        }
    }

    public boolean overworldMenu(int choice, Player player, Scanner scanner){
        boolean isRunning = true;
        switch (choice){
            case(1):
                printLetters("You chose 1.");
                break;
            case(2):
                printLetters("You chose 2.");
                player.setPosition(selectRoom() - 1);
                break;
            case(3):
                printLetters("You pick a fight");
                battleLoop();
                break;
            case(4):
                printLetters("Exiting game");
                isRunning = false;
                break;
        }
        return isRunning;
    }

    public void battleLoop(){
        printLetters("Your HP: ");
    }

    public void showOverworld(){
        int i = 0;
        int pos = player.getPosition();
        Room x = rooms[pos];
        printLetters(player.getPlayerName() + ". " + x.getDescriptions());

    }

    public int selectAction(){
        printLetters("What do you want to do?");
        printLetters("1. Look around");
        printLetters("2. Change rooms");
        printLetters("3. Pick a fight");
        printLetters("4. Exit game");
        return scanner.nextInt();
    }

    public int selectRoom(){
        printLetters("Where do you want to go?");
        printLetters("1. Cellar");
        printLetters("2. Dungeon");
        printLetters("3. Tower");
        return scanner.nextInt();
    }

    public static Game getInstance(Scanner scanner) {
        if (instance == null){
            return new Game(scanner);
        }
        return instance;
    }
}
