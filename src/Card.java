import java.util.ArrayList;

public class Card {
    ArrayList<Note> notes = new ArrayList<>();

    Card(String hanzi, String pinyin, String english, String audio) {
        notes.add(new NHanzi(this, hanzi));
        notes.add(new NPinyin(this, pinyin));
        notes.add(new NEnglish(this, english));
        notes.add(new NAudio(this, audio));
    }
}
