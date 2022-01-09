import java.util.ArrayList;
import java.util.Arrays;

class Sentence {
    private ArrayList<String> characters = new ArrayList<>();

    Sentence(String sentence) {
        this.characters.addAll(Arrays.asList(sentence.split("")));
        System.out.println(this.characters);
    }

    public ArrayList<String> getCharacters() {
        return this.characters;
    }
}