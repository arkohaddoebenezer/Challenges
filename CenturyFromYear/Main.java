public class Main {
    int getCentury(int year) {
        return (int) Math.ceil(year / 100.0);
    }

    public static void main(String[] args) {
        Main myObject = new Main();
        int year = 2024;
        int century = myObject.getCentury(year);

        System.out.println("Year: " + year + " is in the " + century + "th century.");
    }
}