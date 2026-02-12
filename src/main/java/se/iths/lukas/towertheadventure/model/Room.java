package se.iths.lukas.towertheadventure.model;

import se.iths.lukas.towertheadventure.model.Enemy;

public class Room {
    private String name;
    private Enemy enemy;
    private String[] descriptions; // May cause problems later on, change top arrayList if needed.
    private int descriptionsIndex = 0;



    public Room(String name){
        this.name = name;
    }

    public Room(String name, String[] descriptions) {
        this.name = name;
        this.descriptions = descriptions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Enemy getEnemy() {
        return enemy;
    }

    public void setEnemy(Enemy enemy) {
        this.enemy = enemy;
    }

    public String getDescriptions() {
        String desc = descriptions[descriptionsIndex];
        if (descriptionsIndex == descriptions.length - 1){
            descriptionsIndex = 0;
        } else {
            descriptionsIndex++;
        }
        return desc;
    }

    public void setDescriptions(String[] descriptions) {
        this.descriptions = descriptions;
    }


}
