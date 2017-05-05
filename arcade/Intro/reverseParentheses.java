String reverseParentheses(String s) {
         while(s.indexOf("(") != (-1)){
            int end = s.indexOf(")");
            int begin = s.substring(0, end+1).lastIndexOf("(");
            String t = reverse(s.substring(begin + 1, end));
            s = s.substring(0,begin) + t + s.substring(end+1,s.length());
        }
        return s;
}
public static String reverse(String s){
    return new StringBuffer(s).reverse().toString();
}