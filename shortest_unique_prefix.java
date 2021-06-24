public class Solution {
    public ArrayList<String> prefix(ArrayList<String> A) {
        ArrayList<String> result = new ArrayList<>();
        if(A.size() < 1)
            return result;
        for(String st : A) {
            int i = 1;
            ArrayList<String> tem = new ArrayList<>();
            tem.add(st.substring(0, i));
            while (A.stream().filter(k -> !k.equals(st)).anyMatch(k -> k.startsWith(tem.get(0)))){
                i++;
                if (i <= st.length())
                    tem.set(0, st.substring(0, i));
                else
                    break;
            }
            result.add(tem.get(0));
        }
        return result;
    }  
}
