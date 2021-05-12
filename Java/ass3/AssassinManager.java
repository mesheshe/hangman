import java.util.*;


public class AssassinManager {
    private AssassinNode killRingFront;
    private AssassinNode graveyardFront;

    public AssassinManager(List<String> names){
        if (names.isEmpty()){
            throw new IllegalArgumentException();
        }
        killRingFront = null;
        graveyardFront = null;
        for (int i = names.size() - 1; i >= 0; i--){
            killRingFront = new AssassinNode(names.get(i), killRingFront);
        }
    }

    void printKillRing(){
        AssassinNode current = killRingFront;
        if (killRingFront.next == null){
            System.out.println("    " + killRingFront.name + " is stalking " + killRingFront.name);
        }else{
            while (current.next != null){
                System.out.println("    " +current.name + " is stalking " + current.next.name);
                current = current.next; 
            }
            System.out.println("    " +current.name + " is stalking " + killRingFront.name);
        }
    }
    
    void printGraveyard(){
        if (graveyardFront == null){
            return;
        }
        AssassinNode current = graveyardFront;
        while (current != null){
            System.out.println("    " +current.name + " was killed by " + current.killer);
            current = current.next; 
        }
    }

    boolean killRingContains(String name){
        AssassinNode current = killRingFront;
        while (current != null){
            if (current.name.equalsIgnoreCase(name)){
                return true;
            }
            current = current.next; 
        }
        return false;
    }

    boolean graveyardContains(String name){
        AssassinNode current = graveyardFront;
        while (current != null){
            if (current.name.equalsIgnoreCase(name)){
                return true;
            }
            current = current.next; 
        }
        return false;
    }
    
    boolean gameOver(){
        if (killRingFront.next == null){
            return true;
        }else{
            return false;
        }
    }

    String winner(){
        if (gameOver()){
            return killRingFront.name;
        }else{
            return null;
        }
    }

    void kill(String name){
        // when transferring to the graveyard, this will be added in reverse order. Which means that the new person added becomes the front.
        // front = LL(name, front);   
        // for the purpose of printing out printgraveyard nicely
        AssassinNode current = killRingFront;
        AssassinNode next = current.next;
        AssassinNode nodeB4NameFound = null;
        AssassinNode nodeAtNameFound = null;
        if (next == null){
            throw new IllegalStateException();
        }else if (!killRingContains(name)){
            throw new IllegalArgumentException();
        }
        while (next != null){
            if (next.name.equalsIgnoreCase(name)){
                nodeB4NameFound = current;
                nodeAtNameFound = next;
            }
            current = next;
            next = current.next;
        }
        if (nodeB4NameFound == null){ // killingRingFront.name does equal name if nodeB4NameFound is null
            nodeAtNameFound = killRingFront;
            killRingFront = killRingFront.next;    // preserves killRingFront, since we will be working on what was the previously the killRingFront  

            nodeAtNameFound.next = graveyardFront;  
            graveyardFront = nodeAtNameFound;
            graveyardFront.killer = current.name;  // current currently holds the last node in the list. Since we just
                                                  // the first node was just killed off the list, then that person at the last node
        }else{                                    // must be the killer
            nodeB4NameFound.next = nodeB4NameFound.next.next;
            nodeAtNameFound.next = graveyardFront;
            graveyardFront = nodeAtNameFound;  // renaming 
            graveyardFront.killer = nodeB4NameFound.name;
        }
    }

}
    