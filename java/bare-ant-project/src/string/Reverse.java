package string;

public class Reverse {
    public String reverse(String str){
        if (str.length() == 0) 
            return str;

        return reverse(str.substring(1)) + str.charAt(0);

    }
}
