public class Solution {
    public String fractionToDecimal(int A, int B) {
        LinkedHashMap<Long, Long> tem = new LinkedHashMap<>();
        StringBuilder sb = new StringBuilder();
        long p1 = A, p2 = B, x, y;
        if((A < 0 && B > 0) || (A > 0 && B < 0)){
            sb.append("-");
        }
        p1 = (long)Math.abs(p1);
        p2 = (long)Math.abs(p2);
        sb.append(p1 / p2);
        x = p1 % p2;
        while(x != 0 && !tem.containsKey(x)) {
            y = x * 10;
            tem.put(x, y / p2);
            x = y % B;
        }
        if(!tem.isEmpty()){
            sb.append(".");
        }
        for(Map.Entry<Long, Long> k : tem.entrySet()) {
            if(k.getKey() == x){
                sb.append("(");
            }
            sb.append(k.getValue());
        }
        if(x != 0){
            sb.append(")");
        }
        return sb.toString(); 
    }
}