package se.iths.lukas.towertheadventure.model;


public class Player {
    private int maxHp;
    private int currentHp;
    private String playerName;
    private int position;


    public Player(String playerName) {
        this.currentHp = 15;
        this.maxHp = 15;
        this.playerName = playerName;
        this.position = 0;
    }

    public boolean is_dead(int currentHp) {
        return currentHp <= 0;
    }

    public int getCurrentHp() {
        return currentHp;
    }

    public void setCurrentHp(int currentHp) {
        this.currentHp = currentHp;
    }

    public String getPlayerName() {
        return playerName;
    }

    public void setPlayerName(String playerName) {
        this.playerName = playerName;
    }

    public void setPosition(int position){
        this.position = position;
    }

    public int getPosition(){
        return this.position;
    }
}
