import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Map;
import java.util.HashMap;

// カッコ対応版
class Solution{
    // 演算子の優先順位を返す関数
    public static int getPriority(String op) {
        Map<String, Integer> map = new HashMap<>() {
            {
                put("*",3);
                put("/",3);
                put("+",2);
                put("-",2);
                put("(",1);
                put(")",1);
            }
        };
        return map.getOrDefault(op, 0);
    }

    // Stringの数字と演算子を受け取って計算結果を返す関数
    public static String applyOperation(String op1, String op2, String operator){
        long num1 = Long.parseLong(op1);
        long num2 = Long.parseLong(op2);

        String result = "";
        if(operator.equals("+")) result += (num2 + num1);
        if(operator.equals("-")) result += (num2 - num1);
        if(operator.equals("*")) result += (num2 * num1);
        if(operator.equals("/") && num1==0) result += num2;
        else if(operator.equals("/")) result += num2/num1;

        return result;
    }
    public static long expressionParenthesisParser(String expression){
        // 関数を完成させてください
        Deque<String> nums = new ArrayDeque<>();
        Deque<String> ops = new ArrayDeque<>();

        for (int i = 0; i < expression.length(); i++) {

            // 演算子が来たときの処理
            if (!Character.isDigit(expression.charAt(i))) {
                String currOP = expression.charAt(i) + "";
                if (currOP.equals("(")) {
                    ops.push(currOP);
                }
                // )が来たときの処理
                else if (currOP.equals(")")){//　")"がきたら"("がくるまで計算　　
                    String stackTop = ops.pop();
                    while(!stackTop.equals("(")){
                        String res = applyOperation(nums.pop(), nums.pop(), stackTop);
                        nums.push(res);
                        stackTop = ops.pop();
                    }
                }

                else {
                    while (!ops.isEmpty() && getPriority(currOP) <= getPriority(ops.peek())) {
                        String result = applyOperation(nums.pop(), nums.pop(), ops.pop());
                        nums.push(result);
                    }
                    ops.push(currOP+"");
                }
            }

            // 数字が来たときの処理
            else {
                String number = "";
                // 2桁以上の数字に対応
                while (i < expression.length() && Character.isDigit(expression.charAt(i))) {
                    number += expression.charAt(i);
                    i++;
                }
                i--;
                nums.push(number);
            }
        }

        while (!ops.isEmpty()) {
            String result = applyOperation(nums.pop(),nums.pop(), ops.pop());
            nums.push(result);
        }

        return Long.parseLong(nums.peek());

    }
}
