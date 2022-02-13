import java.util.ArrayList;
import java.util.Arrays;

class Sentence {

    private ArrayList<String> characters = new ArrayList<>();
    private Spoken spoken;
    private LearningProgress progress;

    Sentence(String sentence, String audioPath) {
        this.characters.addAll(Arrays.asList(sentence.split("")));
        this.spoken = new Spoken(audioPath);
        this.progress = new LearningProgress();
        System.out.println();
    }

    public ArrayList<String> getCharacters() {
        return this.characters;
    }

    public void setCharacters(ArrayList<String> characters) {
        this.characters = characters;
    }

    @Override
    public String toString() {
        return "Sentence{" +
                String.join("", this.characters) +
                spoken.getPath() +
                progress.toString() +
                '}';
    }
}